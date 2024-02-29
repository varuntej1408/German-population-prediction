#!/usr/bin/env python
# coding: utf-8

# In[102]:


import xml
import html5lib


# In[103]:


pip install beautifulsoup4


# In[5]:


import requests
import pandas as pd

# Define the URL of the webpage containing the table
url = 'https://www.destatis.de/EN/Themes/Society-Environment/Population/Current-Population/Tables/population-by-nationality-groups.html'

# Get the HTML content
html = requests.get(url).content

# Extract all tables from the HTML
df_list = pd.read_html(html)

# Choose the relevant table (usually the last one)
df = df_list[-1]

# Save the dataframe to a CSV file
df.to_csv('my_data.csv', index=False)

df


# In[6]:


df


# In[7]:


column_names = list(df)
column_names 


# In[8]:


df.columns = range(df.shape[1])


# In[9]:


df.shape


# In[10]:


df.shape[1]


# In[11]:


df.rename(columns={0: 'Reference year',1: 'Total Number',2:'Germany',3:'In Percentage Germany',4:'EU',5:'In Percentage EU',6:'Rest of Europe',7:'In Percentage Europe',8:'Other states',9:'In Percentage Other states'}, inplace=True)


# In[12]:


df1 = df.drop(12)


# In[13]:


df['Reference year'].loc[df.index[2]]


# In[14]:


df1


# In[15]:


df1.at[2,'Reference year'] = 2020
df1.at[5,'Reference year'] = 2017
df1.at[6,'Reference year'] = 2016
df1.at[9,'Reference year'] = 2013


# In[97]:


df1.sort_values(by=['Germany'],ascending=True)


# In[17]:


import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


# In[82]:


df1 = df1.astype(str)


# In[98]:




# Sample data (replace with your actual data)
x_values = df1['Reference year']
y_values = df1['Germany']

# Create the line graph
plt.plot(x_values[::-1], y_values[::-1], marker='o', linestyle='-', color='b')
plt.xlabel("Year")
plt.ylabel("Population")
plt.title("German population by years")

# Show the plot
plt.grid(True)
plt.show()


# In[90]:



# Sample data (replace with your actual data)
x_values = df1['Reference year']
y_values = df1['EU']

# Create the line graph
plt.plot(x_values[::-1], y_values[::-1], marker='o', linestyle='-', color='b')
plt.xlabel("Year")
plt.ylabel("Population")
plt.title("EU population by years")

# Show the plot
plt.grid(True)
plt.show()


# In[91]:



# Sample data (replace with your actual data)
x_values = df1['Reference year']
y_values = df1['Other states']

# Create the line graph
plt.plot(x_values[::-1], y_values[::-1], marker='o', linestyle='-', color='b')
plt.xlabel("Year")
plt.ylabel("Population")
plt.title("Other states population by years")

# Show the plot
plt.grid(True)
plt.show()


# In[32]:


from sklearn.linear_model import LinearRegression


# In[67]:



df2 = pd.concat([df1['Reference year'],df1['Germany']],axis  =1)
df2


# In[72]:


x = df2.iloc[:, 0].values.reshape(-1, 1)
y = df2.iloc[:, 1].values.reshape(-1, 1)
model = LinearRegression().fit(x, y)
y_pred = model.predict([[2060]])
y_pred


# In[101]:


# Figure Size
fig = plt.figure(figsize =(10, 7))
 
# Horizontal Bar Plot
plt.bar(x_values, y_values)


# In[ ]:




