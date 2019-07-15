#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Default configurations.
'''

__author__ = 'Michael Liao'

configs = {
    'debug': True,
    'db': {
        'host': '47.105.172.225',
        'port': 3306,
        'user': 'root',
        'password': '123456',
        'db': 'awesome'
    },
    'session': {
        'secret': 'Awesome'
    }
}
