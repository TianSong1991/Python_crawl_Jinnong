import pandas as pd
from selenium import webdriver

data=pd.read_csv("C:/Users/Administrator/Desktop/crawl/citycrawl/crawldata.csv")
num1 = data.shape[0]

driver = webdriver.Chrome()
for i in range(num1):
    url1 = data['urls'][i]
    driver.get(url1)    
    t1=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[3]/table/tbody/tr[2]/td/p/table/tbody").text
    data['phone'][i] = t1

data.to_csv('result.csv')	
