#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import pandas library
import pandas as pd
 
# initialize list of lists
data1 = [['Honey Coupon',180.00,160.00,20.000 ],
        ['Amazon Prime Coupon',180.00,150.00,30.00],
        ['Addidas StoreWide Coupon',180.00,150.00,30.00],
        ['Amazon Prime Coupon',100.00,50.00,50.00],
        ['Addidas StoreWide Coupon',180.00,150.00,30.00]]

data2 = [['55%','44%',50,50,5,'STANDARD','3 274'],
         ['55%','44%',20,50,5,'STANDARD','1 342'],
         ['79%','19%',10,4,10,'STANDARD','1 516'],
         ['55%','44%',30,100,4,'STANDARD','2 023'] ]

# Create the pandas DataFrame
df1 = pd.DataFrame(data1, columns = ['NameOfCoupon','Original Adiddas Price','Disounted Price','You Save!'])
df2 = pd.DataFrame(data2,columns = ['Stocks','Bonds','MonthlyDeposit','OneTimeDeposit','Timeline','RiskLevel','EstimatedToHave'])
 
# print dataframe.
df1
df2

#In a different cell
df1


# In[ ]:





# In[ ]:




