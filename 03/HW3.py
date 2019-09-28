
# coding: utf-8

# In[7]:


#Function 1: Print "hello world !"
def p01():
    print('hello world!')
    return

#Function 2: Print "Hello + Username !"
def p02_1():
    username=input("Username: ")
    print("Hello, " + username +"!")
    return

#Function 3: Transfer temperature from Celsius to Fahrenheit
def p02_2():
    C=float(input("Temperature in Celsius: "))
    F = C * 1.8 + 32
    print ("The temperature in Fahrenheit is "+ str(F))
    return

def main():
    print("List of functions for you to choose: ")
    print("Function 1: Print hello world ")
    print("Function 2. Print Hello + your name ")
    print("Function 3. Transfer temperature from Celsius to Fahrenheit ")


while True:
    try: 
        main()
        n=int(input("Please choose the function No. you want: [The loop exits by pressing Enter]"))
        if n==1:
            p01()
        elif n==2:
            p02_1()
        elif n==3:
            p02_2()
    except:
        break

print("Thank you for using this Program！")


# ### What else can you make a function?
# 
# `lambda`: A lambda function is a small anonymous function. It can take any number of arguments, but can only have one expression. Using lambda simplifies the code, however this may reduce the legibility of the code.
# 
# #### For example:

# In[8]:


x = lambda a,b : a*b
print(x(5,6))

