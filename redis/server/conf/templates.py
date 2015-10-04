#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

from services import linux

class BaseTemplate(object):
    def __init__(self):
        self.name = 'your template name'
        self.hosts = []
        self.services = []

class LinuxGenericTemplate(BaseTemplate):
    def __init__(self):
        super(LinuxGenericTemplate, self).__init__()
        self.name = 'LinuxCommonServices'
        self.services = [
#                linux.CPU(),
                linux.Memory(),
                ]
#        self.services[0].interval = 90

class LinuxTemplate(BaseTemplate):
    def __init__(self):
        super(LinuxTemplate, self).__init__()
        self.name = 'LinuxServices'
        self.services = [
#                linux.CPU(),
                linux.Network(),
                ]
