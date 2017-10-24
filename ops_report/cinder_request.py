# -*- coding: utf-8 -*-
import json

from ops_report import common


class CinderClient(object):

    def __init__(self, token, cinder_ip=None, port=None, project_id=None, ssl=None):
        self.cinder_ip = cinder_ip
        self.port = port if port.upper() != 'NONE' else None
        self.token = token
        self.project_id = project_id
        self.ssl = ssl
    def pools_stats(self):
        if self.port is None:
            full_url_cinder = '{0}://{1}/v2/' \
                            '{2}/scheduler-stats/get_pools?detail=True'.format(self.ssl,self.cinder_ip,self.project_id)
        else:
            full_url_cinder = '{0}://{1}:{2}/v2/' \
                            '{3}/scheduler-stats/get_pools?detail=True'.format(self.ssl,self.cinder_ip,
                                                           self.port,self.project_id)
        headers = {
            'X-Auth-Token': self.token,
            'Content-Type': 'application/json'
        }
        stats_pools = common.send_get_request(full_url_cinder, headers=headers)
        result = stats_pools.result().json()
        return result


    def pools_stats_detail(self):
        """Get a list of pool.
        :return: Output is Total capacity and used capacity in GB
        """
        list_pools = self.pools_stats().get('pools')
       # print(list_pools)
        output = {}
        for pool in list_pools:
            key_name_pool = pool.get('capabilities').get('volume_backend_name')
            output[key_name_pool] = {}
            output[key_name_pool].update({'total_gb': pool.get('capabilities').get(
                'total_capacity_gb')})
            output[key_name_pool].update({'used_gb': (pool.get('capabilities').get(
                'total_capacity_gb')) - (pool.get('capabilities').get(
                'free_capacity_gb'))})
        return output
