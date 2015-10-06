#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

import pickle

pkl_file = open('account.pkl', 'rb')

account_info = pickle.load(pkl_file)

print(account_info)

pkl_file.close()


