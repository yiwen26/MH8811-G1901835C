#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import string
from random import *

#global a, b, c, d
a = string.ascii_lowercase
b = string.ascii_uppercase
c = string.digits
d = string.punctuation

def genPassword(n):
    a1=randint(1,n-3)
    b1=randint(1,n-2-a1)
    c1=randint(1,n-1-a1-b1)
    d1=n-a1-b1-c1
    a2=sample(a,a1)
    b2=sample(b,b1)
    c2=sample(c,c1)
    d2=sample(d,d1)
    p=a2+b2+c2+d2
    shuffle(p)
    return(''.join(p))

if __name__ == '__main__':
    print(genPassword(12))

