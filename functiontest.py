#coding=utf-8
import time
from selenium import webdriver



url = "http://ask.testfan.cn"
driver = webdriver.Chrome(executable_path="C:\Users\chris\Desktop\chromedriver_win32\chromedriver.exe")
driver.get(url)
driver.find_element_by_xpath("/html/body/div[3]/div[1]/h4/a[2]").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div/div[2]/form/div[1]/input").send_keys("yaoraozhou@163.com")
driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/input").send_keys("zsy@testfan")
driver.find_element_by_xpath("/html/body/div/div[2]/form/div[3]/button").click()
time.sleep(2)
driver.quit()