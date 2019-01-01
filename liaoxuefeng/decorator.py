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

def decorator(aClass):
    class newClass:
        def __init__(self, age):
            self.total_display = 0
            self.wrapped       = aClass(age)
        def display(self):
            self.total_display += 1
            print('total display',self.total_display)
    return newClass

@decorator
class Bird:
    def __init__(self, age):
        self.age = age
    def display(self):
        print('my age is ', self.age)

eagleLord = Bird(5)
for i in range(3):
    eagleLord.display()
print(eagleLord.wrapped.age)
eagleLord.wrapped.display()
