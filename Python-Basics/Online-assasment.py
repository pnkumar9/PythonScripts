#!/usr/bin/python

def foo(x):
    x[0] = ['def']
    x[1] = ['abc']
    return id(x)
q = ['abc', 'def']
print(id(q) == foo(q))

z=set('abc')
z.add('san')

print (z)