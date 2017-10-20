# -*- coding: utf-8 -*-
from zabbix.api import ZabbixAPI


def get_zabbix(username, password, ip_zabbix, port):
    url = 'http://{0}:{1}/zabbix'.format(ip_zabbix, port)
    return ZabbixAPI(url=url, user=username, password=password)


class ZabbixClient(object):

    def __init__(self, user_zabbix, pass_zabbix, zabbix_ip, zabbix_port):
        self.username = user_zabbix
        self.password = pass_zabbix
        self.ip_zabbix = zabbix_ip
        self.zabbix_port = zabbix_port
        self.session = get_zabbix(self.username, self.password,
                                  self.ip_zabbix, self.zabbix_port)

    def get_param_host(self, hostname):

    #    output = {real_memory_used: 0, real_memory: 0, percent_CPU: 0}
        output = {}
        data = {
            "output": "extend",
            "host": hostname,
            "filter": {
                'key_': ["vm.memory.size[available]",
                         "vm.memory.size[total]",
                         "system.cpu.util[,system]"]
            },
            "sortfield": "name"
        }

        hosts = self.session.do_request(method='item.get', params=data)
        results = hosts.get('result')
        for result in results:
            if result.get('key_') == "vm.memory.size[available]":
                output['real_memory_used'] = int(result.get('lastvalue'))
            elif result.get('key_') == "vm.memory.size[total]":
                output['real_memory_mb'] = int(result.get('lastvalue'))
            elif result.get('key_') == "system.cpu.util[,system]":
                output['percent_cpu'] = float(result.get('lastvalue'))
            else:
                pass
        return output

# b = ZabbixClient(user_zabbix='Admin', pass_zabbix='zabbix',
#                  zabbix_ip='192.168.100.8', zabbix_port='81')
# c = b.get_param_host(hostname='controller')
# a = 1