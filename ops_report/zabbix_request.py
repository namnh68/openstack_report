# -*- coding: utf-8 -*-
from zabbix.api import ZabbixAPI


def get_zabbix(username, password, ip_zabbix, port):
    url = 'http://{0}:{1}'.format(ip_zabbix, port)
    return ZabbixAPI(url=url, user=username, password=password)


class ZabbixClient(object):

    def __init__(self, user_zabbix, pass_zabbix, zabbix_ip):
        self.username = user_zabbix
        self.password = pass_zabbix
        self.ip_zabbix = zabbix_ip
        self.session = get_zabbix(self.username, self.password, self.ip_zabbix)

    def get_param_host(self, hostname):

        data = {
            "output": "extend",
            "host": hostname,
            "filter": {
                'key_': ["vm.memory.size[available]",
                         "vm.memory.size[total]"]
            },
            "sortfield": "name"
        }

        hosts = self.session.do_request(method='item.get', params=data)
        return hosts.get('result')

# b = ZabbixClient(username='Admin', password='zabbix',
#                  ip_zabbix='192.168.100.8')
# c = b.get_param_host(hostname='controller')
# a = 1