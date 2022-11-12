#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import 
import pandas as pd
import re
import os


# In[2]:


#check the working directory
os.getcwd()


# In[3]:


#change the working directory
os.chdir('E:\\下载\\project\\GOT\\script\\S1')


# In[4]:


#reconfirm
os.getcwd()


# In[5]:


#webdata scraping

#import
import requests
from bs4 import BeautifulSoup

#get url
url = "https://genius.com/1639510"

#getting response object
res=requests.get(url)
 
#Initialize the object with the document
soup = BeautifulSoup(res.content, "html.parser")
 
#Get the whole page
page = soup.html
 
#Print each string recursively
for string in page.strings:
    print(string)


# In[6]:


#save the webpage as text file
f_test=open("S1E1.txt","w", encoding='utf-8') 

for string in page.strings:
    f_test.write(string)

f_test.close()


# In[7]:


#open the script
with open("S1E1.txt",encoding='utf-8',errors='ignore') as f:
         data = f.read()
#print the data(if applicable) 
#print(data)


# In[8]:


#data cleaning: remove the inequivalent contents

#type the "[begining]" and the "[ending]" between the content we want(edit directly in txt file)
#remove the text above "[begining]"
data = data.split('[begining]')[1]
#print the data(if applicable) 
#print(data)


# In[9]:


#remove the text below "[ending]"
data = data.split('[ending]')[0]
#print the data(if applicable) 
#print(data)


# In[10]:


#get rid of the "-" in the script
data = data.replace('-', '')
#print the data(if applicable) 
#print(data)


# In[11]:


#remove all the blank lines in the script
regex = r"^\s+$"
subst = ""
data = re.sub(regex, subst, data, 0, re.MULTILINE)

regex = r"^$\n"
subst = ""
data = re.sub(regex, subst, data, 0, re.MULTILINE)

#print the data(if applicable) 
#print(data)


# In[12]:


#save the cleaned script for later use of wordcloud
f_2=open("word_cloudS1E1.txt","w", encoding='utf-8') 
f_2.write(data)
f_2.close()


# In[13]:


#split the lines by the line changing mark
lines = data.split('\n')
#print the data(if applicable) 
#print(data)


# In[14]:


#number the lines
myrows = []

num = 1
for line in lines:
    myrows.append([num, line])
    num = num + 1
#check whether the lines have been successfully splited and numbered
myrows[:10]


# In[15]:


#turn the numbered and splited lines into dataframe
df = pd.DataFrame(myrows)
df.head()


# In[16]:


#name the column
df.columns = ['line', 'text']
df.head()


# In[17]:


#save the data frame to csv.file
df.to_csv('dataS1E1.csv', index=False,encoding='utf-16')

