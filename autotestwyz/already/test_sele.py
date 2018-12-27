#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestBaiduSample(object):

    @pytest.mark.run(order=1)
    @allure.step(title='打开')
    def test_open(self):
        print("open")
        global driver
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        # chrome_options.add_argument("window-size=381,940")
        chrome_options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://www.baidu.com")
        time.sleep(1)

        assert driver.title == "百度"

    @pytest.mark.run(order=2)
    @allure.step(title='点击')
    def test_news(self):
        print("open news")
        global driver
        driver.find_element_by_name("tj_trnews").click()
        time.sleep(1)

        assert driver.title == "百度新闻"

    @pytest.mark.run(order=3)
    @allure.step(title='关闭')
    def test_close(self):
        print("close")
        global driver
        driver.quit()


'''
if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    pytest.main("-s -q /data/www/html/test_sele.py  --alluredir /data/www/html/report-{0}".format(now))
    os.system("allure generate /data/www/html/report-{0}/ -o /data/www/html/report-{0}/html".format(now))
'''


