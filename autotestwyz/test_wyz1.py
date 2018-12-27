# -*- encoding=utf8 -*-

import os
import sys
import fun
import time
import pytest
import allure
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.webdriver import WebDriver
# from airtest_selenium.proxy import WebChrome
from selenium.webdriver.common import alert

__author__ = "WYZ"

class TestMessageCenter(object):

    @pytest.mark.run(order=1)
    @allure.step(title='浏览器设置')
    def test_setBrower(self):
        global driver
        # 浏览器设置
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # 设置为无头模式
        chrome_options.add_argument('--disable-gpu')  # 设置为不使用gpu
        # chrome_options.add_argument("window-size=1024,768") # 设置浏览器默认窗口大小
        # chrome_options.add_argument("--no-sandbox") # 设置沙盒模式
        # chrome_options.add_argument("--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A366 hxFont/normal hxnoimage/0 VoiceAssistantVer/1201 hxtheme/0 IHexin/10.30.41 (Royal Flush) innerversion/I037.08.340 build/10.30.43")
        driver = webdriver.Chrome(options=chrome_options)
        driver.set_window_size(375, 812)  # 设置浏览器窗口大小
        driver.implicitly_wait(10)  # 设置隐式等待时间为10s
        print("浏览器设置完成")

    @pytest.mark.run(order=2)
    @allure.step(title='登录账号及加载cookie')
    def test_login(self):
        global driver
        # 登录
        # driver.get("http://upass.10jqka.com.cn/login")
        # driver.find_element_by_id("username").click()
        # driver.find_element_by_id("username").send_keys("wyzt6")
        # driver.find_element_by_id("password").click()
        # driver.find_element_by_id("password").send_keys("123456")
        # driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/form/div/ul/li[4]/font").click()
        # driver.find_element_by_name("submit").click()
        # print("登录成功")

        # 打印cookie
        # print(driver.get_cookies())
        # print("-   -"*20)

        # 进入消息中心首页
        driver.get("https://eq.10jqka.com.cn/newscenter/main.html")
        sys.argv = ["wyzt6", "123456"]
        fun.loadCookie(driver, sys.argv[0], sys.argv[1])
        assert driver.get_cookies() != ""
        time.sleep(2)
        # print("成功进入消息中心首页")
        # 将获取到的cookie放入消息中心首页
        # for cookie in driver.get_cookies():
        #     driver.add_cookie(cookie)
        # driver.refresh()
        # print("cookie更新成功")
        # 点击进入自定义设置页面
        driver.find_element_by_xpath("//*[@id=\"customSetTip\"]/div").click()
        time.sleep(2)

    @pytest.mark.run(order=7)
    @allure.step(title='同花顺理财开关打开')
    def test_7(self):
        global driver
        # 点击同花顺理财进行订阅
        driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div/ul/li[3]/div/label/i").click()
        thslcmsg1 = driver.find_element_by_class_name("setTipAlertCon").get_attribute("innerText")
        print("同花顺理财" + thslcmsg1)
        assert thslcmsg1 == "订阅成功"
        time.sleep(2)

    @pytest.mark.run(order=8)
    @allure.step(title='同花顺理财开关关闭')
    def test_8(self):
        global driver
        # 点击同花顺理财取消订阅
        driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div/ul/li[3]/div/label/i").click()
        thslcmsg2 = driver.find_element_by_class_name("setTipAlertCon").get_attribute("innerText")
        print("同花顺理财" + thslcmsg2)
        driver.execute_script("window.alert(document.getElementsByTagName('div')[95].innerText)")
        assert thslcmsg2 == "退订成功"
        time.sleep(2)
# if __name__ == '__main__' :
#     now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
#     pytest.main("-s -q D:\\wyz\\study\\mine\\autotestwyz\\test_wyz1.py  --alluredir D:\\wyz\\study\\mine\\autotestwyz\\TEST\\report-{0}".format(now))
#     os.system("D:\\wyz\\allure-2.7.0\\bin\\allure generate D:\\wyz\\study\\mine\\autotestwyz\\TEST\\report-{0}/ -o D:\\wyz\\study\\mine\\autotestwyz\\TEST\\report-{0}/html".format(now))
