#!/usr/bin/env python
# coding: utf-8

# In[3]:


#The function to compute the maximum of the data
def my_max(data):
    biggest_so_far = None
    for num in data:
        if biggest_so_far is None:
            biggest_so_far = num
        elif num > biggest_so_far:
            biggest_so_far = num
    return(biggest_so_far)

#The function to compute the average of the data
def my_ave(data):
    s=0
    for i in data:
        s = s + i
    return(round((s/len(data)),1))

#The function to compute the median of the data
def my_med(data):
    data.sort()
    r=int(len(data)/2)
    if len(data)% 2 != 0 :
        return (data[r])
    else:
        return ((data[r]+data[r-1])/2)

#The function to compute the minimum of the data
def my_min(data):
    smallest_so_far = None
    for num in data:
        if smallest_so_far is None:
            smallest_so_far = num
        elif num < smallest_so_far:
            smallest_so_far = num

    return(smallest_so_far)

#The function to compute the range of the data
def my_ran(data):
    a=-my_min(data) + my_max(data)
    return(a)

ls=[9,41,12,3,74,15]
print('The maximum of this list is ', my_max(ls))
print('The mininum of this list is ',my_min(ls))
print('The average of this list is ',my_ave(ls))
print('The median of this list is ',my_med(ls))
print('The range of this list is ',my_ran(ls))

