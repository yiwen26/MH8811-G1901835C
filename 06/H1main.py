#!/usr/bin/env python
# coding: utf-8

# In[4]:



from genPassword import *


n=int(input('Which password length you want?'))
if n < 4:
    print('password length should be more than 4 !')
else:
    password=genPassword(n)
    print("the password generated is " + password)


