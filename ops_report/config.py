# For OpenStack
user_admin = 'admin'
pass_admin = 'password'
keystone_ip = '192.168.100.103'
nova_ip = '192.168.100.103'
nova_port = '8776'
project_name = 'admin'

# For Zabbix
user_zabbix = 'Admin'
pass_zabbix = 'zabbix'
ip_zabbix = '192.168.100.105'

# For sending emails
email_from = 'test@gmail.com'
pass_email_from = '123456'
email_to = 'test_to@gmail.com'

# Mapping Nova with Zabbix

mapping = {
    'compute1': 'compute1_zabbix',
    'compute2': 'compute2_zabbix'
}
