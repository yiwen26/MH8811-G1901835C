#!/usr/bin/env python
# coding: utf-8

# In[4]:


import string
from genPassword import *
from random import *


# In[5]:


if __name__== '__main__' :        
    n=int(input('Which password length you want?'))
    password=genPassword(n)
    print(password)

