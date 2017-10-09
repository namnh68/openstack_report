# -*- coding: utf-8 -*-
import json

import config
from ops_report import common


def hyper_list(url=None, token=None):

    url_nova = config.ip_keystone if url is None else url
    full_url_nova = 'http://{0}/compute/v2.1/os-hypervisors/detail'.format(url_nova)
    headers = {
        'X-Auth-Token': token,
        'Content-Type': 'application/json'
    }
    list_hyper = common.send_get_request(full_url_nova, headers=headers)
    result = list_hyper.result().content
    return json.loads(result)


def hyper_show(id_compute, url_nova=None, token=None):
    url_nova = config.ip_keystone if url_nova is None else url_nova
    full_url_nova = 'http://{0}/compute/v2.1/os-hypervisors/{1}'.\
        format(url_nova, id_compute)
    headers = {
        'X-Auth-Token': token,
        'Content-Type': 'application/json'
    }
    show_hyper = common.send_get_request(full_url_nova, headers=headers)
    result = show_hyper.result().content
    return json.loads(result)
