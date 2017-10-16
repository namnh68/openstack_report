#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from datetime import datetime

from ops_report import common
from ops_report import config
from ops_report import email
from ops_report import generate_excel
from ops_report import nova_request
from ops_report import zabbix_request


def gen_name_report():
    path_dir = os.path.dirname(os.path.abspath(__file__))
    name_file = 'openstack_report_' + datetime.now().strftime(
        '%Y_%m_%d_%Hh_%M_%Ss') + '.xlsx'
    full_name_path = os.path.join(path_dir, name_file)
    return full_name_path


def main():
    # For OpenStack
    user_admin = config.user_admin
    pass_admin = config.pass_admin
    keystone_ip = config.keystone_ip
    nova_ip = config.nova_ip
    nova_port = config.nova_port
    project_name = config.project_name
    ratio_ram = config.ratio_ram
    ratio_cpu = config.ratio_cpu

    # For Zabbix
    user_zabbix = config.user_zabbix
    pass_zabbix = config.pass_admin
    zabbix_ip = config.zabbix_ip
    zabbix_port = config.zabbix_port

    # For sending emails
    email_from = config.email_from
    pass_email_from = config.pass_email_from
    email_to = config.email_to
    email_server = config.email_server

    # Step 1: Get token version 3
    token = common.get_token_v3(keystone_ip=keystone_ip, username=user_admin,
                                password=pass_admin, project_name=project_name)

    # Step 2: Get Hypervisors information from Nova
    nova_client = nova_request.NovaClient(token=token, nova_ip=nova_ip,
                                          port=nova_port)
    nova_hyper_list = nova_client.hyper_list_customize(ratio_ram=ratio_ram,
                                                       ratio_cpu=ratio_cpu)

    # Step 3: Get information from Zabbix
    zabbix_client = zabbix_request.ZabbixClient(user_zabbix=user_zabbix,
                                                pass_zabbix=pass_zabbix,
                                                zabbix_ip=zabbix_ip,
                                                zabbix_port=zabbix_port)
    for name_compute, params in nova_hyper_list.items():
        compute_zabbix = config.mapping[name_compute]
        if compute_zabbix is not None:
            real_params = zabbix_client.get_param_host(compute_zabbix)
            nova_hyper_list[name_compute].update(real_params)
        else:
            pass

    # Step 4: From nova_hyper_list, writing to excel file
    path_name_file = gen_name_report()
    generate_excel.write_xls(file_name=path_name_file, data=nova_hyper_list)

    # Step 5: After having this file, then it needs to send the file to Admin.
    email.send_mail(send_from=email_from, password=pass_email_from,
                    send_to=email_to, path_file=path_name_file,
                    server=email_server)
