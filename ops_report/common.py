# _*_ coding:utf-8 _*_
# Reference: https://github.com/daikk115/openstack_upgrade_test

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


def get_token(ip_keystone, username, password, project_name):
    """
    :param ip_keystone: a IP of keystone to get token
    :param username: username
    :param password: password
    :param project_name: project_name
    :return: token and project_id
    """

    auth_url = 'http://{}/identity/v3'.format(ip_keystone)
    auth = v3.Password(auth_url=auth_url, user_domain_name='default',
                       username=username, password=password,
                       project_domain_name='default',
                       project_name=project_name)

    session_ = session.Session(auth=auth)
    token = session_.get_token()
    project_id = session_.get_project_id()
    return token, project_id
