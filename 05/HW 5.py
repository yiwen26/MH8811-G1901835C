#!/usr/bin/env python
# coding: utf-8

# In[16]:


import json


# In[17]:


def open_json_file():
    filename=input('what is the file name you want to open ? ')
    fh=open(filename)
    data=json.load(fh)
    fh.close()
    print(data)
    return(data)
    


# In[18]:


def save_to_file(contents):
    filename=input('what is the file name you want to save ? ')
    fh = open(filename, 'w')
    fh.write(contents)
    fh.close() 
    return(filename)


# In[19]:


def get_file_str():
    filename=input('what was the file name you just saved ? ')
    fhandle = open(filename)
    lines = ''
    for line in fhandle :
        line = line.rstrip()
        if line :
            lines=lines+line
    fhandle.close()
    return lines


# In[20]:


def serialize(data):
    res=''
    t=type(data).__name__
    dtype={'list':'1','dict':'2', 'float':'3', 'int':'4', 'str':'5'}
    if dtype[t] == '1':
        for i in data:
            res = res + str(i) + dtype[type(i).__name__] + '|'
    if dtype[t] == '2':
        for key in data:
            res=res+ key + ',' + str(data[key]) + dtype[type(data[key]).__name__] + '|'
    res=res+':'+dtype[t]
    print(res)
    return(res)


# In[21]:


def deserialize(data):
    dtype={ '3':'float', '4':'int', '5':'str'}
    t=data.split(':')[1]
    ls_str=(data.split(':')[0]).split('|')[:-1]
    if t=='1':
        ls=[]
        for i in ls_str:
            if i[-1]!='5':
                s=eval(dtype[i[-1]] + '(' + i[:-1] + ')')
            else:
                s=i[:-1]
            ls.append(s)
        return(ls)
    if t=='2':
        d={}
        for i in ls_str:
            a,b=i.split(',')[0],i.split(',')[1]
            if i[-1]!='5':
                d[a]=eval(dtype[b[-1]]+ '(' + b[:-1] + ')')
            else:
                d[a]=b[:-1]
        return(d)


# In[22]:


def my_compare(data1,data2):
    if data1 == data2:
        print('Success!')
    else:
        print('Failed!')


# In[15]:


data=open_json_file()
data_str=serialize(data)
filename=save_to_file(data_str)
read_data_str=get_file_str()
des_data=deserialize(read_data_str)
print(des_data)
my_compare(data,des_data)

