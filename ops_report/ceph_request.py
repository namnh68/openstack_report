#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import requests
#import generate_excel_ceph
#import os
#from datetime import datetime
from ops_report import common


from requests_futures.sessions import FuturesSession
future_session = FuturesSession()

class CephClient(object):

# def gen_name_report():
#     path_dir = os.path.dirname(os.path.abspath(__file__))
#     name_file = 'ceph_report_' + datetime.now().strftime(
#         '%Y_%m_%d_%Hh_%M_%Ss') + '.xlsx'
#     full_name_path = os.path.join(path_dir, name_file)
#     return full_name_path
    def __init__(self, ceph_ip, ceph_port):

        self.ceph_ip = ceph_ip
        self.ceph_port = ceph_port


    def get_param_pool(self):
        full_url = 'http://{0}:{1}/api/v0.1/df?detail'.format(self.ceph_ip, self.ceph_port)
        headers = {'Accept': 'application/json'}
        status = common.send_get_request(full_url, headers=headers)
        #response = requests.get(full_url,headers=headers )
        result = status.result().json()
        pools = result.get('output').get('pools')
       # for i in pools:
       #     print i.get('stats').get('bytes_used')
       #     print i.get('stats').get('max_avail')

        output = {}
        for pool in pools:
            keyname_pool = pool.get('name')
            output[keyname_pool] = {}
            # output[keyname_pool].update({'used_mb':0})
            # output[keyname_pool].update({'total_mb':0})
            output[keyname_pool].update({'real_used_mb': pool.get('stats').get('bytes_used')})
            output[keyname_pool].update({'real_total_mb': pool.get('stats').get('max_avail')})
        return output

# def main():
#     path_name_file = gen_name_report()
#     print(path_name_file)
#     print(connect_ceph())
#     generate_excel_ceph.write_xls(file_name=path_name_file, data=connect_ceph())
#
# if __name__ == '__main__':
#     main()
