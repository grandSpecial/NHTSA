
# coding: utf-8

# ## National Highway Traffic Safety Administration: 2005 Colorado Complaints Analysis

# In[163]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

import urllib.request
from bs4 import BeautifulSoup

count = 1
full_list = []

# Generation 1: 2004 -2012
for yr in range(2004,2013):
    urls = [f"https://www.nhtsa.gov/vehicle/{yr}/CHEVROLET/COLORADO/EXTENDED%252520CAB",
            f"https://www.nhtsa.gov/vehicle/{yr/}CHEVROLET/COLORADO/REGULAR%252520CAB",
            f"https://www.nhtsa.gov/vehicle/{yr}/CHEVROLET/COLORADO/4%252520DR"
           ]
    for u in urls:
        driver = webdriver.Firefox()
        driver.get(u)
        driver.implicitly_wait(30)

        time.sleep(10)

        #clear feedback modal
        try:
            feedback = driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/a[1]")
            feedback.click()
        except:
            pass

        try:
            #"ELECTRICAL SYSTEM (68)"
            xpath = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div/div/div/div/div[2]/div[4]/div[2]/div[4]/div/div/div/div[2]/div[2]/div/section[1]/div/div/div[1]/div/span[3]")
            xpath.click()

            driver.implicitly_wait(10)
            while True:
                # open up all case notes
                #faq_Icon
                links = []
                for i in range(1,6):
                    xp = f'/html/body/div[1]/div[4]/div/div/div/div/div/div[2]/div[4]/div[2]/div[4]/div/div/div/div[2]/div[2]/div/section[1]/div/div/div[2]/div/div[{i}]/div[1]/div/a/span[1]'
                    xpath2 = driver.find_element_by_xpath(xp)
                    xpath2.click()
                    links.append(xpath2)

                #read case descriptions and store
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                first = soup.find_all('div', class_='col-xs-9')
                page_list = [x.find_all('p') for x in first]
                for i in page_list:
                    full_list.append(i)

                xpath3 = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div/div/div/div/div[2]/div[4]/div[2]/div[4]/div/div/div/div[2]/div[2]/div/section[1]/div/div/div[3]/button[2]")
                xpath3.click()

        except:
            print(f'captured {len(full_list)} complaints.')
            pass


# In[167]:


ref1 = 'FIRE'
ref2 = "BLOWER"

countsum = 1
for i in full_list:
    if ref1 and ref2 in str(i[0]):
        print(i[0],"\n")
        countsum += 1
print(f'''{countsum} references to the keywords "{ref1}" and "{ref2}". 
These cases represent {round(countsum/len(full_list)*100, 1)}% of all complaints.''')


# In[169]:


ref3 = 'SIGNAL'

countsum = 1
for i in full_list:
    if ref3 in str(i[0]):
        print(i[0],"\n")
        countsum += 1
print(f'''{countsum} references to the keywords "{ref}". 
These cases represent {round(countsum/len(full_list)*100, 1)}% of all complaints.''')

