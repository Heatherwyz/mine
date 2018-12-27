# -*- coding:utf-8 -*-
from time import sleep
from selenium import webdriver
import os
googledriver = ""
driver = webdriver.Chrome()
url = 'https://www.baidu.com'
driver.get(url)
sleep(10)
driver.close()