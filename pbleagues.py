#!/usr/bin/env python
# coding: utf-8

# In[1]:


from splinter import Browser
from bs4 import BeautifulSoup
import time
import pandas as pd


# In[2]:


# Set up the browser
browser = Browser('chrome')


# In[3]:


url = 'https://pbleagues.com/cgi-bin/playerprofile.cgi?EPID=u2GerUTxYgYwJssR'
browser.visit(url)


# In[4]:


profilelist = ['https://pbleagues.com/cgi-bin/playerprofile.cgi?EPID=Xo4nZj48ox1xatVL',
'https://pbleagues.com/cgi-bin/playerprofile.cgi?EPID=1wXnzAjzZ3iSFigC',
'https://pbleagues.com/cgi-bin/playerprofile.cgi?EPID=6msg9on8ggk105m6',
'https://pbleagues.com/cgi-bin/playerprofile.cgi?EPID=16v4f17ac8nbrm0x',
'https://pbleagues.com/cgi-bin/playerprofile.cgi?EPID=fxwppas6wef2dT3T',
'https://pbleagues.com/cgi-bin/playerprofile.cgi?EPID=8rp19xp3y551l8v0',
'https://pbleagues.com/cgi-bin/playerprofile.cgi?EPID=Zmkgv5uZLe564lys',
'https://pbleagues.com/cgi-bin/playerprofile.cgi?EPID=u2GerUTxYgYwJssR',
'https://pbleagues.com/cgi-bin/playerprofile.cgi?EPID=u0FJ0qh8c9Ud0lUC',
'https://pbleagues.com/cgi-bin/playerprofile.cgi?EPID=5sjt0sc87f33rqle',
'https://pbleagues.com/cgi-bin/playerprofile.cgi?EPID=206D64C39C4D9CE9',
'https://pbleagues.com/cgi-bin/playerprofile.cgi?EPID=nZytemzTuemi5uxM',
'https://pbleagues.com/cgi-bin/playerprofile.cgi?EPID=C396507F45443F4B',
'https://pbleagues.com/cgi-bin/playerprofile.cgi?EPID=rTt9uIk4ELqgj3kk',
'https://pbleagues.com/cgi-bin/playerprofile.cgi?EPID=6r7k18hghvj6rso1',
'https://pbleagues.com/cgi-bin/playerprofile.cgi?EPID=m17jTDbfPP8WKTBB',
'https://pbleagues.com/cgi-bin/playerprofile.cgi?EPID=3OngMKT3Ma0S43M7',
'https://pbleagues.com/cgi-bin/playerprofile.cgi?EPID=8113D3D31F1FA347',
'https://pbleagues.com/cgi-bin/playerprofile.cgi?EPID=ZKy2GOEZtbsDCBZc',
'https://pbleagues.com/cgi-bin/playerprofile.cgi?EPID=W08GJEPTmXERySMp',
'https://pbleagues.com/cgi-bin/playerprofile.cgi?EPID=qmywgs0anxgylwpg',
'https://pbleagues.com/cgi-bin/playerprofile.cgi?EPID=7E1EBAACC458F716',
'https://pbleagues.com/cgi-bin/playerprofile.cgi?EPID=buix4f9glin49ikb',
'https://pbleagues.com/cgi-bin/playerprofile.cgi?EPID=BD8D636BE0CB0641',
'https://pbleagues.com/cgi-bin/playerprofile.cgi?EPID=C63479D934EF746C',
'https://pbleagues.com/cgi-bin/playerprofile.cgi?EPID=809D194813F92F1E',
'https://pbleagues.com/cgi-bin/playerprofile.cgi?EPID=E758214EF98B5EB8',
'https://pbleagues.com/cgi-bin/playerprofile.cgi?EPID=x37c8wq40crurch0',
'https://pbleagues.com/cgi-bin/playerprofile.cgi?EPID=44DBA34183260A40',
'https://pbleagues.com/cgi-bin/playerprofile.cgi?EPID=13D95D4E6760F999',
'https://pbleagues.com/cgi-bin/playerprofile.cgi?EPID=QoB5tqckeXmVQbWO',
'https://pbleagues.com/cgi-bin/playerprofile.cgi?EPID=78D5A3902EA9BD77',
'https://pbleagues.com/cgi-bin/playerprofile.cgi?EPID=3755F63C64C3D457',
'https://pbleagues.com/cgi-bin/playerprofile.cgi?EPID=2731C62559C93A9F',
'https://pbleagues.com/cgi-bin/playerprofile.cgi?EPID=0BAAF889FC8C0FF4',
'https://pbleagues.com/cgi-bin/playerprofile.cgi?EPID=K7IDwfioju9KgGF1',
'https://pbleagues.com/cgi-bin/playerprofile.cgi?EPID=bgijm8ss3vqb838z',
'https://pbleagues.com/cgi-bin/playerprofile.cgi?EPID=m6piRzR44YEI84mn',
'https://pbleagues.com/cgi-bin/playerprofile.cgi?EPID=9AD3AC7CDF6A3D88',
'https://pbleagues.com/cgi-bin/playerprofile.cgi?EPID=E6F01500E1C53343',
'https://pbleagues.com/cgi-bin/playerprofile.cgi?EPID=vNoqQJ0WYDHNOMXy']


# In[5]:


user_login = "omgshoed"
user_password = "EAWVN387ePDpWZ5"


# In[6]:


input_field = browser.find_by_xpath('/html/body/div/div[2]/div/div/div[2]/div[3]/div/div[1]/div/form/table/tbody/tr[1]/td[2]/input')
password_field = browser.find_by_xpath('/html/body/div/div[2]/div/div/div[2]/div[3]/div/div[1]/div/form/table/tbody/tr[2]/td[2]/input')
login_button = browser.find_by_xpath('/html/body/div/div[2]/div/div/div[2]/div[3]/div/div[1]/div/form/table/tbody/tr[5]/td[2]/input')


# In[7]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')
input_field.fill(user_login)
password_field.fill(user_password)
login_button.click()


# In[8]:


playernamelist = []
playerpointslist = []
playerrankinglist = []
for profile in profilelist:
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    browser.visit(profile)
    playername = browser.find_by_tag('h2')
    playersummary = browser.find_by_tag('h3')
    playernamelist.append(playername.text)
    playerpointslist.append(playersummary.text[playersummary.text.index("(")+1:playersummary.text.index(")")])
    playerrankinglist.append(playersummary.text[playersummary.text.index(":")+2:playersummary.text.index("(")-1])
print("Data fetching complete!")


# In[9]:


columns = ["Link to APPA profile", "Name", "Current APPA points", "Current Ranking"]
df = pd.DataFrame({"Link to APPA profile":profilelist},{"Name":playernamelist},{"Current APPA points":playerpointslist},{"Current Ranking":playerrankinglist})
df


# In[ ]:


browser.quit()


# In[ ]:





# In[ ]:




