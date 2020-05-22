#!/usr/bin/env python
# Eucledian Vector and API to interact with it.
"""
+,*,abs
"""
import math
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)

    def __mul__(self, x):
        return Vector(x*self.x, x*self.y)
    
    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def __str__(self):
        return "Vector({}, {})".format(self.x, self.y)

    def __repr__(self):
        """String representation of Object. Convention, try to match to original source code.
           eval(repr(Object))=Object can be used in unit test. Is a fallback for str."""
        return "Vector({!r}, {!r})".format(self.x, self.y)

    def __bool__(self):
        """Override default behavior of User defined classes truthful."""
        return bool(abs(self))

v1 = Vector(3,4)
v2 = Vector(2,3)
print(v1+v2)
print(v1*10)
print(repr(v1))
print(abs(v1))
print(bool(v1))