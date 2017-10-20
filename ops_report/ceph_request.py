#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from ops_report import common

class CephClient(object):

    def __init__(self, ceph_ip, ceph_port):

        self.ceph_ip = ceph_ip
        self.ceph_port = ceph_port


    def get_param_pool(self):
        full_url = 'http://{0}:{1}/api/v0.1/df?detail'.format(self.ceph_ip, self.ceph_port)
        headers = {'Accept': 'application/json'}
        status = common.send_get_request(full_url, headers=headers)
        result = status.result().json()
        pools = result.get('output').get('pools')

        output = {}
        for pool in pools:
            keyname_pool = pool.get('name')
            output[keyname_pool] = {}
            output[keyname_pool].update({'real_used_mb': pool.get('stats').get('bytes_used')})
            output[keyname_pool].update({'real_total_mb': pool.get('stats').get('max_avail')})
        return output
