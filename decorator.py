#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def identify_decorator(func):
    print('Enter identify_decorator',func.__name__)
    def wrapper():
        print('Enter wrapper',func.__name__)
        func()
        print('leave wrapper',func.__name__)
    print('leave identify_decorator',func.__name__)
    return wrapper

def aFunction():
    print('I am a normal function')

decotated_function = identify_decorator(aFunction)
print('decotated_function name: ',decotated_function.__name__)

print('Finished decotated_function')

decotated_function()
