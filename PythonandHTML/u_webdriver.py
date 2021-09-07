from selenium import webdriver as wd
import time

driver=wd.Chrome()
web_url='https://localprod.pandateacher.com/python-manuscript/hello-spiderman/'
driver.get(web_url)
time.sleep(1)
driver.close()