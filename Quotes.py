#!/usr/bin/env python
# coding: utf-8

# In[4]:


pip install requests-html


# In[68]:


from requests_html import HTMLSession


# In[69]:


session = HTMLSession()


# In[71]:


url = 'https://quotes.toscrape.com/'
r = session.get(url, headers = header)
r.status_code
# r.html.render(sleep=1)


# In[99]:


contents = r.html.find('div.quote')
# contents
links = []
for content in contents:
    quote = content.find('span.text', first=True).text
    author = content.find('small.author', first=True).text
    link = content.find('a', first=True).attrs['href']
    links.append([quote,author,link])
print(links)
len(links)


# In[80]:


baseurl = 'https://quotes.toscrape.com/'


# In[100]:


birthlist = []
for link in links:
    urllink = baseurl + link[2]
    response = session.get(urllink)
    brithday = response.html.find('span.author-born-date',first=True).text
    birthlist.append(brithday)
print(birthlist)
len(birthlist)


# In[101]:


import pandas as pd


# In[102]:


df1 = pd.DataFrame(links, columns = ['Quote','Author','Sublink'])


# In[104]:


df2 = pd.DataFrame(birthlist, columns = ['Birthday'])


# In[108]:


df = pd.concat([df1,df2], axis =1)


# In[109]:


df


# In[110]:


df['Sublink'] = baseurl + df['Sublink']


# In[112]:


df.rename(columns = {'Sublink':'Link'})


# In[ ]:




