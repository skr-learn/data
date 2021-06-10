#!/usr/bin/env python
# coding: utf-8

# In[80]:


import requests
from datetime import datetime,timedelta
import json


# In[81]:


today = datetime.today()


# In[82]:


today


# In[83]:


print(today)


# In[84]:


num_days = 7

pin = ["841405","841428"]


# In[85]:


all_dates = []


# In[86]:


for i in range(num_days):
    all_dates.append(today + timedelta(i))


# In[87]:


all_dates


# In[88]:


final_dates = []


# In[89]:


for i in all_dates:
    final_dates.append(i.strftime("%d%m%y"))


# In[90]:


final_dates


# In[91]:


slots = 0


# In[ ]:


while True:
    
    for p in pin:
        for d in final_dates:
            URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(p,d)
            
            result=requests.get(URL)
            #print(result.text)
            
            json_result=result.json()
            
            if json_result["centers"]:
                for center in json_result["centers"]:
                    for session in center["sessions"]:
                        if session["available_capacity_dose1"] > 1:
                            slots == 1
                            print("Pincode: "+p)
                            print("Date: "+d)
                            print("Vaccines available (Dose-1): ", session["available_capacity_dose1"])
                            print("Center Name: ", center["name"])
                            print("Center Address: ",center["address"])
                            print("\n")
                        else:
                            slots == 2
            if slots == 2:
                print("No slots available!")


# In[ ]:




