#!/usr/bin/python
#-*- coding: utf-8 -*-

class Food(object):
    __slots__ = ('name', 'flavor') #use a tuple to display all the changeable attributes name

class Tuna (Food):
    pass

f = Food()
f.name = 'salmon'
f.flavor = 'ocean'

try:
    f.like = 'yummy'
except AttributeError as e:
    print('Error: ', e)

t = Tuna()
t.like = 'yummy?'
print('t.like = ', t.like)

