# -*- coding: utf-8 -*-
import json

import config
from ops_report import common


class NovaClient(object):

    def __init__(self, token, ip_nova=None, port=None):
        self.ip_nova = ip_nova
        self.port = str(port)
        self.token = token

    def hyper_list(self):
        ip_nova = config.ip_keystone if self.ip_nova is None else self.ip_nova
        if self.port is None:
            full_url_nova = 'http://{0}/compute/v2.1/' \
                            'os-hypervisors/detail'.format(ip_nova)
        else:
            full_url_nova = 'http://{0}:{1}/v2/' \
                            'os-hypervisors/detail'.format(ip_nova, self.port)
        headers = {
            'X-Auth-Token': self.token,
            'Content-Type': 'application/json'
        }
        list_hyper = common.send_get_request(full_url_nova, headers=headers)
        result = list_hyper.result().content
        return json.loads(result)

    def hyper_show(self, id_compute):
        """
        :param id_compute: ID of compute
        :return: Detail of a compute
        :type: dictionary
        """
        ip_nova = config.ip_keystone if self.ip_nova is None else self.ip_nova
        if self.port is None:
            url_nova = 'http://{0}/compute/v2.1/os-hypervisors/{1}'. \
                format(ip_nova, id_compute)
        else:
            url_nova = 'http://{0}:{1}/v2/os-hypervisors/{2}'.format(ip_nova,
                                                                     self.port,
                                                                     id_compute)
        headers = {
            'X-Auth-Token': self.token,
            'Content-Type': 'application/json'
        }
        show_hyper = common.send_get_request(url_nova, headers=headers)
        result = show_hyper.result().content
        return json.loads(result)

    def hyper_list_customize(self):
        """Get a list of hypervisor.
        :return: Output will be customized with Ram, CPU
        """
        list_hyper = self.hyper_list().get('hypervisors')
        output = {}
        for hypervisor in list_hyper:
            key_name_compute = hypervisor.get('hypervisor_hostname')
            output[key_name_compute] = {}
            output[key_name_compute].update({'memory_mb_used': hypervisor.get(
                'memory_mb_used')})
            output[key_name_compute].update({'memory_db': hypervisor.get(
                'memory_mb')})
            output[key_name_compute].update({'vcpu_used': hypervisor.get(
                'vcpus_used')})
            output[key_name_compute].update({'vcpus': hypervisor.get(
                'vcpus')})
        return output

token = common.get_token_v2(ip_keystone=config.ip_keystone,
                            username=config.username,
                            password=config.password,
                            tenant_name=config.project_name)

a = NovaClient(token=token, port=8774)
b = a.hyper_list_customize()
c = 1