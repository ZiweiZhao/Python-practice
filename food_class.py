#!/usr/bin/env python3
#-*- coding: utf-8 -*-

class Food:
    def yummy(self):
        print ('Food is yummy!')

class Tuna(Food):
    def yummy(self):
        print ('Tuna is yummy!')

class Salmon(Food):
    def yummy(self):
        print ('Salmon is yummy!')

f = Food()
t = Tuna()
s = Salmon()

print ('Is f Food?', isinstance(f, Food))
print ('Is f Tuna?', isinstance(f, Tuna))
print ('Is f Salmon?', isinstance(f, Salmon))

print ('Is t Food?', isinstance(t, Food))
print ('Is t Tuna?', isinstance(t, Tuna))
print ('Is t Salmon?', isinstance(t, Salmon))

