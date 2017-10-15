#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from datetime import datetime

from ops_report import common
from ops_report import config
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

    # For Zabbix
    user_zabbix = config.user_zabbix
    pass_zabbix = config.pass_admin
    zabbix_ip = config.zabbix_ip
    zabbix_port = config.zabbix_port

    # For sending emails
    email_from = config.email_from
    pass_email_from = config.pass_email_from
    email_to = config.email_to

    # Step 1: Get token version 3
    token = common.get_token_v3(keystone_ip=keystone_ip, username=user_admin,
                                password=pass_admin, project_name=project_name)

    # Step 2: Get Hypervisors information from Nova
    nova_client = nova_request.NovaClient(token=token, nova_ip=nova_ip)
    nova_hyper_list = nova_client.hyper_list_customize()

    # Step 3: Get information from Zabbix
    zabbix_client = zabbix_request.ZabbixClient(user_zabbix=user_zabbix,
                                                pass_zabbix=pass_zabbix,
                                                zabbix_ip=zabbix_ip)
