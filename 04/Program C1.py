#!/usr/bin/env python
# coding: utf-8

# In[1]:


smallest_so_far= None
for num in [9,14,12,3,74,15]:
    if smallest_so_far is None:
         smallest_so_far = num
    elif num < smallest_so_far:
         smallest_so_far = num
    print(smallest_so_far,num)
print ('After', smallest_so_far)

