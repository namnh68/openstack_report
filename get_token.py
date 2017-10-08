# _*_ coding:utf-8 _*_
from keystoneauth1.identity import v3
from keystoneauth1 import session


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
