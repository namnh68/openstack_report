#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from datetime import datetime

from ops_report import common
from ops_report import config
#from ops_report import send_email
from ops_report import generate_excel_ceph
from ops_report import cinder_request
from ops_report import ceph_request


def gen_name_report():
    path_dir = os.path.dirname(os.path.abspath(__file__))
    name_file = 'ceph_report_' + datetime.now().strftime(
        '%Y_%m_%d_%Hh_%M_%Ss') + '.xlsx'
    full_name_path = os.path.join(path_dir, name_file)
    return full_name_path


def main():
    # For OpenStack
    user_admin = config.user_admin
    pass_admin = config.pass_admin
    keystone_ip = config.keystone_ip
    cinder_ip = config.cinder_ip
    cinder_port = config.cinder_port
    project_name = config.project_name
    project_id = config.project_id

    # For Ceph
    ceph_ip = config.ceph_ip
    ceph_port = config.ceph_port

    #
    # # For sending emails
    # email_from = config.email_from
    # pass_email_from = config.pass_email_from
    # email_to = config.email_to
    # email_server = config.email_server

    # Step 1: Get token version 3
    token = common.get_token_v3(keystone_ip=keystone_ip, username=user_admin, password=pass_admin, project_name=project_name)

    # Step 2: Get Hypervisors information from Nova
    cinder_client = cinder_request.CinderClient(token=token, cinder_ip=cinder_ip,
                                          port=cinder_port, project_id=project_id)
    cinder_pools_list = cinder_client.pools_stats_detail()

    ceph_client = ceph_request.CephClient(ceph_ip=ceph_ip, ceph_port=ceph_port)

    ceph_pool_list = ceph_client.get_param_pool()

    # Step 3: Get information from Ceph
    for pool_ceph, params in ceph_pool_list.items():
        try:
            pool_ops = config.mapping.keys()[config.mapping.values().index(pool_ceph)]
       # if pool_ops is not None:
            theory_params = cinder_pools_list[pool_ops]
            ceph_pool_list[pool_ceph].update(theory_params)
       # else:
        except Exception as e:
            theory_params = {'total_mb':0, 'used_mb':0}
            ceph_pool_list[pool_ceph].update(theory_params)

    # Step 4: From cinder_pools_list, writing to excel file
    path_name_file = gen_name_report()
    generate_excel_ceph.write_xls(file_name=path_name_file, data=ceph_pool_list)

    # Step 5: After having this file, then it needs to send the file to Admin.
 #   send_email.send_mail(send_from=email_from, password=pass_email_from,
 #                   send_to=email_to, path_file=path_name_file,
  #                  server=email_server)

if __name__ == '__main__':
    main()
