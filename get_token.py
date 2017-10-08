# _*_ coding:utf-8 _*_
from keystoneauth1.identity import v3
from keystoneauth1 import session


def get_token(auth_url, username, password, project_name):

    auth = v3.Password(auth_url=auth_url, user_domain_name='default',
                       username=username, password=password,
                       project_domain_name='default',
                       project_name=project_name)

    session_ = session.Session(auth=auth)
    token = session_.get_token()
    project_id = session_.get_project_id()
    return token, project_id
