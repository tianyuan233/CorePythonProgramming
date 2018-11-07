#!/usr/bin/env python
#-*- coding:utf-8 _*-
"""
@version:
@author: tianyuan233
@time: 2018/11/07
@file: 3.py

"""

a = 3

#共享引用，b成为对象3的一个引用
b = a

print(a)    #3
print(b)    #3

a = 'qqq'

print(a)    #qqq
print(b)    #3