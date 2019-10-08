#!/usr/bin/env python
# coding: utf-8

# In[34]:


file_path = 'C:/Users/wyw/Desktop/python programming/MH8811-04-Data.csv'

#The function to read the data file
def getFileLines(fname):
    fhandle = open(fname)
    lines = []
    for line in fhandle :
        line = line.rstrip()
        if line :
            lines.append(line)
    return lines


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
    return(s/(len(data)))

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

#The function to compute the sample variance of the data
def my_vari(data):
    s1=0
    s2=0
    n=len(data)
    for i in data:
        s1+=i
        s2+=i**2
    v=(s2-s1**2/n)/(n-1)
    return(round(v,1))

ls = list(getFileLines(file_path))
for i in range(len(ls)):
    ls[i]=int(ls[i])
print('The maximum of this dataset is ', my_max(ls))
print('The mininum of this dataset is ',my_min(ls))
print('The average of this dataset is ',my_ave(ls))
print('The median of this dataset is ',my_med(ls))
print('The range of this data is ',my_ran(ls))
print('The sample variance of this dataset is ',my_vari(ls))

