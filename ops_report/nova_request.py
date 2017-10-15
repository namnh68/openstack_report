# -*- coding: utf-8 -*-
import json

from ops_report import common


class NovaClient(object):

    def __init__(self, token, nova_ip=None, port=None):
        self.nova_ip = nova_ip
        self.port = str(port)
        self.token = token

    def hyper_list(self):
        if self.port is None:
            full_url_nova = 'http://{0}/compute/v2.1/' \
                            'os-hypervisors/detail'.format(self.nova_ip)
        else:
            full_url_nova = 'http://{0}:{1}/v2/' \
                            'os-hypervisors/detail'.format(self.nova_ip,
                                                           self.port)
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
        if self.port is None:
            url_nova = 'http://{0}/compute/v2.1/os-hypervisors/{1}'. \
                format(self.nova_ip, id_compute)
        else:
            url_nova = 'http://{0}:{1}/v2/os-hypervisors/{2}'.\
                format(self.nova_ip, self.port, id_compute)
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

# token = common.get_token_v2(keystone_ip=config.ip_keystone,
#                             username=config.username,
#                             password=config.password,
#                             tenant_name=config.project_name)
#
# a = NovaClient(token=token, port=8774)
# b = a.hyper_list_customize()
# c = 1