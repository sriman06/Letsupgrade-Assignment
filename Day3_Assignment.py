#!/usr/bin/env python
# coding: utf-8

# # Question 1
# 
# Write a Python program to remove duplicates from a list

# In[1]:


l1 = [1,2,3,4,3,4,11,2,3]


# In[2]:


# Remove duplicates
new_list =[]
for ele in l1:
    if ele in new_list:
        pass
    else: new_list.append(ele)


# In[3]:


new_list


# # Question 2
# Write a Python program to get the difference between the two lists
# 
# 

# In[5]:


list1 = ['a', 'b', 'c', 'd', 'e', 'f']
list2 = ['a', 'c', 'e', 'g', 'h', 'k']


# In[ ]:





# In[8]:


diff = []
for ele in list1: 
    if ele in list2:
        pass
    else:
        diff.append(ele)


# In[9]:


diff


# 
# # Question 3
# Write a Python program to get the frequency of the elements in a list

# In[14]:


list_1 = [1, 1, 2, 3, 4, 5, 5,3,1]
# Convert the list to set
set0 = set(list_1)
# For each unique element for set, count elements in the list to get frequency
for ele in set0: print(ele,"-",list_1.count(ele))


# # Question 4
# Write a Python program to compute the similarity between two lists.
# 
# Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
# 
# Expected Output: Color1-Color2: ['white', 'orange', 'red'] Color2-Color1: ['black', 'yellow']

# In[15]:


Color1 = ["red", "orange", "green", "blue", "white"]
Color2 = ["black", "yellow", "green", "blue"]

diff = []
for ele in Color1: # list1 - list2
    if ele in Color2:
        pass
    else:
        diff.append(ele)
print("Color1-Color2:",diff)

diff = []
for ele in Color2: # list1 - list2
    if ele in Color1:
        pass
    else:
        diff.append(ele)
print("Color2-Color1:",diff)


# # Question 5
# Write a Python function that takes a list of words and returns the length of the longest one

# In[16]:


def longest_one(list):
    longest_one = ""
    for ele in list:
        if len(ele) > len(longest_one):
            longest_one = ele
        else: pass
    return longest_one

Color1 = ["red", "orange", "green", "blue", "white"]
Color2 = ["black", "yellow", "green", "blue"]

print(longest_one(Color1))
print(longest_one(Color2))


# # Question 6
# Write a Python program to count the occurrences of each word in a given sentence

# In[17]:


sequence = "Write a Python program to count the occurrences of each word in a given sentence"

list_1 = sequence.split() 
# Convert the list to set
set0 = set(list_1)

for ele in set0: print(ele,"-",list_1.count(ele))


# # Question 7
# Write a Python program to count and display the vowels of a given text

# In[18]:


text = "Write a Python program to count and display the vowels of a given text"

def vowels_count(t):
    vowels = ['a', 'e', 'i', 'o', 'u']
    dict_vowels = {'a' : 0, 'e' : 0, 'i' : 0, 'o' : 0, 'u' : 0}
    for ele in vowels:
        dict_vowels[ele] = t.count(ele) 
    return dict_vowels

vowels_count(text)


# # Question 8
# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)

# In[19]:


result={}
for x in range(1,10):
    result[x] = str(x*x)
result.items()


# # Question 9
# Write a Python program to combine two dictionary adding values for common keys
# 
# ● d1 = {'a': 100, 'b': 200, 'c':300}
# 
# ● d2 = {'a': 300, 'b': 200, 'd':400}
# 
# ● Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

# In[20]:


d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}


# In[21]:


counter = {} # Create blank dictionary

for item in d1: # dictionary 1
    if item in d2:
        counter[item] = d1.get(item) + d2.get(item)
    else:
        counter[item] = d1.get(item)

for item in d2: # dictionary 2
    if item in d1: pass
    else:
        counter[item] = d2.get(item)

# Print dictionary
counter


# # Question 10
# Write a Python program to print all unique values in a dictionary
# 
# ● Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]
# 
# ● Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}

# In[22]:


list_of_dic = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]


# In[24]:



u_value = set(val for dic in list_of_dic for val in dic.values())
print("Unique Values: ",sorted(u_value))


# In[ ]:





# In[ ]:




