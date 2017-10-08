# _*_ coding:utf-8 _*_
from requests_futures.sessions import FuturesSession

future_session = FuturesSession()


def send_request(url, method, headers=None, data=None, **kwargs):
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
