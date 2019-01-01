#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def makeHtmlTag(tag,*args,**kw):
    print('Enter the makeHtmlTag',tag,args,kw)
    def real_decorator(fn):
        print('Enter the real_decorator',tag,args,kw,fn.__name__)
        css_class = "class = '{0}'".format(kw["css_class"]) \
                if "css_class" in kw else ""
        def wrapped(*args, **kw):
            print('Enter the wrapped',tag,args,kw,fn.__name__)
            return "<"+tag+' '+css_class+">" + fn(*args,**kw) + "</"+tag+">"
        print('leave the real_decorator',tag,args,kw,fn.__name__)
        return wrapped

    print('leave the makeHtmlTag',tag,args,kw)
    return real_decorator

@makeHtmlTag(tag='b',css_class='bold_css')
@makeHtmlTag(tag='i',css_class='italic_css')
def hello():
    return "hello world"

print(hello())


class myDocorator(object):

    def __init__(self, fn):
        print('inside myDocorator.__init__()')
        self.fn = fn

    def __call__(self):
        self.fn()
        print('inside myDocorator.__call__()')

@myDocorator
def aFunction():
    print('inside decorating aFunction')

print('Finished decorating aFunction')

aFunction()
