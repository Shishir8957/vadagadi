# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

# website = "https://hamrobazaar.com/category/motorcycles/eb9c8147-07c0-4951-a962-381cdb400e37/59973aed-f03d-4985-9aec-542831929081"
# path = "/Users/royel/Downloads/chromedriver"

# driver = webdriver.Chrome()

# service = Service(executable_path=path)
# driver = webdriver.Chrome(service=service)
# driver.get(website)

# # from selenium import webdriver
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.chrome.options import Options
# # import time

# # options = Options()
# # options.add_experimental_option('excludeSwitches', ['enable-logging'])
# # driver = webdriver.Chrome(executable_path="/Users/royel/Downloads/chromedriver.exe")
# # url = 'https://hamrobazaar.com/category/motorcycles/eb9c8147-07c0-4951-a962-381cdb400e37/59973aed-f03d-4985-9aec-542831929081'

# # driver.get(url)
# b1=[]
# a = driver.find_elements(by="xpath",value='//section[@class="home--listings"]//div[@class="product-list"]//div[@class="card-product-linear"]//div[@class="card-product-linear-imgContainer"]//div[@class="main-img"]')
# print(a)
# for i in a:
#     p = i.find_element(by="xpath",value='./a').get_attribute("href")
#     print(p)

# driver.quit()

# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# import time

# options = Options()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(executable_path="/Users/royel/Downloads/chromedriver.exe")
# url = 'https://ramrogaadi.com/used-bikes-in-kathmandu'

# driver.get(url)
# b1=[]
# a = driver.find_elements(by="xpath",value='//div[@class="item-detl-head"]')
# print(a)
# for i in a:
#     p = i.find_element(by="xpath",value='./a').get_attribute("href")
#     print(p)

# driver.quit()

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path="/Users/royel/Downloads/chromedriver.exe")
url = 'https://ramrogaadi.com/used-bikes-in-kathmandu'

driver.get(url)
b1=[]
a = driver.find_elements(by="xpath",value='//div[@class="item-detl-head"]')
print(a)
for i in a:
    p = i.find_element(by="xpath",value='./a').get_attribute("href")
    print(p)

driver.quit()