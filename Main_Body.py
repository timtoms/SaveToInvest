#!/usr/bin/env python
# coding: utf-8

# In[151]:


import requests, webbrowser
from bs4 import BeautifulSoup

user_input = input("enter product name to search: ")
print("searching...")
google_search = requests.get("https://www.google.com/search?q="+user_input)

soup = BeautifulSoup(google_search.text, 'html.parser')

search_results = soup.select('.r a')

product_to_match = user_input.replace(" ","%20")
url = 'https://www.joinhoney.com/itemsearch?q='+ product_to_match
response = requests.get(url)
honey = BeautifulSoup(response.text, 'html.parser')

webbrowser.open(url)

selected_url ='https://www.joinhoney.com/shop/adidas/p/7360533218492451884_7582091810f99e22716293ae964d0eb5_4ef30554412929c68b459d3b817479fa?searchQuery=adidas%20sleek%20shoes'
page = requests.get(selected_url)
selection = BeautifulSoup(page.text, 'html.parser')
product_info = selection.find(id="Shop:Product:ProductInfo:ProductInfoCard:div-price")
print(product_info)

    


# In[143]:


a = str(product_info.contents)[3:8]
Risk = "standard"


# In[144]:


print(a)


# In[181]:


timeline = "5"
projected = "3,274"
print("If you invest this saved $"+ a + " into this fund, you are estimated to have $" + projected + "in" + timeline + " years " + str(float(a)*1.123) + "estimate is based on the average performance of the past 5 years")


# In[182]:


print("If you invest this saved $"+ a + " into this fund, you are estimated to have $" + projected)


# In[163]:


float(a)*3

