# _*_ coding:utf-8 _*_
# Reference: https://github.com/daikk115/openstack_upgrade_test
from __future__ import division
import math

from keystoneauth1.identity import v2
from keystoneauth1.identity import v3
from keystoneauth1 import session
from requests_futures.sessions import FuturesSession

future_session = FuturesSession()


def send_request(url, method, headers=None, data=None, **kwargs):
    """
    This method for the near future
    """
    if method == 'GET':
        return future_session.get(url, headers=headers, **kwargs)
    elif method == 'POST':
        return future_session.post(url, headers=headers, data=data, **kwargs)
    elif method == 'PUT':
        return future_session.put(url, headers=headers, data=data, **kwargs)
    elif method == 'PATCH':
        return future_session.patch(url, headers=headers, data=data, **kwargs)
    elif method == 'DELETE':
        return future_session.delete(url, headers=headers, **kwargs)
    else:
        print("Method does not support: {}".format(method))


def send_get_request(url, headers=None, **kwargs):
    return future_session.get(url, headers=headers, **kwargs)


def get_token_v3(keystone_ip, username, password, project_name):
    """
    :param keystone_ip: a IP of keystone to get token
    :param username: username
    :param password: password
    :param project_name: project_name
    :return: token and project_id
    """

    auth_url = 'http://{}/identity/v3'.format(keystone_ip)
    auth = v3.Password(auth_url=auth_url, user_domain_name='default',
                       username=username, password=password,
                       project_domain_name='default',
                       project_name=project_name)

    sess = session.Session(auth=auth)
    token = sess.get_token()
    return token


def get_token_v2(keystone_ip, username, password, tenant_name):
    auth_url = 'http://{}:5000/v2.0'.format(keystone_ip)
    auth = v2.Password(auth_url=auth_url, username=username,
                       password=password, tenant_name=tenant_name)
    sess = session.Session(auth=auth)
    token = sess.get_token()
    return token


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0 B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "{0} {1}".format(s, size_name[i])


def byte_to_mb(size_byte):
    if size_byte <= 0:
        return 0
    else:
        mb = size_byte/1048576
        return mb
