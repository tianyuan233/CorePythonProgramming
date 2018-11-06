#!/usr/bin/env python
#-*- coding:utf-8 _*-
"""
@version:
@author: tianyuan233
@time: 2018/11/06
@file: slots.py
__slots__ 类属性 防止用户随心所欲的动态增加实例属性
"""
class SlotedClass():
    __slots__ = ('foo','bar')


c = SlotedClass()

c.foo = 42
print(c.foo)
#打印正常


c.xxx = 123
print(c.xxx)
#AttributeError: 'SlotedClass' object has no attribute 'xxx'