# For OpenStack
user_admin = 'admin'
pass_admin = 'cd883c249b92bbd3eb05'
#pass_admin = 'Welcome123'
keystone_ip = '172.16.69.50'
nova_ip = '172.16.69.50'
nova_port = '8774'
ratio_ram = '1.5'
ratio_cpu = '1.5'
project_name = 'admin'
project_id = 'e42a00c2ba6c4bbaa4bf4d8d22e260c2'
cinder_ip = '172.16.69.50'
cinder_port = '8776'
ssl = 'https'

# For Zabbix
user_zabbix = 'Admin'
pass_zabbix = 'zabbix'
zabbix_ip = '192.168.100.105'
zabbix_port = '80'

# For Ceph
ceph_ip = '172.16.69.167'
ceph_port = '5000'

# For sending emails
email_from = 'test@gmail.com'
pass_email_from = '123456'
email_to = 'test_to@gmail.com'
email_server = 'smtp.gmail.com:587'

# Mapping Nova with Zabbix

mapping = {
    'compute1': 'compute1_zabbix',
    'compute2': 'compute2_zabbix',
    'ceph_hdd': 'volumes-hdd',
}
