# -*- coding: utf-8 -*-
from zabbix.api import ZabbixAPI


zabi = None


def _get(global_za, za):
    if not global_za:
        global_za = za
    return global_za


def set_zabbix(url, username, password):
    zabi = ZabbixAPI(url=url, user=username, password=password)
    return zabi


def get_zabbix(url, username, password):
    global zabi
    return _get(zabi, set_zabbix(url, username, password))


