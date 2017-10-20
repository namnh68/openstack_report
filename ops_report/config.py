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
zabbix_ip = '172.16.69.45'
zabbix_port = '80'

# For Ceph
ceph_ip = '172.16.69.167'
ceph_port = '5000'

# For sending emails
email_from = 'mycloudvnn@vdc.com.vn'
pass_email_from = 'Vdc1T@!ma1l'
email_to = 'zabbix.vdcit@gmail.com'
email_server = 'smtp1.vdc.com.vn:25'

# Mapping Nova with Zabbix

mapping = {
    'compute1.hn.vnpt': 'com1_hn',
    'compute2.hn.vnpt': 'com2_hn',
    'ceph_hdd': 'volumes-hdd',
}
