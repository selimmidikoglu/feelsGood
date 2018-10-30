import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.select import Select
import json


def keyExistence(key,dict):
    keyExistence = False
    if key in dict:
        keyExistence = True
    return keyExistence

driver = webdriver.Chrome('D:\\reactProjects\\feelsGood\\feelsGood\\chromedriver.exe')

driver.get("https://www.brainyquote.com/authors")
driver.maximize_window()

authors = driver.find_elements_by_class_name("authorContentName") 
# inserting authors names to array
# if one of those authors is clicked name will be deleted in other 
# for loop to click all the authors without any repeat
authors_names = []
quotes_dic = {}
kw_quoteId = {}
'''/html/body/div[5]/div[2]/div[1]/div/div/div[1]/div[2]/div/div[20]/a/span'''
for author in authors:
    authors_names.insert(len(authors_names),author.text)
id = 0 # starting from 0 assigning ids to everyquote
i = 0
counter = 0
id_fake = 0 # since I loop through 5 different keywords id of one quote is applicable for 5 keyword
for author_name in authors_names:
    time.sleep(1)
    authors = driver.find_elements_by_xpath("//div[@class = 'bqLn']/a/span")
    authors[i].click()
    driver.execute_script("window.scrollTo(0, 100)") 
    quotes = driver.find_elements_by_xpath("//div[@class='clearfix']/a[1]")
    for quote in quotes:
        quotes_dic[i] = {"id": id,"author": author_name,"quote": quote.text}
        id = id + 1
        print(quotes_dic[i])
        print("adnan")
    keywords = driver.find_elements_by_xpath( "//div[@class ='kw-box']/a")
    for keyword  in keywords:
        if counter<5:
            if not keyExistence(keyword.text,kw_quoteId):
                arr = []
                kw_quoteId[keyword.text] = arr
                kw_quoteId[keyword.text].append(id_fake)
            else:
                kw_quoteId[keyword.text].append(id_fake)
        else:
            counter = 0   
            id_fake =id_fake + 1
            if not keyExistence(keyword.text,kw_quoteId):
                arr = []
                kw_quoteId[keyword.text] = arr
                kw_quoteId[keyword.text].append(id_fake)
            else:
                kw_quoteId[keyword.text].append(id_fake)
        counter = counter + 1
        print(keyword.text, kw_quoteId[keyword.text])
    print(driver.current_url)
    driver.back()
    i = i + 1 



'''quotes = driver.find_elements_by_xpath("//div[@class='clearfix']/a[1]")
keywords = driver.find_elements_by_class_name("oncl_list_kc")
  for keyword in keywords:
        if counter<5:
            kw_quoteId[keyword] = str(id)
            counter = counter + 1
            print(kw_quoteId)
        else:
            counter = 0'''
'''counter = 0
for keyword in keywords:
    if counter == 5:
        counter = 0
        print("\n") 
    print(keyword.text)
    counter = counter + 1'''
       

'''//*[@id="qpos_1_1"]/div[1]/div/a[1]'''

'''//*[@id="qpos_1_2"]/div[2]'''