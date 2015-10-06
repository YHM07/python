#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

import pickle

account_info = {
        '1': ['Alex', '123', '150000', '150000', 'Normal'],
        '2': ['Tom',  '123', '10000', '10000', 'Normal'],
        '3': ['Jack', '123', '140000', '140000', 'Locked'],
        }

pkl_file = open('account.pkl', 'wb')
pickle.dump(account_info, pkl_file )

pkl_file.close()
