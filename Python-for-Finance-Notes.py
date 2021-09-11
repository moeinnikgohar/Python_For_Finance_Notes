#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#####################Section 3: Python variables and data types#############################


# In[ ]:


#Variables


# In[4]:


x = 2
print (x)


# In[89]:


x,y=(1,2)


# In[91]:


x


# In[92]:


y


# In[42]:


print (1,2)


# In[43]:


print (x,y) #y has changed from 2 to 64 because further down i have assigned a new value to y


# In[ ]:


#Numbers:
#2 types of numbers in python: integers - whole numbers, floats - decimals.
#we can determine the type of variable by writing:
#the result will tell us the type of variable x1 is, it can also tell us the type of value


# In[3]:


x1=5
type(x1)


# In[2]:


type(5)


# In[5]:


x2=4.75
type(x2)


# In[6]:


int(x2) #this will transform the float variable into an integer


# In[7]:


float(x1) #this will transform the integer into a float by adding  a decimal


# In[ ]:


#Boolean values are not numeric, in python they are 'True' and 'False', in capital letters


# In[8]:


x3=True
type(x3)


# In[ ]:


#Strings are text values composed of a sequence of characters


# In[9]:


'George'


# In[10]:


"George"


# In[12]:


print('George')


# In[13]:


print ("George")


# In[2]:


x4="George"


# In[3]:


x4


# In[4]:


type(x4)


# In[16]:


y=10
print (y + " Dollars")


# In[ ]:


#This happens because we cannot put Integer and Strings in the same expression, so we have to convert y into a string


# In[17]:


print (str(y)+" Dollars") 


# In[ ]:


#how to use apostrophe


# In[47]:


'I\'m Fine'


# In[48]:


"I'm a Rocket Scientist"


# In[ ]:


#how to use quotation marks


# In[18]:


'Press "Enter"'


# In[5]:


print ('Press "Enter"')


# In[ ]:


#How to add space to sentences


# In[49]:


'red''car'


# In[50]:


'red ''car'


# In[21]:


'red '+'car'


# In[54]:


print('red', 'car')


# In[56]:


3, 5, 6, 7.2, 8.0, 'car'


# In[ ]:


###############################Section 4: Arithmetic Operators###########################################
# the following signs: +-=/ are called operators, whilst the numbers in the operations are called operands


# In[29]:


1+2


# In[30]:


3-5


# In[25]:


15/3


# In[26]:


16/3 #we could also use float(16)/3 or 16.0/3


# In[27]:


#the % sign is used to obtain the remainder from a division
16 % 3 #should give us a remainder of 1


# In[28]:


5*3


# In[35]:


x5=4*3


# In[34]:


x5


# In[62]:


5**3


# In[36]:


y=4**3


# In[37]:


y


# In[38]:


y==64 #the double equality (==) means: is y really equal to 64?


# In[39]:


y==65


# In[41]:


print (7,2)


# In[44]:


#Line Continuation: we use \ to show end of 1 line and continuation of calculation in the next line
2*5 + 3 + 5


# In[45]:


#Indexing allows us to identify letters in a string
"Friday"[3] #in python we count from 0, so the 4th letter would be the 3rd index


# In[12]:


#Indentation: helps us to structure our code
#lets define a function "five" that takes as an argument an unknown x(any number):
def five(x):
    x=5 #x re-assigned a value of 5 #indent=the space created at start of the line
    return x
#we need to create a space of line between print and def function since they are 2 different functions, otherwise we get error

print(five(3)) #new line started with no indentation
#we will still get 5 because we have assigned a value of 5 to x, if we remove this we get 3


# In[14]:


def five(x):
    return x
print(five(2)) #this should now give us 2


# In[ ]:


#########################Section 5: Comparison Operators#######################################


# In[54]:


10==20/2 #is 10 equal to 20/2?


# In[61]:


10!=10 #means 10 is "not equal to(!=)" 10, which is False


# In[56]:


10!=15 #means 10 is not equal to 15, which is True


# In[57]:


100>50 #means: is 100 greater than 50? True


# In[58]:


100<50 #means: is 100 less than 30? False


# In[59]:


15<=15


# In[60]:


15>=10+6


# In[62]:


#Logical Operators (a.k.a Boolean Operators): NOT, AND, OR
#AND checks whether the 2 statements are True
#OR checks at least one of the statements is True
#NOT leads to the opposite of the given statement
#"OR" operator needs one True to give True
#"AND" operator needs 2 Trues to give True, otherwise it gives False


# In[67]:


True and True


# In[64]:


True and False


# In[68]:


True or False


# In[69]:


False or False


# In[70]:


not True


# In[71]:


not False


# In[73]:


3>5 and 10<=20 #the first statement is False, but the second one is true, however False and True entails False


# In[74]:


#The order of Logical Operators is: NOT, AND, OR


# In[75]:


True and not True #this is True and False, which results in False


# In[77]:


False or not True and True #this gives False or False and True, which gives False or False, which gives False


# In[78]:


True and not True or True #gives True and False or True, gives False or True, "OR" operator needs one True to give True
#but AND needs 2 Trues to give True, otherwise it gives False


# In[84]:


#Identity Operators: is(==), is not(!=)


# In[85]:


5 is 6


# In[86]:


5 is not 6


# In[87]:


######################Section 6: Conditional Statements################


# In[88]:


#IF statment: 


# In[90]:


if 5==15/3:
    print ("Hooray")
    
#we use == because = is used for variable name, i.e. x=5. colon is used to tell the computer what to do when "if" is satisfied
#also make sure the print is indented (the colon(:) indents the line)
#don't forget quotation marks around the printing message


# In[91]:


if 5==18/3:
    print ("Hooray")


# In[92]:


#we get nothing becuase we have not told the machine what to do when the IF statement is not satisfied


# In[95]:


if 5!=18/3:
    print ("Hooray")


# In[102]:


x=1

if x>3:
    print ("Case1")
if x<=3:
    print ("Case2")


# In[104]:


#Using the "ELSE" function: it is used for all other cases and requires colon after it (else:) 


# In[103]:


x=1

if x>3:
    print ("Case1")    
else:
    print ("Case3")


# In[105]:


#ELSE IF (ELIF), order of priority is: IF, ELIF, ELSE


# In[117]:


def compare_to_five(y):
    if y>5:
        return "Greater"
    elif y<0:
        return "Negative"   
    elif y<5:
        return "Less"
    else:
        return "Equal"
#when you add a new elif to the above code, you must shift+enter the cell for it to take effect
#when you have 2 elif functions that are less than 5, it is important to write the smaller one (<0) first


# In[118]:


print (compare_to_five(10))


# In[119]:


print (compare_to_five(2))


# In[120]:


print (compare_to_five(5))


# In[121]:


print (compare_to_five(-2))


# In[122]:


x=2

if x>4:
    print ("Correct")
else:
    print ("Incorrect")


# In[123]:


#########Section 7: Python Functions###############


# In[129]:


#to write a function we always start with "def" and then we write the function name:
# def function_name (parameters of the function): and don't forget the colon to make sure we have an indent for the next line
#to apply a function we must call it! e.g we need to write the function name with any parameters required, as per def


# In[130]:


def simple():
    print ("my first function") #we use print because there are no values in the parameter to be returned


# In[131]:


simple() 


# In[132]:


def plus_ten(a): #naming your function makes the code more readable by the audience, e.g. x1 is confusing, plus_ten is better
    return a+10 #this is the function body, or the connection between input and output
#remember: return can only be used once in a function


# In[133]:


plus_ten(2)


# In[134]:


#Creating a function with a parameter
def plus_ten(a):
    result = a+10
    return result


# In[136]:


plus_ten(3)


# In[138]:


#Print does not affect calculation of the output
#return does not visualise the output, it specifies what a certain function is supposed to give back
#we can return only a single result out of a function
def plus_ten(a):
    result = a+10
    print ("Outcome:")
    return result


# In[139]:


plus_ten(4)


# In[1]:


def minus_two(b):
    result = b - 2
    print("outcome:")
    return result


# In[2]:


minus_two(13)


# In[140]:


#Function within a Function


# In[146]:


def wage(working_hours):
    return working_hours*25 #so the hourly rate is 25 dollars per hour

def with_bonus(working_hours):
    return wage(working_hours)+50 #a 50 dollars bonus is also added


# In[149]:


wage(10)


# In[148]:


with_bonus(10)


# In[147]:


wage(8), with_bonus(8)


# In[14]:


def salary(years_worked):
    return years_worked*100000

def salary_with_bonus(years_worked):
    return salary(years_worked)+(years_worked * 50000)


# In[15]:


salary(3)


# In[16]:


salary_with_bonus(3)


# In[150]:


#Combining conditional statements (IF) and Functions


# In[151]:


def add_10(m):
    if m>=100:
        m=m+10
        return m
    else:
        return "save more!"


# In[152]:


add_10(110)


# In[153]:


add_10(90)


# In[154]:


#creating functions containing a few arguments: functions with more than 1 parameter


# In[17]:


def subtract_bc(a,b,c): #all 3 parameters included in 1 function separated by comma. Parameter is variable in the /
    #declaration of function
    result=a-b*c
    print ('parameter a equals', a)
    print ('parameter b equals', b)
    print ('parameter c equals', c) 
    return result


# In[19]:


subtract_bc(10,3,2) #if you state parameters like this, then order matters


# In[157]:


subtract_bc(b=3,c=2,a=10) #if you state parameters like this, then order won't matter


# In[158]:


#Built-in Function in Python - they can be applied directly
#examples include: type(), int(), float(), str()


# In[159]:


max(10,20,30)


# In[160]:


min(2,4,8)


# In[161]:


z=-20
abs(z) #allows us to obtain the "absolute value of an argument"


# In[166]:


list_1=[1,2,3,4]
sum(list_1) #calculates the sum of all elements in a list designated as an argument


# In[167]:


round(3.555,2) #this will round 3.555 to 2 decimal places


# In[177]:


round(3.92) #however if the number of decimal places is not indicated, it rounds to nearest whole number


# In[179]:


round(3.92,0) #put 0 decimal places if you want the whole number to be returned as a float


# In[180]:


2**10


# In[181]:


pow(2,10) #the above calculation for power can also be calculated using the pow() function


# In[182]:


len('mathematics') #returns the number of elements(letters) in an object(word) 


# In[183]:


########Section 8: Python Sequences##############


# In[21]:


# List = is a sequence of data points
participants = ['zlatan', 'cristiano', 'leo', 'zizou'] #the object in this list is the "participants"


# In[22]:


participants


# In[23]:


print (participants[2]) #we have accessed the list by indexing value 2, which is the 3rd element of this list, leo


# In[24]:


print (participants[1])


# In[25]:


#now what if you have a really long list and want to find the last item on the list?
#you need to index -1 to access the last point
print(participants[-1])


# In[26]:


#if you index -2, we get the second to last item on the list
print(participants[-2])


# In[27]:


#replacing items in a list
participants[3]='rooney'


# In[28]:


participants


# In[29]:


#deleting items in a list
del participants[2]


# In[30]:


participants


# In[31]:


#adding a new name to the list: this can be achieved using the .append() method - dot before append is called the dot operator
#the dot operator calls/invokes a certain method: object.method("new term"), new term being added to the list must be in ""
participants.append("tevez")


# In[32]:


participants


# In[33]:


#to add more than one name to the list, we use the extend() method, and use [] + '' + ,
participants.extend(['berba', 'benzema'])


# In[34]:


participants


# In[35]:


print ('The first participant is '+participants[0]+'.')


# In[231]:


# we can find the number of elements in a list using the len() function, should return 7 elements since we have 7 names
len(participants) #the built-in function len() has taken the object "participant" as an "argument"


# In[232]:


len('participants') #remember the difference between the word participant and the object participant!


# In[233]:


#list slicing: allows us to only select the elements we want in a list
#for example if we want to slice the list to man utd players under ferguson only, we slice from element 1(ronaldo) up to 5
#we chose 5 to tell python that we need to slice it to just up to 5
participants[1:5]


# In[235]:


#if we wanted to just slice the list to the first 3 participants, we do the following:
participants[:3] #we selected up to the first 4 elements: 0,1,2,3


# In[236]:


#if we wanted the last 2 names on this list we do the following:
participants[4:]


# In[237]:


#or we could use this method:
participants[-2:]


# In[238]:


#we can find the position of elements in our list by indexing them:
participants.index("tevez")


# In[239]:


participants.index("zlatan")


# In[240]:


#Creating Lists of Lists:


# In[241]:


newcomers=['Daniel James','Wan-Bissaka']
newcomers


# In[242]:


bigger_list=[participants, newcomers]
bigger_list


# In[243]:


#we can use the sort method to order our list in alphabetical order:
participants.sort()
participants


# In[245]:


#we could also reverse this order:
participants.sort(reverse=True)
participants


# In[246]:


#we can sort numbers too:
numbers=[1,2,3,4,5]


# In[249]:


numbers.sort()
numbers


# In[250]:


numbers.sort(reverse=True)
numbers


# In[251]:


#Tuples: a type of data sequences, they are immutable(cannot be changed or modified), so you cannot append or delete elements
#Tuples elements are placed within parenthesis, NOT brackets
x=(40,41,42)
x


# In[252]:


y=50,51,52 #python will automatically place these in parenthesis
y


# In[255]:


#Tuple assignement
a,b,c=1,2,3
c


# In[257]:


x[1] #we can index position of elements in tuples too


# In[258]:


#we can also place tuples within a list, each tuple becomes a separate element within the list
list=[x,y]
list


# In[261]:


#Tuples are useful with comma_separated_values:
(age, years_of_school)="30,17".split(',') #age and years of school are variables. split method separates the values 30 and 17
print (age)
print (years_of_school)


# In[262]:


#Functions can provide Tuples as return values
#Function itself can only provide a single return value, but with Tuples it can return a Tuple holding multiple values:


# In[266]:


def square_info(x):
    A=x**2
    P=4*x
    print("Area and Perimeter:")
    return A,P

square_info(3)


# In[267]:


#Dictionaries: they represent another way of storing data
#in a dictionary each value is associated with a certain key, forming a key-value pair, placed in curly braces{}
dict={'k1':'cat','k2':'dog','k3':'mouse','k4':'fish'}
dict


# In[268]:


dict['k2']


# In[269]:


#adding a new value to the dictionary
dict['k5']='parrot'
dict


# In[270]:


#replacing a value in a dictionary
dict['k2']='squirrel'
dict


# In[284]:


#example:
department_workers={'dep_1':'peter', 'dep_2':['ali','hasan','hosein']}


# In[285]:


department_workers['dep_2']


# In[286]:


#another way of creating a dictionary:
team={}
team['defence']='de ligt'
team['midfield']='pogba'
team['striker']='ronaldo'


# In[287]:


print (team)


# In[288]:


print (team['midfield'])


# In[289]:


print(team.get('striker'))


# In[291]:


print(team.get('coach')) #we got none because coach does not exist in this dictionary


# In[294]:


#we could use dictionaries for companies and their prices on the market:
IBD={"JPmorgan":50,"goldman":60,"citi":40}
print (IBD)


# In[295]:


print (IBD['goldman'])


# In[1]:


#######Section 9: Using iterations in Python#############
#iteration is the ability to execute a code repeatedly


# In[3]:


#For Loops
even=[0,2,4,6,8,10,12,14,16,18,20]


# In[14]:


for n in even: #for every element n in the list even
    print (n) #where n is the loop variable #the phrase "print (n)" acts as the body of our loop


# In[24]:


#we can get the list in straight line by using comma in print:
for n in even:
    print (n, end=" ") #notice the space between " "


# In[29]:


#While loops and incrementing
x=0
while x<=10:
    print(x, end=" ") #don't end the code here, the loop will be infinite and the computer will crash
    x=x+1 #This is called incrementing: this will stop the loop from being infinite, an increment of 1


# In[33]:


#we could also do this:
x=0
while x<=10:
    print(x, end=" ")
    x+=2 #using += is the same as x=x+2


# In[55]:


#Create lists with the range() function
#range(start, stop, steps) creates a list of numbers. order of priority(stop,start,step)
#start = first number on the list: if not provided it will automatically be 0
#stop = last value + 1: this is mandatory, whilst start and step values are optional.
#step = the distance between each 2 consecutive values: if not provided it will automatically be 1
[*range(10)] #here python assumes 0 as starting value with steps of 1, and 10 is the stop value


# In[59]:


[*range(0,10,2)]


# In[60]:


[*range(3,7)] #here python selects 3 as starting value and 7 as stopping value, it also assumes steps of 1


# In[61]:


#Using conditional statements and loops together
#to get (2**0), (2**1),,,,,(2**9) we use the following code:
for n in [*range(10)]:
    print (2**n, end=" ")


# In[64]:


#combination of an iteration and conditional in python
for x in range(20):
    if x%2==0: #if x divided by 2 leaves a remainder of zero, meaning if x is even
        print (x, end=" ")
    else:
        print ("odd", end=" ")


# In[65]:


#2 main ways to program a loop
x=[0,1,2]


# In[66]:


#first way:
for item in x:
    print (item, end=" ")


# In[11]:


#second way:
x=[0,1,2]
for item in range(len(x)): #For each item in a range that goes through elements from the list x that is lined with an argument
    print (x[item], end=" ") #this will loop for len(x)=3: range(3)=range(0,3,1)=[0,1,2]


# In[39]:


#conditional statements, functions and loops
def count(numbers): #we are using a count function to count the number of items whose value is less than 20
    total=0 #this variable is a rolling sum, because it changes once we verify the conditions
    for x in numbers:
        if x<20:
            total+=1 #if x is smaller than 20, we will increment the total(which zero at the moment) by 1
    return total


# In[40]:


list_1=[1,3,7,15,23,43,56,98]


# In[41]:


count(list_1)


# In[37]:


#iterating over dictionaries

prices = {
    "burger":4,
    "coke":1,
}
quantity = {
    "burger":3,
    "coke":1,
}
#to find out how much money is spent, we need a loop:

money_spent = 0 #this is a rolling sum again

for i in prices: #we can either loop for prices or through quantity, because both contain same keys, both will get the answer
    money_spent=money_spent+(prices[i]*quantity[i])
    
print (money_spent)


# In[1]:


#####Section 10: Advanced Python Tools#######


#                                           #####Object Oriented Programming######
# #Object oriented programming is a stepping stone for explaining modules
# #every value in python is an object: integers, floats, lists, strings... these are all logical objects
# #object oriented programming is about interacting with one or more objects
# #objects allow us to model real world concepts
# #object = data + manipulation operations 
# #each object belongs to some class, and the class defines the rules for creating that object
# #we can attach a certain number of attributes (e.g type of data: float, integer and etc) to the object
# #Method is a consequential logic sequence that can be applied to the object. e.g indexing a float
# #object can also be called instance
# #attributes can also be called properties
# #Function() vs Object.Method(): a function can have many parameters, but in a method the object is one of its parameters
# #method belongs to a certain class, whilst a function exists on its own

#                                            #####Modules and Packages#######
# #A module is a pre-written code containing definitions of variables, functions and classes. it can be loaded in all new programs
# #also, we need not rewrite the code manually at the beginning of a new program.
# #A package is a collection or directory of related python modules.
# #Technically you could create your own modules and packages.
# #But people in the programming community have developed a growing set of packages that are readily available for download \ 
# #which have been tailored for various types of professions and specializations.
# #packages are also known as libraries, so the 2 terms are used interchangeably 

#                                     ###python's standard library#######
# #python's standard library is a collection of modules available as soon as you install python
# #for example the len() function or list() class 
# #people don't need to install all the modules there are, they install the modules and packages they need for their profession
# #it is mostly the developers job to create modules, and you can download and import the module
# #once the module has been released, you can update it and improve it. modules can be re-used multiple times
# #modules improve python's efficiency.

# In[4]:


#Importing Modules: 
#e.g. importing a math module with sqrt() function - this is not part of python standard library (but is part of anaconda)
#There are 4 ways to import a module:


# In[5]:


#Method 1:
import math


# In[6]:


math.sqrt(16)


# In[7]:


#Method 2:
from math import sqrt


# In[8]:


sqrt(25)


# In[9]:


#Method 3:
from math import sqrt as s


# In[10]:


s(36)


# In[13]:


import math as m


# In[14]:


m.sqrt(49)


# In[15]:


#Method 4: 
from math import * #all the features from math functions classes or methods will be imported


# In[16]:


sqrt(64)


# In[17]:


#the fourth method is usually frowned upon since it could result in duplication of functions if you are importing more than \
#one module in the same code file. avoid this method if you can.


# In[19]:


#you can get more information about a module by doing the following:
help(math) #this will give you the description of all the functions within a module


# In[20]:


#you can also get description for a single function in a module:
help(math.sqrt)


# In[1]:


#Must-have packages(Libraries) for Finance and Data Science


# In[5]:


import numpy #a 3rd party package that allows us to work with multidimensional arrays
#arrays represent a powerful way to organise and process data, hence it is good for large data sets
#NumPy is good for producing numerical results. it is a package that contains scientific computing tools


# In[6]:


import pandas #this is a package that enhances numpy even further
#pandas allows us to organise data in a tabular form and to attach descriptive labels to the rows and columns of the table
#pandas is suitable for working with time series and huge databases 
#pandas is the main data analysis tool in python. it stands for PANel DAta, which multidimensional datasets


# In[7]:


import matplotlib #a 2D plotting library especially designed for visualisation of NumPy computations


# In[8]:


#NumPy, Pandas and matplotlib are all part of a larger group of "Scipy" libraries
#Scipy is a python ecosystem, containing a a lot of tools for scientific calculations suitable for the fields of mathematics,
#Machine learning, artificial intelligence, engineering and more.


# In[11]:


#We need the following 3 modules:
import math #mathematical functions
import random #invokes random number generators
import statsmodels #descriptive statistics, plotting functions, regressions


# In[9]:


#all the 3 libraries and 3 modules imported so far were not part of the python standard library, but they were included in the /
#anaconda package


# In[12]:


#how to install packages/modules you don't have:


# In[13]:


import panda_datareader


# In[14]:


#this package is not part standard library or anaconda package, so must be installed by other means:


# In[15]:


#go to your pc start menu, type anaconda prompt, type: pip install pandas-datareader, then press enter. might take a minute.
#pip means, pip installs packages, or pip installs python


# In[18]:


import pandas_datareader #now the module has been imported successfully


# In[19]:


#Arrays: difference between arrays and list is that all the elements in array must be of the same data type (integer & etc)


# In[20]:


import numpy as np


# In[22]:


a = np.array([[0,1,2,3],[4,5,6,7]]) #assigned a NumPy array to the variable "a"
a


# In[23]:


#NumPy n-dimensional array = ndarray. 
#An ndarray is always homogenous (all blocks should be of the same data type, and same number of elements)
b=np.array([[0,"thomas",2,3],[4,5,6,7]])
b


# In[24]:


c=np.array([[0,2,3],[4,5,6,7]])
c


# In[25]:


#array(), returns a data structure in the NumPy array format
#we can see the shape of an array by typing the following:
a.shape #shape of array "a": should indicate that the object has 2 rows and 4 columns


# In[26]:


#we can also acces the values in an array:
a[1,3] #number of row,number of column. remember, we start counting from zero, hence 1 indicates second row


# In[31]:


#we can also change the value in an array:
a[1,2]=8 #we are changing 6 to 8
a


# In[33]:


#we can also extract a whole row:
a[0] #extracting the first row


# In[47]:


#arrays are important in finance because array is the data structure that will carry into organized values into /
#vectors, matrices and other multi-dimensional objects.
#A vector is an object that has both a magnitude and direction:


# In[1]:


import numpy as ny


# In[2]:


d=ny.array([3,5]) #elements 3 and 5 represent x and y on a graph respectively 
d


# In[4]:


import numpy as np


# In[5]:


e=np.array([3,5])
e


# In[6]:


#1D array = vector
#2D array = matrix. the numpy array allows us to create matrix


# In[7]:


#Generating Random Numbers
import random


# In[8]:


#the random function random() will generate a random float in the range from 0 to 1 [0;1], 0 included and 1 excluded!
#also remember that the probability is from 0 to 1
prob=random.random()
print (prob)


# In[12]:


#random.randint() - randomises over a provided interval and delivers and integer value. e.g. throwing a dice, integers 1 to 6:
number=random.randint(1,6)
print (number)


# In[15]:


#now let's create a matrix using NumPy arrays
import numpy as np


# In[23]:


np.random.randint(1,6,(4,6)) #the (4,6) means it's a 4 x 6 matrix, and the 1,6 means values are going to be from 1 to 5
#this is very useful in Monte Carlo Simulations


# In[24]:


#importing real-life data in python requires you to find the source
#sources of financial data: computer or web server
#to get data from the web server you need its API (application programming interface) /
#we call them financial data APIs (online financial data sources), there are examples of these:
#Financial Data APIs= iex, morningstar, alpha vantage, Quandl. all provide up to date data
#panda's data reader is an example of a module that will help you retrieve data /
#from the financial data sources and prepare them for analysis
#we can also use files from computer for financial data in the *.csv (comma-separated value) format
#advantage of *.csv is that it is rich data and easy to handle. disadvantage is: it's not up to date

#financial data APIs:
#advatange: up to date data
#disadvantage: prone to breaking down for unknown periods of time.
#also a certain API  may only have part of the data required for proper financial analysis 
#Currently some API is offer just single or multiple stock data while others may provide /
#foreign stock data or market indices data.
#Yahoo API is the only API that is compatible with all versions of python. 
#for this course we will be using the Yahoo Finance API (the data source in our code)
#Yahoo API is better than google, google does not provide foreign stock and market indices data
#if Yahoo finance API is not available, then use morningstar or alpha vantage APIs. iex (python3).
#to do this you need to add the iex API to the python termina. open terminal, type pip install iex-api-python, Enter

#both APIs and *.csv can be found in the resource section of the lectures in this course.
#filenames with csv in the end (in resources of this course) are from Yahoo, and are the best for this course


# In[1]:


#Importing and organising data in python Part 1:
import numpy as np
import pandas as pd


# In[2]:


ser=pd.Series(np.random.random(5), name="Column 1") #one of the 2 main data types in pandas is series (single column of data)
#the 5 indicates 5 random numbers in this single column of data


# In[3]:


ser #You can think of a series object as a dictionary whose items are of the same data type.


# In[5]:


ser[2] #this will access the 3rd element of the list through its index


# In[7]:


#the second data type in pandas is called DataFrame, this is similar to series, but it has many columns of data
from pandas_datareader import data as wb #wb stands for web


# In[8]:


#now we are going to extract data from Yahoo Finance about "Procter & Gamble":
PG=wb.DataReader('PG', data_source='yahoo', start='1995-1-1')
#PG is the procter & gamble's ticker. ticker is the symbol with which a company's shares are quoted on the stock exchange.
#for example apple's ticker is AAPL, microsoft's ticker is MSFT
#When extracting financial data, we need the ticker, data source and start date


# In[9]:


PG 


# In[10]:


#importing and organising data in python part 2A:
#always important to check your data once it is imported. 
#the weekends and public holidays will not be shown, because we only have data for trading days.
#the first row(0) is the row with the first date and data in it
#the closing price and the adjusted closing price seem far apart in 1995, but they reach the same value in 2019 /
#the difference is due to dividends paid to stock owners and to other changes to the stock price such as / 
#stock splits increases of capital and so on.


# In[11]:


PG.info() #this tells we are dealing with a DataFrame object with 6 columns, extracted from yahoo
#the number of entries in each column in 6181, hence the data is accurate
#also all data are float, sometimes the volume could be expressed as integer


# In[12]:


PG.head() #shows us the first 5 rows of our data


# In[14]:


PG.head(3) #we can adjust this to show less or more data


# In[15]:


PG.tail() #this will show us the last 5 rows of our data


# In[16]:


PG.tail(2) #we can adjust this to show less or more data


# In[22]:


#now we are going to create a dataset with 5 columns representing adjusted closing price for stocks of 5 different companies:
#the companies are: Procter & Gamble, Microsoft, AT&T, Ford and General Electric
tickers = ['PG', 'MSFT', 'T', 'F', 'GE']
new_data = pd.DataFrame() #we will create a new data frame object from pandas and we'll call it new data.
for t in tickers:
    new_data[t] = wb.DataReader(t, data_source='yahoo', start='1995-1-1')['Adj Close']
#For every ticker in tickers (t in tickers) provide me with the adjusted closing price for each ticker for each instance.
#This trick will work only if the data for all five companies is organized in the same way with the same column names.
#This is a form of iteration, which is much faster than filling in data row by row


# In[24]:


new_data.tail() #this is done to check that the new data for the 5 tickers has been retrieved correctly


# In[ ]:


#importing and organising data in python part 2B: (lecture 56)
#remember to pip install iex before starting this lecture
#########################IEX API IS CURRENTLY DOWN, SO WE HAVE TO COME BACK TO THIS LECTURE#########################
#########################IEX API IS CURRENTLY DOWN, SO WE HAVE TO COME BACK TO THIS LECTURE#########################
#########################IEX API IS CURRENTLY DOWN, SO WE HAVE TO COME BACK TO THIS LECTURE#########################
#########################IEX API IS CURRENTLY DOWN, SO WE HAVE TO COME BACK TO THIS LECTURE#########################
#########################IEX API IS CURRENTLY DOWN, SO WE HAVE TO COME BACK TO THIS LECTURE#########################
#########################IEX API IS CURRENTLY DOWN, SO WE HAVE TO COME BACK TO THIS LECTURE#########################
#########################IEX API IS CURRENTLY DOWN, SO WE HAVE TO COME BACK TO THIS LECTURE#########################


# In[29]:


import numpy as np
import pandas as pd


# In[30]:


import pandas_datareader


# In[31]:


from pandas_datareader import data as wb


# In[4]:


import iex


# In[ ]:


PG=wb.DataReader('PG', data_source='iex', start='2017-1-1') #IEX can only retrieve data for the last 5 years


# In[ ]:


#########################IEX API IS CURRENTLY DOWN, SO WE HAVE TO COME BACK TO THIS LECTURE#########################
#########################IEX API IS CURRENTLY DOWN, SO WE HAVE TO COME BACK TO THIS LECTURE#########################
#########################IEX API IS CURRENTLY DOWN, SO WE HAVE TO COME BACK TO THIS LECTURE#########################
#########################IEX API IS CURRENTLY DOWN, SO WE HAVE TO COME BACK TO THIS LECTURE#########################
#########################IEX API IS CURRENTLY DOWN, SO WE HAVE TO COME BACK TO THIS LECTURE#########################
#########################IEX API IS CURRENTLY DOWN, SO WE HAVE TO COME BACK TO THIS LECTURE#########################
#########################IEX API IS CURRENTLY DOWN, SO WE HAVE TO COME BACK TO THIS LECTURE#########################


# In[ ]:


#THE COURSE ORGANISER HAS ADVISED USING "YAHOO FINANCE" UNTIL IEX ISSUES ARE FIXED


# In[ ]:


#importing and organising data in python part 3:


# In[5]:


import quandl #first we have to "pip install quandl + press ENTER" in anaconda prompt


# In[6]:


mydata_01 = quandl.get("FRED/GDP") #FRED = Federal Reserve Economic Data. GDP = Gross Domestic Product


# In[7]:


mydata_01.tail()


# In[8]:


mydata_01.head()


# In[9]:


#we can save the quandl data here in the form of *.csv after we import the pandas library


# In[10]:


import pandas as pd


# In[22]:


mydata_01.to_csv('Desktop/Python/example_01.csv') #this will save the quandl data as csv on your desktop


# In[26]:


#we could also open a comma separated file by doing the following:
mydata_02 = pd.read_csv('Desktop/Python/Lecture57/Data_02.csv') #I downloaded Data_02 csv file from resources section
#then I saved it in a folder within my desktop python folder (lecture57), now we are going to open this csv file


# In[27]:


mydata_02.head()


# In[28]:


mydata_02.tail()


# In[29]:


#saving and loading an Excel file requires you to follow the same steps:


# In[30]:


mydata_02.to_excel('Desktop/Python/example_02.xlsx') #this will save convert your data_02 csv to excel


# In[31]:


mydata_03=pd.read_excel('Desktop/Python/Lecture57/Data_03.xlsx') #I downloaded Data_03 file from resources section
#then I saved it in a folder within my desktop python folder (lecture57), now we are going to open this xlsx file


# In[40]:


mydata_03.tail()


# In[33]:


#Changing the index of your time series data
#time series data represents a series of data points indexed chronologically.
#Python automatically assigns numbers to every row of your data starting from 0 in pythonic terms. /
#We can say Panda's has rendered the default integer index. in these situations our job will be /
#to set another column as an index of the table. There are 2 ways to do this:


# In[34]:


#Method 1:
#the first method is to use the date index: (lets use Data_02 as an example)
#hence we can upload the data (mydata_02) once more but this time we will add a comma and index column written index
mydata_02 = pd.read_csv('Desktop/Python/Lecture57/Data_02.csv', index_col='Date')


# In[36]:


mydata_02.tail() #we apply tail just to keep the notes short


# In[37]:


#as you can see above; the first column, pythonic index, has disappeared, and date is now our new index.


# In[41]:


#Method 2:
#now we can directly applying indexing if the data is already loaded.
#if not loaded, then we have to do the following before indexing: mydata_03=pd.read_excel........ and so on.
#for example for mydata_03 we only have years instead of absolute date. so we can index the data to year:
mydata_03.set_index('Year').tail() #we apply tail just to keep the notes short


# In[42]:


#there is however an issue with this method. set underscore index will just display the data with the index you /
#have indicated. hence if we type mydata_03 again, we will see the python indexing:
mydata_03.tail()


# In[43]:


#to resolve this we have to reassign mydata_03 to year indexing
mydata_03=mydata_03.set_index('Year')


# In[45]:


mydata_03.tail() #this should delete the python indexing, and make Year the main index


# In[46]:


#the above methods (1 and 2) were the 2 ways to convert a table with information into a time series data in Python.


# In[1]:


#also one way to check validity of our notebook file is to select kernel, restart & run all.
#python will run the entire code unless there is an error somewhere, if there is an error, it will stop and not /
#continue running the rest of the code. since this file is only notes, we will not try that here. 
#but remember this for interviews, especially if you want to show your work


# In[2]:


############## Section 11: Part II Finance: Calculating and comparing the rates of return in Python #################


# In[3]:


#Government Bonds: they have an average return of 3%, and there has only been a few cases of governments going /
#bankrupt and not repaying investors, hence it is low risk. Investor is expected to receive the initial investment + /
#the interest. 


# In[4]:


#Stocks(equity shares): they have a higher rate of return, 6% on average, however there are higher fluctuations and /
#price changes. different variables influence a company's share price; operations, competition, /
#regulatory environment, strategic decisions and industry trends. 
#higher returns come at the price of higher risk.
#It's about making informed decisions that consider both dimensions of risk and return & optimizing the /
#risk return combination of an investment portfolio.


# In[5]:


# Calculating a security's rate of return: (selling price + dividends - buying price) / (buying price).
# this is also known as simple rate of return, also expressed as = [(selling price + dividends) / (buying price)] - 1
# to find out whether this was a good investment, we can compare the rate of return % to other investments.
# Logarithmic Rate of Return = Log (Selling price/Buying price) = Log(selling price) - Log(buying price)
# we cannot use both logarithmic and simple rate of return in the same financial analysis. 
# both methods are valid, however simple rate of return is more applicable when dealing with multiple assets over /
# the same timeframe.
# logarithmic rate of return is preferred for calculations of a single asset over time.


# In[6]:


# Timeframe is important for rate of return: investments with different holding periods shouldn't be compared.


# In[7]:


# Annual Return = [(daily return + 1)^365]*100 
#this formula converts daily, monthly and quarterly returns to yearly


# In[8]:


# Connection between Historical and Expected rates of return (Future return represented by a proxy):


# In[5]:


#Calculating a Security's rate of return in python: Simple Returns: Part I
import numpy as np
from pandas_datareader import data as wb #this is a module
import matplotlib.pyplot as plt #this allows us to work with charts and edit their elements easily


# In[6]:


PG = wb.DataReader('PG', data_source='yahoo', start='1995-1-1')


# In[7]:


PG.head()


# In[8]:


PG.tail()


# In[9]:


# Adj Close: The adjustment that has been made reflects dividend payments to shareholders and operations such as
#stock splits. hence this is the most righmost column to use for calculations of simple rate of return.


# In[10]:


#a reminder, P1=price of day 1, P0=price of day zero. simple rate of return = (P1/P0) - 1
#and now we are going to calculate the daily rate of return by creating an extra column using the following:
PG['simple_return'] = (PG['Adj Close'] / PG['Adj Close'].shift(1)) - 1 #pandas.DataFrame.Shift(number of lags) = P0
#if i want the adj close price of 2 days before today then I will type .shift(2)
print (PG['simple_return']) 


# In[11]:


#NaN: Not a Number


# In[12]:


#Calculating a Security's rate of return in python: Simple Returns: Part II
#in this part we will plot the daily rate of return


# In[13]:


PG['simple_return'].plot(figsize=(8, 5))
plt.show()


# In[14]:


# Quite often positive returns have been followed by negative returns. As you can see the most significant daily /
#observations were mainly negative.
# In finance we are accustomed to seeing negative returns that have a much higher magnitude of positive returns /
#usually positive returns accumulate over time and stock prices increase. But when things do go wrong stock prices /
#tend to fall very quickly.
# However an investor who is interested in buying a stock and holding it in the long run is mainly interested in /
#the average rate of return that the stock will have.


# In[15]:


#Average Rate of Return:
avg_returns_d=PG['simple_return'].mean() #calculates the daily average rate of return
avg_returns_d


# In[16]:


#this is a small number, to get a better observation lets multiply the results by number of annual trading days (250)
avg_returns_a=PG['simple_return'].mean()*250
avg_returns_a


# In[17]:


#but we still need to make this more presentable, so we need to turn it into a string and add percentage:
print (str(round(avg_returns_a, 5)*100) + ' %') #5 indicates the number of digits after the decimal point


# In[18]:


######### NUMBER OF DECIMALS HAVE NOT BEEN DISPLAYED PROPERLY, WAIT FOR FORUM TO ANSWER YOUR QUESTION ###########


# In[19]:


#Calculating a Security's rate of return in python: Logarithmic Returns:
#Log Returns = Ln[(Pt)/(Pt-1)], Pt-1 is the price of the day before, Pt is price of today.


# In[20]:


PG.head()


# In[24]:


PG['log_return'] = np.log(PG['Adj Close'] / PG['Adj Close'].shift(1)) #NumPy offers vectorised computation (vectors /
#matrices, and multidimensional arrays). hence loops can be replaced with 1 dimensional or multi-dimensional arrays /
#via the process of vectorisation (which is performed by array programming)
print (PG['log_return'])


# In[25]:


PG['log_return'].plot(figsize=(8, 5))
plt.show()


# In[27]:


log_return_d=PG['log_return'].mean() #calculates the daily average rate of return
log_return_d


# In[29]:


log_return_a=PG['log_return'].mean()*250 #calculates the annual average rate of return
log_return_a


# In[32]:


print (str(round(log_return_a, 5)*100) + ' %')


# In[1]:


# What is a portfolio of securities and how to calculate its rate of return:
# calculating rate of return for a portfolio of stocks:
# rate of return of a security (e.g. apple stocks) * weight (%) of security (apple stocks) in the portfolio
# do this calculation for all securities in the portfolio and add up the total, this is the portfolio rate of return


# In[2]:


#Calculating the return of a portfolio of securities (PG, MSFT, F, GE)
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt


# In[3]:


tickers = ['PG', 'MSFT', 'F', 'GE']
mydata=pd.DataFrame()
for t in tickers:
    mydata[t]=wb.DataReader(t, data_source='yahoo', start='1995-1-1')['Adj Close']


# In[4]:


mydata.info()


# In[5]:


mydata.head()


# In[6]:


mydata.tail()


# In[7]:


# Now we will create a line chart of these results to see how these securities performed throughout the timeframe
#to do this, we need to normalise the data to 100: (Pt/P0)*100
#we need to use the "iloc" indexer (zero between the brackets) to extract the data from the first row of the table


# In[9]:


mydata.iloc[0]


# In[11]:


#Normalisation: (Pt/P0)*100, this is a mathematical trick, the first row (P0) divided by itself (P0) will always /
#produce 1, multiplied by 100 will give 100. hence all stocks will start on vertical axis at 100
#we do this to compare the behavior of the four different stocks as if they were all starting from the same value 100
(mydata / mydata.iloc[0] *100).plot(figsize = (15, 6));
plt.show()


# In[13]:


#If we don't do this we will see the adjusted closing prices of all companies plotted directly /
#and we will not have a good landmark, see the graph below:
(mydata).plot(figsize = (15, 6))
plt.show()


# In[14]:


#we can also use the "loc" indexer (date in brackets) to extract data from first row
mydata.loc['1995-01-03']


# In[15]:


#both "loc" and "iloc" indexer can be used interchangeably, and you can use them to extract data from any row


# In[17]:


#the next step is to calculate the return (simple return) of all 4 stocks and create a new table with them:
returns = (mydata/mydata.shift(1)) - 1
returns.head()


# In[18]:


weights = np.array([0.25, 0.25, 0.25, 0.25])


# In[19]:


# calculate the product of the weight of each stock by its return via matrix multiplication, via NumPy.dot method
#in pythonic terms, the one or multi-dimensional array we obtain is referred to as the dot product
np.dot(returns, weights)


# In[20]:


#we got an array as a result of matrix multplication between returns matrix and weight matrix (has 1 column & 4 rows)
#but we need a single number to give us an idea of the portfolio's return
# we got an array answer because we forgot to estimate the average return of each stock's price:


# In[21]:


annual_returns=returns.mean()*250
annual_returns


# In[22]:


np.dot(annual_returns, weights)


# In[24]:


#now let's save this as a percentage value:
pfolio_1 = str(round(np.dot(annual_returns, weights), 5)*100) + ' %'
print (pfolio_1)


# In[25]:


#now let's say we have the same securities in a new portfolio with different weighting, let's compare:
weights_2=np.array([0.4, 0.4, 0.15, 0.05])


# In[30]:


pfolio_2 = str(round(np.dot(annual_returns, weights_2), 5)*100) + ' %'
print (pfolio_1)
print (pfolio_2)


# In[31]:


# Popular stock indices that can help us understand financial markets:
#market index is a good proxy for the development of the market.
#It would be too difficult to measure the development of every security traded in a stock exchange.
#Some securities are small and their shares are not even traded daily.
#That's why practitioners use market indices to provide an idea of the overall market performance.
#Stock Indices are an excellent comparator to understand how your own stocks are performing.


# In[32]:


# Top US Market Indices
# i. S&P 500: comprises 500 of the largest listed companies. The diverse constituency of the S&P 500 makes it a /
#true approximation of the U.S. stock market. It is a market cap weighted index so companies are weighted according /
#to their market value. If the market cap of P and G is three times the market cap of Nike a 1 percent change /
#in P and Gs shareprice will have three times the impact (on the market) of a 1 percent change in Nike's price.
# ii. Dow Jones Industrial Average: The Dow Jones industrial average index uses an average of 30 large /
#public stocks traded in the U.S market. it is one of the oldest indices calculated historically. /
#However it cannot be used as a representation of the U.S. stock market because it includes only 30 stocks and /
#is equally weighted, hence all stocks are considered in the same way disregarding their size.
# iii. NASDAQ composite index: It is an index of grouped securities that are listed on the Nasdaq stock exchange.
#Most companies listed there are IT companies and Nasdaq shows us about the rate of return of tech stocks.


# In[33]:


# Foreign Stock Indices
#FTSE100 UK
#DAX30 Germany
#NIKKEI Japan
#SSE (composite index) China


# In[34]:


# Global Indices:
#MSCI: Morgan Stanley Capital International: includes stocks from all developed markets in the world


# In[35]:


#If you want to understand whether one of the stocks you own is performing well one of the best comparators you /
#can use is a stock index; by commparing the stock against the overall market performance.
#In addition a stock index gives you a sense of the type of return you can expect if you invest in a /
#well diversified portfolio in a given market.


# In[39]:


#Calculating the Indices Rate of Return:
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt


# In[43]:


tickers = ['^GSPC', '^IXIC', '^GDAXI', '^DJI'] #GSPC=S&P500, IXIC=Nasdaq, GDAXI=DAX30, DJI=DowJonesIndustrialAverage
# ^ this sign indicates that we are dealing with market index data
ind_data = pd.DataFrame()
for t in tickers:
    ind_data[t]=wb.DataReader(t, data_source='yahoo', start='1997-1-1')['Adj Close']


# In[44]:


ind_data.head()


# In[45]:


ind_data.tail()


# In[46]:


(ind_data/ind_data.iloc[0]*100).plot(figsize=(15, 6));
plt.show()


# In[ ]:


#graph analysis:
#We observe a general rise of the indices value. This was because in the period between 1995 and 2001 there was /
#a dot.com bubble and the stock markets in industrialized countries like USA UK and Germany were boosted by a / 
#significant rise in the value of Internet companies being composed primarily of tech companies Nasdaq logically /
#depicts best this trend relative to the other indices in a certain period its performance declines abruptly in /
#the next few years. Germany manifest stability and growth. Of course the global economic and financial crises of /
#2007 2008 as well as the sovereign debt crisis in 2011 reflect the picture accordingly. But in the long term /
#observing the results from 1997 until today we can say that overall all indices performed very well 


# In[47]:


ind_returns = (ind_data / ind_data.shift(1)) - 1


# In[48]:


ind_returns.head()


# In[49]:


ind_returns.tail()


# In[50]:


annual_ind_returns=ind_returns.mean()*250
annual_ind_returns


# In[52]:


#now let's compare a stock with indices: 
#(The first type of analysis that you need to perform when analyzing the stock market)
tickers = ['PG', '^GSPC', '^DJI']
data_2 = pd.DataFrame()
for t in tickers:
    data_2[t] = wb.DataReader(t, data_source='yahoo', start='2007-1-1')['Adj Close']


# In[53]:


data_2.head()


# In[54]:


data_2.tail()


# In[55]:


(data_2/data_2.iloc[0]*100).plot(figsize=(15, 6));
plt.show()


# In[1]:


############################# Section 12: Part II Finance: Measuring Investment Risk ################################


# In[2]:


#How to measure and forecast a security's risk:
#Variability is the best measure of risk we have. we can look at the average rate of return over the past years for /
#a stock security, if the fluctuations are too high, then that indicates high variability, which is risky.
#a volatile stock market is much more likely to deviate from its historical returns and surprise investors negatively.
#investors don't like surprises, whether positive or negative, they prefer stable known rate of return.


# In[3]:


#Statistical Measures to Quantify Risk:
# Variance: measures the dispersion of a set of data points around the mean: S^2=[Sum(X-Xm)^2]/[N-1]
# Standard Deviation : SQRT(S^2)


# In[8]:


#Calculating a Security's Risk (aka volatility, aka standard deviation) in Python:
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt


# In[9]:


tickers = ['PG', 'BEI.DE']
sec_data = pd.DataFrame()
for t in tickers:
    sec_data[t] = wb.DataReader(t, data_source='yahoo', start='2007-1-1')['Adj Close']


# In[10]:


sec_data.head()


# In[11]:


sec_data.tail()


# In[12]:


sec_returns = np.log(sec_data / sec_data.shift(1)) #we use log return because we will examine each company separately


# In[13]:


sec_returns


# In[14]:


#PG


# In[15]:


sec_returns['PG'].mean() #daily average return


# In[16]:


sec_returns['PG'].mean()*250 #annualised average return


# In[17]:


sec_returns['PG'].std()


# In[18]:


sec_returns['PG'].std()*250**0.5 #we do to the power of 0.5 which is SQRT, because std is equivalent to SQRT of S^2
#so to annualise SQRT(S^2) we need to multiply it by 250 inside the SQRT, hence it becomes SQRT[(S^2)x250]


# In[19]:


#Beiersdorf


# In[20]:


sec_returns['BEI.DE'].mean()


# In[21]:


sec_returns['BEI.DE'].mean()*250


# In[22]:


sec_returns['BEI.DE'].std()


# In[23]:


sec_returns['BEI.DE'].std()*250**0.5


# In[24]:


#PG seems to have a higher mean and BEI.DE has a higher std(volatility), but we need to present this better:
print (sec_returns['PG'].mean()*250)
print (sec_returns['BEI.DE'].mean()*250)


# In[25]:


#another way to present the mean values:
sec_returns[['PG', 'BEI.DE']].mean()*250 #we use 2 brackets because there cannot be a floating point with 2 values
#a float can only contain a single value. Therefore we must create an array with two dimensions briefly. Each pair /
#of brackets we surround are column names which will increase the number of dimensions of the newly created NumPy /
#object by 1.


# In[26]:


sec_returns[['PG', 'BEI.DE']].std()*250**0.5


# In[27]:


#This implies we have recorded the mean values of DNG and of buyers Dorce returns as elements in one matrix and /
#the values of their standard deviations in another matrix 


# In[28]:


#Benefits of Portfolio Diversification:
#The relationship between securities: common factors influence the price of shares in a stock exchange.
#general favorable macro economic conditions facilitate the business of all companies. When people have jobs and /
#some money in their pockets they will spend more. And companies benefit from that as their revenues increase.
#In a tough economy consumers reduce their spending and buy mainly products of primary importance and because stock /
#prices are determined by profits whenever the economy is doing good stock prices are higher. Investors will pay a /
#high price for profitable companies. During recession companies profits are lower & share prices fall significantly.


# In[29]:


#Calculating the Covariance between Securities: (measuring the relationship between stocks):
#The correlation coefficient measures the relationship between 2 variables: SigmaXY=[(X-Xm)*(Y-Ym)]/[stdX*stdY]
#X=house size, Y=house price. The formula can also be expressed as: SigmaXY=[SUM(X-Xm)*(Y-Ym)]/[n-1]
# if Covar > 0, the 2 variables move in the same direction
# if Covar < 0, the 2 variables move in the opposite direction
# if Covar = 0, the 2 variables move independently
#sometimes the value of Covariance tends to be very large, e.g. 50, or 0.00002345 which is hard to interpret, that's /
#why we need Correlation.


# In[30]:


#Correlation adjusts Covariance.
#Interpreting Correlation:
#Perfect Correlation: house price directly proportional to house size (straight line on the graph of price/size)
# this means that the house size is the only variable that determines house price.
#but in reality there are other variables that affect the house price; such as location and year of construction.


# In[31]:


#Variables that determine the Share Price:
# Industry Growth
# Revenue Growth
# Profitability
# Regulatory Environment


# In[32]:


#The more similar the context in which two companies operate the more correlation there will be between their share /
#prices as they will be influenced by the same or similar factors.
#No Correlation: variables with 0 correlation are absolutely independent from each other.
#Negative Correlation: variables move in opposite directions. 2 types: perfect negative correlation (-1), and 
#imperfect negative correlation (between -1 and 0). example of negative correlation: ice cream and umbrella / 
#in this example weather is the common variable, however it affects the businesses in different way.


# In[33]:


#calculate the covariance and the correlation between the prices of two companies Procter and Gamble and buyers:


# In[34]:


# we first need to understand the concept of Covariance Matrix:
#It is a representation of the way two or more variables relate to each other. The covariance between a variable /
#and itself is the variance of that same variable actually. So along the main diagonal you will have the variances /
#of the variables and the rest of the matrix table will be filled with the covariances between them.

#In our case the variables are two stock prices. Therefore we will expect a two by two covariance matrix with the /
#variances of each stock along the main diagonal and the covariance between the two stocks displayed in the other /
#two cells.

# it will look like this:           Var(PG)       | cov(PG, BEI)
#                                   --------------|--------------
#                                   cov(BEI, PG)  | Var(BEI)


# In[35]:


#pandas.DataFrame.var() calculates the variance:


# In[36]:


PG_var = sec_returns['PG'].var() #Daily Return Variance
PG_var


# In[37]:


BEI_var = sec_returns['BEI.DE'].var()
BEI_var


# In[38]:


PG_var_a = sec_returns['PG'].var()*250 #Annual Return Variance
PG_var_a


# In[39]:


BEI_var_a = sec_returns['BEI.DE'].var()*250
BEI_var_a


# In[40]:


#at this stage it is unnecessary to create a data frame and fill in each cell with values. The cov method whose /
#name comes from the term covariance does this for us automatically, it computes pairwise covariance of columns:
cov_matrix = sec_returns.cov() #sec_returns is associated with sec_data which has info about PG and BEI.DE stocks
cov_matrix #the covariances should be the same: 0.000039


# In[41]:


cov_matrix_a = sec_returns.cov()*250 #now we annualise it
cov_matrix_a


# In[42]:


#the correlation is calculated via the corr method in python, it computes pairwise correlation of columns:
corr_matrix = sec_returns.corr()
corr_matrix


# In[43]:


# we get 1.0 beacause we divide the variances of PG and BEI.DE by the same values.
#it just means that the movement of a stock is perfectly correlated with itself.
#the correlation formula: [cov(x,x)]/[std(x)*std(x)] = var(x)/var(x)

# The other two cells in the correlation table contain the same number. They tell us the stock returns of the two /
#companies are weakly correlated and be very careful here, this is not the correlation between the price of the two /
#equities.
#the correlation between returns which is the same as to say the correlation between the rate of returns reflects /
#the dependence between prices at different times and focuses on the returns of your portfolio rather than on /
#stock price levels. as an investor, return is what you care about, not the nominal price of the stock.


# In[44]:


#Finally don't fall in the trap of annualizing the correlation table, It does not contain average daily values. It /
#shows us the relation that exists between the two variables, so we need not multiply by 250.


# In[45]:


#Considering the risk of multiple securities in a portfolio: (calculation of portfolio variance)
#If a portfolio contains two stocks its risk will be a function of the variances of the two stocks and /
#the correlation between them.
#basic algebra: (a+b)^2 = a^2 + 2ab + b^2
#formula for calculating portfolio variance of 2 stocks: (W1.std1 + W2.std2)^2 , W=weight of stock, hence W1+W2 = 1
# (W1.std1 + W2.std2)^2 = W1^2.std1^2 + 2W1.std1.W2.std2.cov(stock1, stock2) + W2^2.std2^2, remember std^2 = var.
#cov(stock1, stock2) is aka the correlation coefficient between stock1 and stock2
#This is how we calculate a portfolio's variance. It depends on two things. The standard deviations of the /
#two stocks and the correlation between the stocks


# In[46]:


#Calculating Portfolio Risk
#Equal Weighting Scheme:
weights = np.array ([0.5,0.5])


# In[47]:


#Portfolio Variance:
pfolio_var = np.dot(weights.T, np.dot(sec_returns.cov()*250, weights)) # T = transposed
#the line above translates to the following: 
# [W1, W2]horizontal matrix * [Var&Cov matrix] * [W1,W2]vertical matrix
# the line above = transposed weights vector * annualised covariance matrix * normal weights vector
#numpy.dot() method makes this complex multiplication look simple
pfolio_var


# In[48]:


#Portfolio Volatility:
pfolio_vol = np.dot(weights.T, np.dot(sec_returns.cov()*250, weights))**0.5
pfolio_vol


# In[51]:


print (str(round(pfolio_vol, 5)*100) + ' %')


# In[52]:


#The classic mathematical computation would have taken us much longer, the same dot product structure can be used /
#when calculating the risk of investing in a multi-asset portfolio where larger weights and covariance matrices will /
#be involved.


# In[53]:


#Understanding systematic and idiosyncratic risk.
#portfolio's risk can be described as the sum of two components: the variances of the securities contained in the /
#portfolio and the products of the covariances (and correlation) between securities and their standard deviations.

#Systematic risk is Un-Diversifiable: it depends on the variance of each individual security. Systematic risk is /
#made of the day to day changes in stock prices and is caused by events that affect all companies. examples of events:
# Recession of the economy
# Low consumer spending
# Wars
# Forces of nature (e.g. earthquakes)
#there is not much we can do about systematic risks, we have to just accept these uncertaincies.

#idiosyncratic risk is Diversifiable: this is aka company specific risk, driven by company specific events. these /
#risks can be smoothed out through diversification. 
#Diversifiable risks can be eliminated if we invest in non-correlated assets.
#Academic research has shown if we build a portfolio containing at least 25 to 30 stocks that are not correlated /
#unsystematic risk will almost disappear. e.g. S&P500 index is well diversified. If you own a portfolio of 500 /
#stocks the only risk you are exposed to is systematic risk and it doesn't mean this comes at the expense of a /
#lower expected return.
#Some institutional investors go even further and build portfolios of securities not from the same country which /
#should reduce the correlation between these securities even further and drive down the overall portfolio.


# In[54]:


#Calculating diversifiable and non-diversifiable risk of a portfolio:
weights = np.array([0.5, 0.5])


# In[55]:


weights[0] #weight of security 1


# In[56]:


weights[1] #weight of security 2


# In[ ]:


#this examples allows us to emphasize the difference between creating an indie array with single or double brackets.
#each pair of brackets around the name of the column will add one dimension to the NumPy array.


# In[57]:


#Diversifiable Risk (annual) = Portfolio Variance - Weighted Annual Variances of each Stock
PG_var_a = sec_returns [['PG']].var() * 250
PG_var_a #value will be expressed as single elements in 1x1 matrices that is two dimensional arrays.


# In[58]:


BEI_var_a = sec_returns [['BEI.DE']].var() * 250
BEI_var_a


# In[59]:


dr = pfolio_var - (weights[0] ** 2 * PG_var_a) - (weights[1] ** 2 * BEI_var_a) # dr = Diversifiable Risk
dr 


# In[60]:


#the answer above is strange, instead of a float we obtain a vector with no numbers (NaN)
#we can fix this by 
# i) turning the 1x1 matrix into a float
float(PG_var_a)


# In[61]:


# ii) when you assign a value to PG_var_a you can use single brackets when you indicate you will use data from the /
#PG column. this will automatically store the output as a float value the dtype: float64 line will disappear and you /
#will see more digits after the decimal point. we will repeat the last 3 calculations now.
PG_var_a = sec_returns ['PG'].var() * 250
PG_var_a #so now PG_var_a is a floating point


# In[62]:


BEI_var_a = sec_returns ['BEI.DE'].var() * 250
BEI_var_a


# In[63]:


dr = pfolio_var - (weights[0] ** 2 * PG_var_a) - (weights[1] ** 2 * BEI_var_a)
dr


# In[66]:


print (str(round(dr, 5)*100) + ' %')


# In[67]:


#the above can also be written as:
print (str(round(dr*100, 5)) + ' %') 


# In[68]:


# Non-Diversifiable Risk
# method i: substract diversifiable risk from the portfolio variance
n_dr_1 = pfolio_var - dr
n_dr_1


# In[69]:


#method ii: summing the annual variances
n_dr_2 = (weights[0] ** 2 * PG_var_a) + (weights[1] ** 2 * BEI_var_a)
n_dr_2


# In[70]:


n_dr_1 == n_dr_2 #either method is valid, hence we should get a True value.


# In[1]:


####################### Section 13: Part II Finance: Using Regressions for Financial Analysis ######################


# In[2]:


# Regression Analysis: quantifying the relationship between 2 variables; dependent variable and independent variable
# Regression analysis can be handy when we want to forecast a future dependent variable with the help of patterns /
#from our historical data.
# example: the larger the house, the higher it's price. the dependent variable is the house price, the independent /
#variable (aka explanatory variable: it helps us explain why some houses cost more) is the size of the house.
#Simple Regression: using only 1 variable
#Multivariate Regression: using more than 1 variable


# In[3]:


#Simple Regression: relationship between house prices and house size.
#How do we determine the best line that will help us describe the relationship between house prices and house size?
#the best fitting line contains the least amount of estimation error. estimation error is the distance between the /
#points on a graph (observations) and the line of best fit. so each deviation from the line is an error.
# a simple regression equation is similar to equation of a straight line (y = mx + c):
# y = alpha + beta.x


# In[5]:


# Running a regression in python:
import numpy as np
import pandas as pd

from scipy import stats
import statsmodels.api as sm

import matplotlib.pyplot as plt


# In[6]:


data = pd.read_excel('Desktop/Python/Housing.xlsx') #saved the housing.xlsx file from lecture resources onto desktop


# In[7]:


data


# In[8]:


data[['House Price', 'House Size (sq.ft.)']]


# In[9]:


#now we can perform Univariate Regression (since we are using only 1 independent variable):
x = data['House Size (sq.ft.)'] #independent variable
y = data['House Price'] #dependent variable


# In[10]:


x


# In[11]:


y


# In[12]:


plt.scatter(x,y)
plt.show


# In[13]:


#the axis of the above graph does not start from 0 for either x or y axis, let's fix it:
plt.scatter(x,y)
plt.axis([0, 2500, 0, 1500000])
plt.show


# In[14]:


#now lets label the graph too:
plt.scatter(x,y)
plt.axis([0, 2500, 0, 1500000])
plt.ylabel('House Price')
plt.xlabel('House Size (sq.ft.)')
plt.show


# In[15]:


#are all regressions created equal? let's learn how to distinguish good regressions:
#which regressions are reliable? 
# a simple regression containing only one variable will omit some important factors, which will result in an /
#estimation error (an estimate deviating from the actual price). hence simple regression is useful, but not perfect
# hence the equation for simple regression would be: y = alpha + beta.x + error
#in terms of sample observations, errors are aka residuals
#The best fitting line minimises the squared sum of the distances of these residuals.
# If you draw a different line to the best fitting line in this plot, it's squared residuals will be higher than /
#the sum of the squared residuals of the best fitting line.
#This is the reason coefficients found with this technique are called OLS (Ordinary Least Square) estimates.
#We need to find a line that minimizes the distance between itself and the actual data observations we are using to /
#calculate a regression. So that's how we calculate regression coefficients and an equation that allows us to /
#predict the independent variable. 


# In[16]:


# we can distinguish between good and bad regression using the R-squared statistical method.
# to understand R-squared method, we need to think about the following question:
# "how can we measure data dispersion and variability?": We need to think of the total variability of the data /
# which is the measure for data dispersion and variability, in other words variance (S^2=[Sum(X-Xm)^2]/[N-1]).
#so we'll use that concept very close to the one variance, it is called TSS (Total Sum of Squares)
# TSS = Sum(X-Xm)^2 
# TSS provides a sense of variability of the data.


# In[17]:


# R-squared formula: R^2 = [1-(SSR/TSS)] #SSR is the sum (total) of squared residuals (errors) of the entire data.
#R-squared is aka regression coefficient
#R-squared varies between 0-100%, the higher it is the more predictive power the model has.
#Typically a simple regression with an R squared of less than 10% has little predictive value.
#One variable regression with an R squared a 30 percent or more are solid indicators of future performance.


# In[18]:


# Computing Alpha, Beta and R-squared in Python:


# In[21]:


#we have already read the housing data from the excel file, now we will run a regression, followed by statistical /
#interpretation:
x1 = sm.add_constant(x) #the stats module (sm) contains tools for running a regression
reg = sm.OLS(y,x1).fit() #fit method will apply a specific estimation technique to obtain the full fit of the model.
#in summary: first you need to include a constant. We will assign the newly obtained information which is the /
#object "x" and the constant to a new variable. Let's call it "x1", right after that we will assign to another /
#variable "reg". The output is an ordinary least squares (OLS)regression. for OLS arguments we must add the /
#dependent variable "y" and the newly defined "x1".


# In[22]:


reg.summary()


# In[23]:


#in the above table we can see an R-squared value of 0.678, which means that the independent variable in our /
#regression; House Size, can explain 68% of the dependent variable; House Price. hence this is a good model
# in the second table above, we can see that the first row includes info regarding the constant we added:
# the const coef = 260800 = Alpha = interception on Y-axis = regression line will cut the axis at this point
# in the second row of second table: House Size (sq.ft.) Coef = 401.9 = Beta = slope of the regression line 
#this means for every sq.ft the price is expected to go up by $402
#the House Size (sq.ft.) std err = 65.243 = it means that Beta will vary within the range of $65


# In[24]:


#now lets test this model using expected value of y for a 1000 sq.ft house:
260800 + 401.9*1000


# In[25]:


#the graph shows 2 properties with price of roughly $610,000, which is in line with the $662700 we calculated for /
#a 1000 sq.ft house, and it is within the std err margin of $65*1000, hence this model is valid


# In[26]:


#This statsmodel's library allows us to apply a complete OLS model that provides three tables with multiple /
#statistics alternatively stats.linregress allows us to extract five of these statistics very quickly:
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)


# In[27]:


slope #Beta


# In[28]:


intercept #Alpha


# In[29]:


r_value


# In[30]:


r_value**2 #R-squared


# In[31]:


p_value #we will learn more about this in multivariate regression


# In[32]:


std_err


# In[33]:


####################### Section 14: Part II Finance: Markowitz Portfolio Optimisation ######################


# In[34]:


# investments in multiple securities shouldn't be analyzed separately but should be considered in a portfolio and /
#financier's must understand how different securities in a portfolio interact with each other.
#the combination of securities with low correlation allows Investors to optimize their returns without assuming / 
#additional risk.
#Markowitz assumes investors are rational and risk averse so they are interested in earning higher returns and /
#prefer avoiding additional risk.
# for any level of risk investors will be interested only in the portfolio with the highest expected return.
#Markowitz suggests there is a set of efficient portfolios that can provide a higher expected rate of return for /
#the same or even lower risk. This group of portfolios is called the Efficient Frontier. Check the excel example in /
#this lecture.
#Its starting point (top right) is the minimum variance portfolio; the lowest risk an investor could bear.
#points below the efficient frontier represent inefficient portfolios. As for each we can find an alternative /
#portfolio with greater expected return for the same level of standard deviation.


# In[42]:


#Obtaining the Efficient Frontier in Python: Part I:
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline  #this line of code contains some specific matplotlib features')
#the code above(%) facilitates plotting matplotlib graphs just below code cells & storing them in a notebook document


# In[43]:


assets = ['PG', '^GSPC']
pf_data = pd.DataFrame()

for a in assets:
    pf_data[a] = wb.DataReader(a, data_source = 'yahoo', start = '2010-1-1')['Adj Close']


# In[44]:


pf_data.tail()


# In[45]:


(pf_data/pf_data.iloc[0]*100).plot(figsize=(10,5))


# In[46]:


log_returns=np.log(pf_data/pf_data.shift(1))


# In[47]:


log_returns.mean()*250


# In[48]:


log_returns.cov()*250


# In[49]:


log_returns.corr()


# In[50]:


#Portfolio Optimisation:
#First we must create a variable that will carry the number of assets in our portfolio. We will use it in our /
#formulas so they can respond to a change in the number of assets that compose the portfolio. It will equal the /
#number of elements of the assets list. we can obtain this number with the help of the "len" function:
num_assets = len(assets)


# In[51]:


num_assets # we only have PG and GSPC, so we should get 2


# In[52]:


#now we must create two random weights right now. np.random.random could generate two floats between 0 and 1.
#when we run this code and we obtain two new values:
arr=np.random.random(2)
arr


# In[53]:


arr[0]+arr[1]


# In[54]:


#there is a problem with this method; the 2 weights don't add up to 1, so we must do the following:
weights = np.random.random(num_assets) #we assign 2 random numbers between 0 and 1 to the new NumPy array "weights"
weights /= np.sum(weights) # w=w/sum(w)
#weights array [w1 w2](vertical.matrix) turns into w = (w1/(w1+w2))+(w2/(w1+w2))
# this will equal w = (w1+w2)/(w1+w2) = 1
# this line of code it enables you to obtain two randomly generated weights whose sum will always equal 1.
weights


# In[55]:


weights[0] + weights[1]


# In[56]:


#Obtaining the Efficient Frontier in Python: Part II: The Markowitz Mean Variance Theory


# In[57]:


#Expected Portfolio Return:
np.sum(weights*log_returns.mean())*250 #np.sum = Numpy Summation of values in multi-dimensional objects


# In[58]:


#Expected Portfolio Variance:
np.dot(weights.T, np.dot(log_returns.cov()*250, weights))


# In[59]:


#Expected Portfolio Volatility: sqrt(Expected Portfolio Variance)
np.sqrt(np.dot(weights.T, np.dot(log_returns.cov()*250, weights)))


# In[60]:


#We went through these three cells (above) because we will need the formulas for the return and the volatility /
#in the simulation of the portfolios mean variance combinations
#We will create a graph where 1000 mean variance simulations will be plotted. 
#We are not considering 1000 different composed of different stocks.
#We are considering 1000 combinations of the same two assets PG and S&P 500.
#This means we simulate 1000 combinations of their weight values out of the 1000 combinations.
#e.g. one portfolio is going to have 1% PG and 99% ^GSPC, another portfolio with 99% PG and 1% ^GSPC


# In[62]:


#our goal is to create a graph that visualizes the hypothetical portfolio returns versus volatilities.
#Therefore we will need two objects where we can store this data.
#So portfolio returns starts as an empty list, We intend to fill with randomly generated expected returns:
pfolio_returns = []
pfolio_volatilities = [] #same rule applies to pfolio_volatilities
#The key is the append method that will add each newly generated portfolio return value to the list portfolio returns/
#and this operation will be repeated for each pass of the loop until the portfolio returns list accumulates 1000 /
#observations.
for x in range (1000):
    weights = np.random.random(num_assets) #two components (assets) generates two weights
    weights /= np.sum(weights)
    pfolio_returns.append(np.sum(weights*log_returns.mean())*250)
    pfolio_volatilities.append(np.sqrt(np.dot(weights.T, np.dot(log_returns.cov()*250, weights))))
    
pfolio_returns, pfolio_volatilities


# In[63]:


#in the above there should be 2 brackets [pfolio_returns, pfolio_volatilities] [pfolio_returns, pfolio_volatilities] /
#these are two super long lists containing 1000 values each.
#these lists are hard to manipulate, hence we need to convert them to NumPy arrays:


# In[64]:


pfolio_returns = []
pfolio_volatilities = [] 

for x in range (1000):
    weights = np.random.random(num_assets) 
    weights /= np.sum(weights)
    pfolio_returns.append(np.sum(weights*log_returns.mean())*250)
    pfolio_volatilities.append(np.sqrt(np.dot(weights.T, np.dot(log_returns.cov()*250, weights))))

pfolio_returns = np.array(pfolio_returns)
pfolio_volatilities = np.array(pfolio_volatilities)
    
pfolio_returns, pfolio_volatilities #now these 2 variables should be organised as arrays, looks better


# In[65]:


#now we neeed to plot the results on a graph.


# In[66]:


#Obtaining the Efficient Frontier in Python: Part III
#First we will create a data frame object containing two columns one for returns and another one for the respective /
#volatilities we will call this object portfolios:
portfolios = pd.DataFrame({'Return': pfolio_returns, 'Volatility': pfolio_volatilities})


# In[67]:


portfolios.head()


# In[68]:


portfolios.tail() #tail shows 1000 entries, hence our data is correct


# In[75]:


portfolios.plot(x='Volatility', y='Return', kind='scatter', figsize=(10, 10));
plt.xlabel('Expected Volatility')
plt.ylabel('Expected Return')


# In[1]:


######################## Section 15: Part II Finance: The Capital Asset Pricing Model (CAPM) ########################


# In[2]:


# in the CAPM setting, investors are:
#Risk-averse
#Rational: Prefer higher returns (they want to optimize their portfolios in terms of both risk and return)
#Willing to buy the Optimal Portfolio


# In[3]:


# The Market Portfolio: a combination of all the possible investments in the world
#the risk return combination of this portfolio is superior to the one of any other portfolio.
#The expected return of the market portfolio coincides with the expected return of the market and because this is a /
#diversified portfolio it makes sense it is optimal in terms of risk.
#this portfolio contains no idiosyncratic risk, only systematic risk. it also lies on the efficient frontier


# In[4]:


#CAPM assumes the existence of a risk free asset and investment with no risk (zero std).
#because of the risk-free nature of CAPM, investors are willing to accept a lower expected rate of return. but why?
#because in an efficient market investors are compensated only for additional risk they're willing to bear, this is/
#well-represented in the efficient frontier curve. Once investors own an efficient portfolio they can't arbitrage /
#the system and earn a higher expected return for the same level of risk.


# In[5]:


#once we introduce a risk free asset then it means the market portfolio isn't the only asset rational investors /
#would invest in, the risk free investment offers something new to investors; zero risk.
#So rational investors will form their portfolios considering both the risk free rate and the market portfolio.
#How much are they going to invest in risk free and how much are they going to invest in the market portfolio?
#Well it depends on how much they want to earn.
#The line that connects the risk free rate and is tangent to the efficient frontier is called the Capital Market line.
#Investors will allocated their money between the risk-free and market portfolio.
#The point where the Capital Market Line intersects the Efficient Frontier is the Market Portfolio.
#so an investor willing to take more risk will hold greater portion of the market portfolio compared to risk-free, /
#but if the investor is risk-averse, they will hold greater portion of the risk-free asset than market portfolio.
#investors who want even higher returns can borrow money and invest further to the right of the market portfolio.
#investors make their decisions based on their risk appetite


# In[6]:


#Understanding and Calculating a Security's Beta:
#Beta quantifies the relationship between the security and the overall market portfolio.
#during a recession the price of all the assets in the market portfolio will decrease, and the market portfolio /
#will experience a negative rate of return (e.g. -5%). Investors can't protect themselves through diversification /
#because this is systemic risk. during recession some stocks may perform less bad than the market portfolio since /
#they are less volatile, and some stocks perform even worse than the market portfolio because they are more volatile.
#but once the economy recovers, the more volatile stock will have much higher return than the less volatile stock.
#the market portfolio would have a postive return now (e.g. 9%).


# In[7]:


# Beta = [(cov(rStock, rMarket))/varianceMarket] = measures market risk that cannot be avoided through diversification


# In[8]:


#therefore, the riskier the stock, the higher it's Beta

# Beta = 0, no relationship between stock and the market
# Beta = 1, stock will perform the same way as the market

# Beta < 1, Defensive: during recession, these stocks will lose less, they are less risky
#but these stock will have lower return than the market when economy flourishes

# Beta > 1, Aggresive: stocks are riskier than the market, they do better than the market when economy flourishes
#but these stock will perform worse than the market during recession


# In[9]:


#some companies such as Walmart are going to be less affected by recession, because public will always need food.
#however other comapanies, such as car manufacturer's will be more affected by recession or any other economic cycle /
#this is because during recession, a car is not a priority, hence car companies will see a slump in revenues
# Beta (walmart) = 0.09, Beta (ford) = 1.1
#Conclusion: Beta is a measurement that shows us how risky an individual security is regarding the rest of the market.


# In[18]:


#Calculating the Beta of a stock: 
# Beta shows the extent to which the change in the price of security is related to the overall performance of market.
#in our example the stock will be PG and the market will be S&P 500.
import numpy as np
import pandas as pd
from pandas_datareader import data as wb

tickers = ['PG', '^GSPC']
data = pd.DataFrame() #we will create a new data frame object from pandas and we'll call it new data.
for t in tickers:
    data[t] = wb.DataReader(t, data_source='yahoo', start='2012-1-1', end='2016-12-31')['Adj Close']
    #Beta is typically measured with data from the past five years.


# In[19]:


sec_returns = np.log(data / data.shift(1))


# In[20]:


cov = sec_returns.cov()*250 #this will generate a covariance matrix between PG and GSPC
cov


# In[21]:


cov_with_market=cov.iloc[0,1] #iloc will allow us to obtain the covariance as a float
cov_with_market


# In[22]:


market_var=sec_returns['^GSPC'].var()*250
market_var


# In[23]:


PG_Beta = cov_with_market / market_var #this will give is Beta
PG_Beta


# In[24]:


#the value is greater than 0 and less than 1, hence PG is a Defensive stock
#we can cross-check the above value with Google Finance too, we can have a 2-3% margin difference.


# In[25]:


# CAPM Formula: ri = rf + Beta_im(rm - rf)

# ri = security's expected return = ith return
# rf = return of risk-free asset = the bare minimum that any investor must accept when making an investment
# Beta_im = Beta between stock and market
# rm = expected return of the market
# rm - rf = equity risk premium

#how much should the risk premium that the investor would expect be? 
#it has to be related to the amount of risk (Beta) he's willing to accept.


# In[26]:


#CAPM example: PG
# rf = approximate with 10Y US government bond yield (2.5%) = this is the closest you can get to risk-free in reality
# this is also known as the 10Y Treasury Yield (bloomberg website, "united states rates & bonds" gives accurate data)
#but in a real ecnonomy, absolute risk-free does not exist, hence 10Y US government bond yield is used.
# Beta_PG_S&P500 = 0.62 #this was calculated earlier
#however if we were using a UK security, then we should calculate the Beta for UK security and FTSE100
#it is important that we calculate the Beta for the security with the market of the security's home country.
# rm - rf = 4.5-5.5% = equity risk premium
#academic research has proven the market risk premium for equities in the U.S. has been between 4.5% and 5.5% /
#and practitioners typically use one of these values or simply 5% which is in between.
# ri = rPG = expected return of PG

# ri = 2.5% + 0.62(5%) = 5.6%

#When an investor buys PG shares he would expect to earn 5.6% as a compensation for the risk he's taking.


# In[28]:


#Calculating the expected return of PG (CAPM):
PG_er = 0.025 + PG_Beta*0.05
PG_er


# In[29]:


# Introducing Sharpe Ratio and how to put it into practice:
#rational investors want to minimize their risk and hence invest in less volatile securities. therefore they need a /
#measure of risk-adjusted return. rational investors like to compare stocks based on risk-return performance.
#in other words they would like the highest return for a given amount of risk.

# Sharpe Ratio is a great way to make a proper comparison between stocks and portfolios and decide which one is /
#preferable in terms of risk and return.

# Sharpe Ratio = (ri - rf) / (std of i)

# ri = security's expected return = ith return
# rf = return of risk-free asset
# std of i = standard deviation of stock
# ri - rf = Excess return of stock

#this allows us to understand if an investment fund (stock/portfolio) is satisfactory on a risk adjusted basis 


# In[31]:


#Obtaining the Sharpe Ratio in python:
Sharpe_Ratio = (PG_er - 0.025) / (sec_returns['PG'].std()*250**0.5)
Sharpe_Ratio


# In[32]:


# Measuring Alpha and verifying how good or bad a Portfolio Manager is doing:

#Alpha is the intercept of the CAPM
# the standard CAPM assumes an Alpha of zero, that is why it was not included in the formula previously
# CAPM formula with alpha becomes: ri = Alpha + Beta_im(rm - rf)
# a good portfolio manager outperforms the market and earns a positive Alpha
# a poor portfolio manager underperforms the market and earns a negative or zero Alpha

#for an investment manager to outperform the market, they require:
# Industry knowledge
# Company-specific information
# Trading know-how

#outperforming the market requires hand-picking successful investments; long-term investments. 
# Passive investment: investing in a market index (S&P 500) and waiting patiently
# Active investment: adjusting investment portfolios on a frequent basis, hence investor will be taking advantage of /
#short-term price changes. Buy low, Sell high. Active trading time horizon: 1 day to Months
#active trading is the basis on which investment professionals justify their fees.
#If an investment professional charges you 1% of the invested amount he needs to outperform the market by over 1% /
#otherwise you'd be better off investing in a passive fund that charges you small portion of the invested income.

#Comparing Investments: we can only compare the Alpha of investments with a similar risk profile.
#only 2% of funds have a positive Alpha that is consistently different than zero. This has caused an important trend /
#in the investment industry where most investors know that well diversified and passive index tracking funds e.g. /
#S&P 500 charging low fees are very efficient and started to consider them as a solid alternative to active /
#management strategies.
#William Sharp believes investors should bet on the efficiency of markets and avoid paying high management fees.

#in conclusion: Alpha tells us how much return we get, without bearing extra risk


# In[1]:


########################## Section 16: Part II Finance: Multivariate Regression Analysis ############################


# In[2]:


#by considering more variables in the regression equation will improve its explanatory power and provide a better /
#idea of the full picture of circumstances that determine the development of the variable we are trying to predict.
#an example would be the house price variables discussed earlier (size, location, number of rooms, neighbourhood).
#Therefore a regression that considers multiple variables should provide predictions closer to true results.
#we need the right variables otherwise results could be misleading.

#Simple Regression: a single Beta coefficient and explanatory variable
#Multivariate Regression: multiple Beta coefficients and explanatory variables. hence we are calculating a best /
#fitting line across multiple dimensions. If the independent variables are more than two things become complicated /
#if they are three you can use a sophisticated three dimensional graph.

#R squared measurement will help us determine how powerful the regression we've obtained is. R-squared can be /
#from 0 to 1 and the more variables we include in the equation the higher we would expect it to be.

#There are two main ways to check if an explanatory variable is helpful:
#First we can run a regression with the variable and then run a new regression without that variable or with a /
#different variable.
#We should observe how r squared changes if it is higher the first time than this independent variable has good /
#explanatory power and its value contributes to the explanation of the value of the dependent variable.
# Or we can compare the P-value of Beta coefficients (probability that Beta coefficients should have been different)
#Low P-value: there is a low chance that the Beta coefficients are different than estimated
#So a low P value is a good thing. It provides assurance that the real beta coefficient differs from zero and /
#helps us explain the dependent variable.
#P-value that is lower than 5% allows us to state we can be 95% confident that the Beta coefficient we've estimated /
#is different than 0 
#practitioners accept P-values that are lower than 5% or if more conservative lower than 1%.

#beta coefficients estimated in a multivariate regression can still be interpreted as the marginal impact that an /
#explanatory variable has on the dependent variable. But this is only true if all other explanatory variables /
#remain constant.

#Multivariate Regression Formula: Yi = Beta_0 + Beta_1*X_1 + Beta_2*X_2 + Beta_i*X_i + explanatory_variable

# example: Yi = Beta_0 + 0.8.GDP% + 1.2*Industry_Growth% + explanatory_variable
#for every % increase of GDP growth the company will be expected to earn 0.8% more if the expected industry growth /
#remains the same. The expected return and the GDP growth are interrelated in this regression and we cannot /
#interpret one without the other.


# In[3]:


# Running a Multivariate Regressio in Python:
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt


# In[4]:


data = pd.read_excel('Desktop/Python/Housing.xlsx')


# In[5]:


data


# In[6]:


#independent variables: House Size (sq.ft.), Number of Rooms, Year of Construction


# In[7]:


X = data[['House Size (sq.ft.)', 'Number of Rooms', 'Year of Construction']] #2 brackets since X is multi-dimensional
Y = data['House Price']


# In[10]:


X1 = sm.add_constant(X)
reg = sm.OLS(Y,X1).fit()
reg.summary()


# In[ ]:


#all the p-values are above 5% in the above table, hence the 3 coefficients are not statistically significant.


# In[11]:


#independent variables: House Size (sq.ft.), Number of Rooms


# In[12]:


X = data[['House Size (sq.ft.)', 'Number of Rooms']]
Y = data['House Price']


# In[13]:


X1 = sm.add_constant(X)
reg = sm.OLS(Y,X1).fit()
reg.summary()


# In[14]:


#independent variables: House Size (sq.ft.), Year of Construction


# In[15]:


X = data[['House Size (sq.ft.)', 'Year of Construction']]
Y = data['House Price']


# In[16]:


X1 = sm.add_constant(X)
reg = sm.OLS(Y,X1).fit()
reg.summary()


# In[17]:


#independent variables: Number of Rooms, Year of Construction


# In[18]:


X = data[['Number of Rooms', 'Year of Construction']]
Y = data['House Price']


# In[19]:


X1 = sm.add_constant(X)
reg = sm.OLS(Y,X1).fit()
reg.summary()


# In[20]:


#an experienced researcher runs hundreds of regressions before making a sound inference. 
#we ran as many regressions as possible in the code above.

# When we skim through the values in the new output we can see year of construction does not get a low P-value in /
#any of the two regressions it has been involved in, this means it is not related to house prices 

#The P-value for number of rooms and house size is practically zero which is amazing. When we run a regression with /
#only these two variables "size" and "number of rooms" there are P-alues increase significantly.
#So we cannot confirm they can influence the price of a house

#at this stage even if we cannot make a firm conclusion, these results can give us good guidance for future research.
# our output suggests that if we gather more data about more observations house size or number of rooms might prove /
#to be good indicators of house prices and their p value will probably decrease in the regressions we will run.
#How come? Well in our calculations the value of the R-squared was high. This gives us confidence that in general /
#we have gathered a good set of explanatory variables. So it might not be necessary to change the set.
# In addition there could be a problem among these three explanatory variables most probably house size and number /
#of rooms are related and they act as a single explanatory variable. This means they are the same factor. 
#Hence we should gather data about other types of explanatory variables

# regressions can give us a good direction for future research following such direction could help us assess /
#whether a certain factor influences the phenomenon we are trying to explain.
# Furthermore regression analysis can be invaluable when we study the past to understand the future behaviour of /
#financial assets like stocks.


# ################## Section 17: Part II Finance: Monte Carlo simulations as a decision-making tool ###################

# In[ ]:


#When we run a Monte-Carlo simulation we are interested in observing the different possible realizations of a future /
#event. What happens in real life is just one of the possible outcomes of any event. with Monte Carlo we can use /
#past data to create a simulation; a new set of fictional but sensible data. These realisations are generated by /
#observing the distribution of the historical data and calculating its mean and variance.
#The simulation would be a larger data set, it will have a good proxy of different outcomes, it will be used in a /
#number of situations. This will help us make an informed decision.
#Monte-Carlo simulations are used in corporate finance, investment valuation, asset management, risk management, /
#estimating insurance liabilities, pricing of options and other derivatives.
#the large level of uncertainty in finance makes Monte-Carlo a valuable tool that improves the decision making /
#process when several random variables are in play.


# In[3]:


#Monte Carlo applied in Corporate Finance context:
#Finance managers face many unknowns in their work. They must forecast the development of revenues. Costs of goods /
#sold and operating expenses and each value is affected by many factors whose behaviour could be considered random.

# Current Revenues = Last Year Revenues * (1 + YearOnYear Growth Rate)

#the random variable here is the Y-O-Y growth rate, and through 1000s of simulations of growth rate we can get an /
#idea of average, maximum and minimum values. This can help finance manager understand where revenues are heading.

# Revenue Growth Rate and Revenue Volatility can be obtained by:
# i) Historical Data
# ii) User Intuition

#COGS = cost of goods sold = modeled as a percentage of revenues
#OpEx = operating expense = modeled as a percentage of revenues

#COGS and OpEx depend on the revenues the firm makes. If revenues are low there will be no need to spend a lot for /
#cost of goods sold as fewer products will be produced.

# Revenue - COGS = Gross Profit 

# Gross Profit - OpEx = Operating Profit


# In[4]:


# Monte Carlo: Predicting Gross Profit: Part I
import numpy as np
import matplotlib.pyplot as plt


# In[5]:


rev_m = 170 #revenue mean
rev_stdev = 20
iterations = 1000 #we will produce 1000 simulated observations from a normal distribution.


# In[6]:


rev = np.random.normal(rev_m, rev_stdev, iterations) #this is NumPy's random Normal Distribution generator
rev #most of the value should be close to the mean value "170" we selected.
#we now have 1000 revenue data points


# In[8]:


plt.figure(figsize=(15, 6))
plt.plot(rev)
plt.show() #all the data falls between 150 (mean + stdev) and 190 (mean - stdev). we rarely observe scenarios /
#outside of these limits.


# In[10]:


#what is the impact for cost of goods sold? COGS amount to 60% (0.6) of company's revenues. normal distribution with a /
#mean of 60% of revenues and the estimation of 60% will have a standard deviation of 10% (0.1)
COGS = - (rev * np.random.normal(0.6, 0.1)) #we put a minus sign because COGS is money spent
#the code above is the multiplication of revenues by 60%
#We have also assigned a random COGS value to each one of the 1000 revenue data points.
#This is why the revenue value we obtained must be multiplied by a value extracted from a random normal distribution /
#with a mean of 0.6 and a standard deviation of 0.1 (this allows the value to alternate up and down by 10%).
plt.figure(figsize=(15, 6))
plt.plot(COGS)
plt.show()


# In[11]:


COGS.mean()


# In[13]:


COGS.std()


# In[14]:


#if you re-run the COGS approximation you will not always get the same mean value of the observations. They could be /
#dispersed around 80 90 100 or 110 and this will be fine. What is important is that every time the deviation of /
#COGS will be around 10% of its mean


# In[16]:


#Monte Carlo: Predicting Gross Profit: Part II
#such analysis that can help a finance manager predict future revenues costs and margins.
Gross_Profit = rev + COGS #we used a plus sign because COGS has already been calculated with a minus in front of it
Gross_Profit

plt.figure(figsize=(15, 6))
plt.plot(Gross_Profit)
plt.show()


# In[19]:


max(Gross_Profit)


# In[20]:


min(Gross_Profit)


# In[21]:


Gross_Profit.mean()


# In[22]:


Gross_Profit.std()


# In[23]:


plt.figure(figsize=(10, 6))
plt.hist(Gross_Profit, bins = [40,50,60,70,80,90,100,110,120]);
plt.show()


# In[24]:


plt.figure(figsize=(10, 6))
plt.hist(Gross_Profit, bins = 20); #the graph should be smoother because now instead of 9 bins, we have 20 bins
plt.show()


# In[25]:


#There are two ways to use Bins. One way is to create a list whose elements separate the bins along the x axis.
#If our list contains the numbers 40 50 60 and so on until 120 then we will see observations between 40 and 50 /
#grouped in one bin between 50 and 60 grouped in another and so on. Here the bins are too big and it is hard to /
#agree our data was normally distributed. The alternative procedure is to assign the number of bins directly.
#If I ask for 20 bins the computer will automatically split my data into 20 equal intervals and this time it will be /
#obvious the numbers are normally distributed.


# In[1]:


# Forecasting Stock Prices (asset pricing) with a Monte Carlo Simulation:

# Price Today = Price Yesterday * e^r
# r = log return of share price between yesterday and today = ln(price_today/price_yesterday)
#remember: e^log(x) = x
#this allows us to depict today's stock price as a function of yesterday's stock price and the daily return we'll have

#we know yesterday's price, however we do not know "r", as it is a random variable.
#we can use "Brownian Motion" in order to model "r". Brownian motion is a concept that would allow us to model /
#such random-ness (r is a random variable).


# In[2]:


#Brownian Motion: The formula we can use is made of 2 components:
# i) Drift: this is the direction that rates of return have been headed in the past
# ii) Stock's volatility: this is a random variable

#Drift [ln(current_price/previous_price)] is the best approximation about the future we have. First we'll start by /
#calculating the stocks periodic daily returns over the historical period. We only have to take a natural logarithm /
#of the ratio between current and previous price.
#Once we have calculated daily returns in the historical period we can easily calculate their average standard /
#deviation and variance.

#Formula for Drift becomes: Drift = Average Daily Return - 0.5(variance) = expected daily return of the stock

#We recognize historical values are eroded in the future. Hence a random component is included; 0.5 times the variance

# the second component of Brownian Motion is "Stock's Volatility" (random variable):
# this is expressed as: Random Variable = Historical_Volatility * Z (of a Random number between 0 and 1)

# Random Variable = Stock's_Historical_Volatility * Z(Rand(0;1))

#this random number from 0 to 1 is a percentage
#If we assume expected future returns are distributed normally Z of the percentage between 0 to 1 would give us the /
#number of standard deviations away from the mean.
#So for example the distance between the mean and events with a probability of less than 99.7% is /
#3 standard deviations. This is how we can determine the variable component of the Brownian motion.

# Hence the equation for the Stock Price of Today becomes:

# Price Today = Price Yesterday * e^(Drift+Stock's_Volatility)
# Price Today = Price Yesterday * e^((AverageDailyReturn-0.5(variance))+(Stock's_Historical_Volatility*Z(Rand(0;1))))

#If we repeat this calculation 1000 times we'll be able to simulate the development of tomorrow's stock price and /
#assess the likelihood it will follow a certain pattern.
#In addition this is a great way to assess the upside and the downside of the investment as we've obtained an /
#upper and lower bound when performing the Monte-Carlo simulation.


# In[3]:


#Monte Carlo - Forecasting Stock Prices in python: Part I
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
from scipy.stats import norm
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


ticker = ['PG']
data = pd.DataFrame()
data[ticker] = wb.DataReader(ticker, data_source='yahoo', start='2007-1-1')['Adj Close']


# In[5]:


log_returns=np.log(1 + data.pct_change()) #pandas.pct_change() = this is percent change. obtains simple returns from /
#a provided dataset


# In[6]:


log_returns.tail()


# In[7]:


data.plot(figsize=(10,6));


# In[8]:


log_returns.plot(figsize=(10,6)); #the graph tells us that the returns are normally distributed and have a stable mean


# In[9]:


#we'll do this entire exercise without annualizing our indicators. since we are predicting PG's daily stock price
u = log_returns.mean()
u


# In[10]:


var = log_returns.var()
var


# In[11]:


drift = u - (0.5*var) #Drift is the best approximation of future rates of return of the stock.
drift


# In[12]:


stdev = log_returns.std()
stdev


# In[13]:


# Brownian Motion: r = drift + stdev * e^r
#we have now set up the first component of the Brownian Motion, now we will create the second component


# In[ ]:


#Monte Carlo - Forecasting Stock Prices in python: Part II


# In[14]:


type(drift) #the drift is series type, we need to convert it to NumPy Array type.


# In[15]:


type(stdev) #the stdev is series type, we need to convert it to NumPy Array type.


# In[16]:


np.array(drift)


# In[17]:


drift.values #object.values transfers the object into a Numpy Array. this does same job as np.array(object)


# In[18]:


stdev.values #object.values transfers the object into a Numpy Array. this does same job as np.array(object)


# In[19]:


#The second component of the Brownian motion is a random variable "Z" a number corresponding to the distance between /
#the mean and the events expressed as the number of standard deviations. SciPy's norm.ppf allows us to obtain this
norm.ppf(0.95) #the result below implies that If an event has a 95% chance of occurring the distance between this /
#event and the mean will be 1.65 standard deviations:


# In[20]:


x = np.random.rand(10, 2) #To complete the second component we will need to randomize. the well-known NumPy Rand /
#function can help us do that easily if we want to create a multi dimensional array. 10 & 2 means it's a 10by2 matrix.
x


# In[21]:


norm.ppf(x) #We will include this random element within the distribution to obtain the distance from the mean /
#corresponding to each of these randomly generated probabilities. e.g. the first number 1.531 corresponds to the /
#first number in the matrix above; 0.937


# In[22]:


Z = norm.ppf(np.random.rand(10, 2)) #The newly created array use the probabilities generated by the random function /
#and converted them into distances from the mean zero as measured by the number of standard deviations.
Z


# In[24]:


#now let's forecast the stock prices for the next 1000 days:
t_intervals = 1000
iterations = 10 #we will ask the computer to produce 10 series of future stock price predictions.
# the time intervals and iterations will specify the dimensions of the array filled with values from 0 to 1.


# In[34]:


# a reminder: 
# Daily Returns = e^r 
# r = drift + stdev * z
daily_returns = np.exp(drift.values + stdev.values * norm.ppf(np.random.rand(t_intervals, iterations)))
#using t_intervals and iterations will give us 10 columns and 1000 rows in our array below
daily_returns


# In[35]:


#So the formula we used in the previous cell would allow us to obtain a 1000 by 10 array with daily return /
#values; 10 sets of 1000 random future stock prices.


# In[36]:


#Monte Carlo - Forecasting Stock Prices in python: Part III


# In[37]:


#at this stage we need to create a price list. Each prize must equal the product of the price observed the previous /
#day and the simulated daily return. once we obtain the price and date t we can estimate the expected stock price /
#we will have in day t plus one:

# S(t) = S(0) * daily_return(t)   

# S(t+1) = S(t) * daily_return(t+1)

# S(t+999) = S(t+998) * daily_return(t+999)

#Then this process will be repeated 1000 times and we will obtain a prediction of a company's stock price 1000 days /
#from now.


# In[38]:


#we have already calculated the daily_returns variable. but what is our first stock price in the list [S(0)]?
# The first stock price in our list must be the last one in our data set. It is the current market price.
#we call this variable zero as it contains the stock price today at the starting point; Time Zero.
#With the help of the ILO method and the index operator we can indicate we need the last value from the table by /
#typing minus one within the brackets:
S0 = data.iloc[-1]
S0


# In[39]:


#Let's proceed with filling in the list. How big should it be? as big as the daily returns array.
#the price list Matrix could be at most as big as the daily returns matrix (1000 rows 10 columns, 1000 by 10 matrix)
#NumPy has a method that can create an array with the same dimensions as an array that exists and that we have /
#specified, this method is called zeros like:
price_list = np.zeros_like(Daily_returns) #argument will be the daily returns array. We will obtain an array of 1000 /
#by 10 elements just like the dimension of daily returns and then fill it with zeros.
price_list


# In[40]:


#So why did we create this object? Well now we can replace these zeros with the expected stock prices by using a loop.


# In[41]:


#First we must set the first row of our price list to S0. Not just the first value but the entire row of 10 elements /
#because S0 will be the initial price for each of the 10 iterations we intend to generate.
price_list[0] = S0
price_list


# In[ ]:


#We must set up a loop that begins in day 1 and ends at day 1000. We can simply write down the formula for the /
#expected stock price on date t in Pythonic it will be:

# S(t) = S(t-1) * daily_returns(t)


# In[43]:


for t in range (1, t_intervals):
    price_list[t] = price_list[t-1] * daily_returns[t]


# In[44]:


price_list


# In[46]:


#the price list has been completed. The matrix shows 10 possible paths (iterations) of the expected stock price, /
#starting from the last day (last value from the table, S0). This is best presented in a graph:
plt.figure(figsize=(10,6))
plt.plot(price_list);


# In[47]:


# An introduction to Derivative Contracts:
#a derivative is a financial instrument, whose price is derived based on development of 1 or more underlying assets
#example of these assets include: Stocks, Bonds, Interest Rates, Commodities, Exchange Rates
#it is a contract involving at least 2 parties describing how and when they will exchange payments.

# Trading Derivatives:
# i) some are traded in "Regulated Markets": a uniform contractual structure, and are much simpler to understand
# ii) some are traded in "Over The Counter Markets"

#Originally derivatives served as hedging instruments. companies interested in buying these contracts were mostly /
#concerned about protecting their investment. So if a business owner sold some of his goods in pounds £ and received /
#payments in three months time he would be more than willing to buy a derivative contract that allowed him to /
#exchange pounds in three months for dollars $ today, locking the revenues he would receive from the sale today.

#new types of derivatives have been developed as a result of financial engineering.

#there are 3 types of people dealing with Derivatives:
# i) Hedging: people who want to hedge their investments
# ii) Speculating
# iii) Arbitrageurs: traders interested in finding pricing discrepancies and profiting from these assuming no risk 

# There are 4 main types of financial Derivatives:

# i) Forwards: 2 parties agree that 1 party will sell to the other an underlying asset at a future point of time.
#the price of the asset is agreed beforehand.

# ii) Futures: these are highly standardised Forward contracts typically stipulated in a marketplace (an Exchange).
# Futures require participation of a clearinghouse. The transaction goes through the marketplace and the /
#counter-parties do not know each other.

# iii) Swaps: 2 parties agree to exchange cash flows based on an underlying asset at a future point of time.
# The underlying asset can be an interest rate, stock price, a bond price, a commodity price and so on.
#The most widely used swap contracts are Interest rate swaps. one party agrees to receive a cash flow based on a /
#fixed interest rate while the other agrees to receive a cash flow based on a floating interest rate.
# e.g. if underlying asset is £100k and fixed rate (for me) is 5%, on settlement date the floating rate could be 6% / 
# then at this point i owe the counterparty £5k and they owe me £6k, so net sum would be £1k payment to me.

# iv) Options: an option contract enables its owner to buy or sell an underlying asset at a given price. Also known /
#as strike price. option contracts can be exercised until a certain date called maturity date. options that involve /
#buying an asset are called call options while options based on the sale of an asset are called put options. 
#European options can be exercised only at maturity while American options may be exercised at any time.
#The owner of the option contract may buy or sell the get at the given price but he may also decide not to do it.


# In[48]:


# Black Scholes Formula = an important tool for Derivatives Pricing:

#The original framework developed by the three scientists consider the pricing of a European call or put option /
#and assumed efficient markets, absence of transaction costs, no dividend payments, known volatility & risk free rate
#Some of these hypotheses can be relaxed to calculate an options price in practice.

#So what does the black Sholes formula do? It calculates the value of an option
#Call Option: If the strike price is less than market price the owner of the option will exercise it and buy the /
#share. however if the strike price is higher than the market price he won't exercise the option, he can buy the /
#shares cheaper in the market


# In[49]:


# Black Scholes Formula (for a call option):

# C(S,t) = N(d1)S - N(d2)ke^(-r(T-t))

# d1 = [1/(s*SQRT(T-t))]*[ln(S/K)+(r+(s^2)/2)*(T-t)]
# this shows us how much we are going to get if the option is exercised
#We are multiplying the probability of exercising the option by the amount received when the option is exercised

# d2 = d1 - s*SQRT(T-t)
# this is the amount we must pay when exercising the option.
#here we have the discounted value of the amount we must pay to exercise the option.

# S = current stock price
# K = option strike price
# t = time until option expires
# r = risk-free interest rate
# s = sample standard deviation
# N = standard (cumulative) normal distribution
# e = exponential term
# C = call premium
# T = time horizon measured in years

#All this is done if the development of the stocks share price follows a normal distribution.

# Black Sholes formula calculates the value of a call by taking the difference between the amount you get if you /
#exercise the option minus the amount you have to pay if you exercise the option.

#sometimes the (T-t) is replaced by (t). read further to find out why.


# In[52]:


#Monte Carlo: Black Scholes Merton in python.
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
from scipy.stats import norm


# In[53]:


#when we multiply the contents inside d1 and d2, it becomes:

# d1 = [ln(S/K) + ((r) + (stdev^2)/(2))*2] / [s*SQRT(t)]

# d2 = d1 - s*SQRT(t) = [ln(S/K) + ((r) - (stdev^2)/(2))*2] / [s*SQRT(t)]

def d1(S, K, r, stdev, T): #the formula parameters must be expressed
    return (np.log(S/K) + (r + stdev**2/2)*T) / (stdev * np.sqrt(T))

def d2(S, K, r, stdev, T):
    return (np.log(S/K) + (r - stdev**2/2)*T) / (stdev * np.sqrt(T))


# In[54]:


norm.cdf(0) #cumulative normal distribution: cdf = cumulative distribution function; shows us how data accumulates /
#in time. it's output can never be below 0 or above 1. 0 is the first point and 1 is the last point on the graph
#norm.cdf take as an argument a value from the data and will show us what portion of the data lies below that value.
# in this case the argument is zero, centre of normal distribution curve. For instance an argument of zero will /
#lead to an output of zero point five. Since 0 is the mean of the standard normal distribution and half the data /
#lies below this value


# In[55]:


norm.cdf(0.25)


# In[57]:


norm.cdf(0.75)


# In[58]:


norm.cdf(9) #an argument of 9 gets value of 1 because it is expected to be the largest data point in our set


# In[59]:


#we can now itroduce the Black Scholes Merton (BSM) formula:

# C = S*N(d1) - K(e^(-rt))*N(d2)

def BSM(S, K, r, stdev, T):
    return (S*norm.cdf(d1(S, K, r, stdev, T))) - (K*np.exp(-r*T)*norm.cdf(d2(S, K, r, stdev, T)))
#This is an example of how we can use a function within another function (d1 and d2 in BSM).


# In[63]:


ticker = ['PG']
data = pd.DataFrame()
data[ticker] = wb.DataReader(ticker, data_source='yahoo', start='2007-1-1', end='2019-8-18')['Adj Close']


# In[64]:


#now lets get the current stock price:
S = data.iloc[-1]
S


# In[65]:


log_returns=np.log(1 + data.pct_change()) #since the behavior of a single stock throughout a given period is of /
#interest estimating log returns will be appropriate.


# In[67]:


stdev = log_returns.std() * 250 ** 0.5
stdev
#professionals usually apply certain formulas or as they say interpellation is to compute this value. In our case we /
#will use an approximation; the standard deviation of the logarithmic returns of this stock


# In[68]:


#We can now calculate the price of the call option:
r = 0.025 #We will stick to a risk free rate of 2.5% corresponding to the yield of a 10 year government
K = 110.0 #let's assume the strike price equals $110
T = 1 #let's assume the time horizon is 1 year


# In[69]:


d1(S, K, r, stdev, T)


# In[70]:


d2(S, K, r, stdev, T)


# In[72]:


BSM(S, K, r, stdev, T) #this will give us the Call Option Price
##The value of the option depends on multiple parameters such as strike price, time to maturity and volatility. It /
#is not directly proportional to the price of the security 
#Professionals implement a lot more complicated mathematical formulas and loops to specify the call within a /
#millionth of its value because when investing tens of millions infinitesimal differences matter.


# In[73]:


#How can you use a Monte Carlo simulation when applying the Black-Scholes-Merton formula for calculating future /
#outcome? when randomly generating future stock prices


# In[87]:


# Monte Carlo: Euler Discretisation: Part I
#we will compute the price of a call option in a more sophisticated way regarding the previous lecture.
#with this new approach, the method and the formulas we will apply to compute the call option price are different:
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
from scipy.stats import norm
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[88]:


ticker = ['PG']
data = pd.DataFrame()
data[ticker] = wb.DataReader(ticker, data_source='yahoo', start='2007-1-1', end='2019-8-18')['Adj Close']


# In[89]:


log_returns=np.log(1 + data.pct_change())


# In[90]:


#Earlier we use the standard formula for calculating the price of a call option. However as a financier you would /
#like to run thousands of experiments to be sure the price you pick will be the most accurate one. Monte-Carlo /
#simulations can provide us with thousands of possible call option prices. Then we could average the pay off/
#associated to these randomly generated values and discount it back to today. The trick lies in the formula we will /
#use to calculate the future prices.

#It will be another version of a Brownian motion and approximate formula and the approach employed will be called /
#Euler Discretization: 

# S(t) = S(t-1) * e^[(r - stdev**2/2)*(DeltaT)+ stdev*SQRT(DeltaT)*Z(t)]

# (T-t) = DeltaT = fixed time interval component
# Z(t) = random component


# In[91]:


r = 0.025


# In[92]:


stdev = log_returns.std() * 250 ** 0.5
stdev


# In[93]:


type(stdev)


# In[94]:


stdev = stdev.values #we do this to turn it from series to array, we need it in array for later calculations
stdev


# In[95]:


T = 1.0 #time horizon of 1 year
t_intervals = 250 #number of the time intervals must correspond to the number of trading days in a year.
delta_t = T / t_intervals
iterations = 10000 #number of times we want to simulate the random component.


# In[97]:


#The random component Z will be a matrix with random components as drawn from a standard normal distribution which /
#as already mentioned implies a normal distribution with mean 0 and standard deviation of 1. The dimension of the /
#matrix these values will occupy will be defined by the number of time intervals augmented by 1 and the number of /
#iterations:
Z = np.random.standard_normal((t_intervals + 1, iterations))
S = np.zeros_like(Z) #creates an empty array s of the same dimension as the random component Z
S0 = data.iloc[-1] #to fill its first row with the last available stock price data for PG
S[0] = S0


# In[98]:


#We loop from 1 to the number of time intervals plus 1 and we create a whole stock price matrix with the dimension /
#of the time intervals plus 1 to the number of iterations; more precisely 250 plus 1 equals 251 and we have /
#10,000 iterations. So the dimension of this matrix is 251 rows to 10,000 columns
for t in range (1, t_intervals + 1):
    S[t] = S[t-1] * np.exp((r - 0.5 * stdev**2) * delta_t + stdev * delta_t ** 0.5 * Z[t])


# In[100]:


S


# In[99]:


S.shape


# In[101]:


#to plot only ten simulations we can use a matplotlib trick, after we specify we would like to plot S, we could /
#add an index operator where we designate all the 250 time intervals that must be plotted by typing a colon before /
#the comma. since we are not willing to see all 10000 potential tracks we can limit the graph to the first 10 /
#iterations we have generated by writing colon 10
plt.figure(figsize=(10,6))
plt.plot(S[:, :10]);


# In[102]:


# Monte Carlo: Euler Discretisation: Part II


# In[103]:


#how is the payoff of a call option calculated? you will exercise your right to buy the option if the stock price /
#minus the strike price is a positive number and you will not exercise your right to buy. So the value of the option /
#depends on the chance the stock price minus the strike price will be a positive difference. and in particular how /
#positive it is expected to be.
#the numpy.maximum() method will create an array that contains either 0s or the numbers equal to the differences 
#hence the Payoff is calculated as:
p = np.maximum(S[-1] - 110, 0)
p


# In[104]:


p.shape #the answer should be the same length as the S-matrix (10,000)


# In[105]:


#formula to discount the average of this payoff is:

# C = [(e^(-rT))*sigma(Pi)] / iterations

# sigma(Pi) = sum of the computed payoffs
# e^-rT = exponential discounting with a math component


# In[106]:


C = np.exp(-r * T) * np.sum(p) / iterations
C


# In[ ]:


#we successfully obtained the price of a call option. the price of call option we obtained earlier with BSM was /
#15.168994, which is not significantly different to the value we obtained with the new method 15.04688....
#This is proof of the choice of the computation methods can lead to insignificant but not unimportant differences /
#in the outcome.

