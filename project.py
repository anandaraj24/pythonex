#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Question 1:
def print_N_nos(x):
    for i in range(1,x+1):
        if i%3==0:
            print("Fizz")
        else:
            print(i)
            


# In[2]:


#Question 2:
list1=[1,2,3,5,8,4,7,9,1,4,12,5,6,5,2,1,0,8,1]
i=len(list1)-1
while i>=0:
        result=list1[i]
        print(result,"-",list1.count(result))
        i-=1
        


# In[3]:


#Question 2 (Alternate method):
from collections import Counter
Counter(list1)


# In[4]:


#Question 3:
dict1={"Rick":85,"Amit":42,"George":53,"Tanya":60,"Linda":35}
sum(dict1.values())


# In[27]:


#Question 4:
score=[1,2,2,3,2,0,2,3,4,0,1,1,2,6,3,2,2,6]
def Stats(overs):
    print("The total runs Score in {} overs is : {}".format(int(len(overs)/6),sum(overs)))
    for i in score:
        print("The total score in 1st over is:",sum(score[0:6]))
        print("The total score in 2nd over is:",sum(score[6:12]))
        print("The total score in 3rd over is:",sum(score[12:]))
        #Assuming batsman 1 plays 1st over and rotates the strike to batsman 2 who plays 2nd over and again batsman 1 plays 3rd over
        print("Batsman 1 scored {} runs".format(sum(score[0:6])+sum(score[12:])))
        print("Batsman 2 scored {} runs".format(sum(score[6:12])))
        break


# In[28]:


Stats(score)


# In[ ]:




