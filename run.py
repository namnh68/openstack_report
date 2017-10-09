#!/usr/bin/env python
# -*- coding: utf-8 -*-

import optparse

from ops_report import config


def main():
    parser = optparse.OptionParser(usage="usage: %prog [options]",
                                   version="%prog 1.0")
    parser.add_option('-u', '--username', action='store', type='string',
                      dest='username', default=config.username,
                      metavar='USERNAME',
                      help='The name of users')
    parser.add_option('-p', '--password', action='store', type='string',
                      dest='password', default=config.password, metavar='PASSWORD',
                      help='The password of users')
    parser.add_option('-n', '--project_name', action='store', type='string',
                      dest='project_name', default=config.project_name,
                      metavar='PROJECT_NAME',
                      help='The project name of users')
    parser.add_option('-i', '--keystone', action='store', type='string',
                      dest='keystone_ip', default=config.ip_keystone,
                      metavar='KEYSTONE IP',
                      help='The IP of keystone')
    (options, args) = parser.parse_args()
    username = options.username
    password = options.password
    project_name = options.project_name
    keystone_ip = options.keystone_id
