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
__author__ = "WYZ"

class TestMessageCenter(object):

    @pytest.mark.run(order=1)
    @allure.step(title='浏览器设置')
    def test_setBrower(self):
        global driver
        # 浏览器设置
        chrome_options = Options()
        # chrome_options.add_argument('--headless')  # 设置为无头模式
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

    @pytest.mark.run(order=3)
    @allure.step(title='互动消息开关打开')
    def test_3(self):
        global driver
        # 点击互动消息按钮进行订阅
        driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div/ul/li/div/label/i").click()
        hdmsg1 = driver.find_element_by_class_name("setTipAlertCon").get_attribute("innerText")
        print("互动消息1" + hdmsg1)
        assert hdmsg1 == "订阅成功"
        time.sleep(2)

    @pytest.mark.run(order=4)
    @allure.step(title='互动消息开关关闭')
    def test_4(self):
        global driver
        # 点击互动消息按钮进行取消订阅
        driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div/ul/li/div/label/i").click()
        hdmsg2 = driver.find_element_by_class_name("setTipAlertCon").get_attribute("innerText")
        print("互动消息2" + hdmsg2)
        assert hdmsg2 == "退订成功"
        time.sleep(2)

    @pytest.mark.run(order=5)
    @allure.step(title='公告大事开关打开')
    def test_5(self):
        global driver
        # 点击公告大事按钮进行订阅
        driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div/ul/li[2]/div/label/i").click()
        ggmsg1 = driver.find_element_by_class_name("setTipAlertCon").get_attribute("innerText")
        print("公告大事" + ggmsg1)
        assert ggmsg1 == "订阅成功"
        time.sleep(2)

    @pytest.mark.run(order=6)
    @allure.step(title='公告大事开关关闭')
    def test_6(self):
        global driver
        # 点击公告大事按钮取消订阅
        driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div/ul/li[2]/div/label/i").click()
        ggmsg2 = driver.find_element_by_class_name("setTipAlertCon").get_attribute("innerText")
        print("公告大事" + ggmsg2)
        assert ggmsg2 == "退订成功"
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
        assert thslcmsg2 == "退订成功"
        time.sleep(2)

    @pytest.mark.run(order=9)
    @allure.step(title='问财开关打开')
    def test_9(self):
        global driver
        # 点击问财订阅
        driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div/ul/li[4]/div/label/i").click()
        wcmsg1 = driver.find_element_by_class_name("setTipAlertCon").get_attribute("innerText")
        print("问财" + wcmsg1)
        assert wcmsg1 == "订阅成功"
        time.sleep(2)
        # wctc = driver.find_element_by_class_name("znxgAlertTip").is_displayed()
        # print(wctc)
        # assert wctc == True
        # print("弹出弹窗")
        # time.sleep(2)

    @pytest.mark.run(order=10)
    @allure.step(title='问财开关打开时弹窗弹出')
    def test_10(self):
        global driver
        wctc = driver.find_element_by_class_name("znxgAlertTip").is_displayed()
        print(wctc)
        assert wctc == True
        print("弹出弹窗")
        time.sleep(2)

    @pytest.mark.run(order=11)
    @allure.step(title='问财开关打开时弹出的弹窗取消')
    def test_11(self):
        global driver
        driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div[5]/div/span/a").click()
        time.sleep(2)
        wctc = driver.find_element_by_class_name("znxgAlertTip").is_displayed()
        print(wctc)
        assert wctc == False
        print("取消问财的弹窗")
        time.sleep(2)

    @pytest.mark.run(order=12)
    @allure.step(title='问财开关关闭')
    def test_12(self):
        global driver
        driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div/ul/li[4]/div/label/i").click()
        wcmsg2 = driver.find_element_by_class_name("setTipAlertCon").get_attribute("innerText")
        print("问财" + wcmsg2)
        assert wcmsg2 == "退订成功"
        time.sleep(2)

    @pytest.mark.run(order=13)
    @allure.step(title='问财开关再次打开')
    def test_13(self):
        global driver
        # 点击再次问财订阅
        driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div/ul/li[4]/div/label/i").click()
        wcmsg3 = driver.find_element_by_class_name("setTipAlertCon").get_attribute("innerText")
        print("问财再次" + wcmsg3)
        assert wcmsg3 == "订阅成功"
        time.sleep(2)

    @pytest.mark.run(order=14)
    @allure.step(title='问财弹窗再次弹出')
    def test_14(self):
        global driver
        wctc = driver.find_element_by_class_name("znxgAlertTip").is_displayed()
        print(wctc)
        assert wctc == True
        print("再次弹出弹窗")
        time.sleep(2)

    @pytest.mark.run(order=15)
    @allure.step(title='进入问财选股')
    def test_15(self):
        global driver
        # 点击选股
        driver.find_element_by_xpath("//*[@id='customSetColumn']/div[5]/div[1]/span/a[2]").click()
        wcxg = driver.current_url
        print("跳转的链接是" + driver.current_url)
        assert wcxg == "https://search.10jqka.com.cn/wukong/mobile/index.html?tab=1"
        driver.back()
        print('返回消息中心自定义设置')

    @pytest.mark.run(order=16)
    @allure.step(title='问财开关再次关闭')
    def test_16(self):
        global driver
        # 再次退订问财
        driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div/ul/li[4]/div/label/i").click()
        wcmsg4 = driver.find_element_by_class_name("setTipAlertCon").get_attribute("innerText")
        print("问财再次" + wcmsg4)
        assert wcmsg4 == "退订成功"
        time.sleep(2)

    @pytest.mark.run(order=17)
    @allure.step(title='新股提醒开关打开')
    def test_17(self):
        global driver
        # 点击新股提醒进行订阅
        driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div/ul/li[5]/div/label/i").click()
        xgtxmsg1 = driver.find_element_by_class_name("setTipAlertCon").get_attribute("innerText")
        print("新股提醒" + xgtxmsg1)
        assert xgtxmsg1 == "订阅成功"
        time.sleep(2)

    @pytest.mark.run(order=18)
    @allure.step(title='新股提醒开关关闭')
    def test_18(self):
        global driver
        # 点击新股提醒取消订阅
        driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div/ul/li[5]/div/label/i").click()
        xgtxmsg2 = driver.find_element_by_class_name("setTipAlertCon").get_attribute("innerText")
        print("新股提醒" + xgtxmsg2)
        assert xgtxmsg2 == "退订成功"
        time.sleep(2)

    @pytest.mark.run(order=19)
    @allure.step(title='同顺号开关打开')
    def test_19(self):
        global driver
        # 点击同顺号进行订阅
        driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div/ul/li[6]/div/label/i").click()
        tshxmsg1 = driver.find_element_by_class_name("setTipAlertCon").get_attribute("innerText")
        print("同顺号" + tshxmsg1)
        assert tshxmsg1 == "订阅成功"
        time.sleep(2)

    @pytest.mark.run(order=20)
    @allure.step(title='同顺号开关关闭')
    def test_20(self):
        global driver
        # 点击同顺号取消订阅
        driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div/ul/li[6]/div/label/i").click()
        tshxmsg1 = driver.find_element_by_class_name("setTipAlertCon").get_attribute("innerText")
        print("同顺号" + tshxmsg1)
        assert tshxmsg1 == "退订成功"
        time.sleep(2)

    @pytest.mark.run(order=21)
    @allure.step(title='保险服务开关打开')
    def test_21(self):
        global driver
        # 点击保险服务进行订阅
        driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div/ul/li[7]/div/label/i").click()
        bxfwmsg1 = driver.find_element_by_class_name("setTipAlertCon").get_attribute("innerText")
        print("保险服务" + bxfwmsg1)
        assert bxfwmsg1 == "订阅成功"
        time.sleep(2)

    @pytest.mark.run(order=22)
    @allure.step(title='保险服务开关关闭')
    def test_22(self):
        global driver
        # 点击保险服务取消订阅
        driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div/ul/li[7]/div/label/i").click()
        bxfwmsg2 = driver.find_element_by_class_name("setTipAlertCon").get_attribute("innerText")
        print("保险服务" + bxfwmsg2)
        assert bxfwmsg2 == "退订成功"
        time.sleep(2)

    @pytest.mark.run(order=23)
    @allure.step(title='看盘新姿势开关打开')
    def test_23(self):
        global driver
        # 点击订阅看盘新姿势
        driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div/ul/li[8]/div/label/i").click()
        kpmsg1 = driver.find_element_by_class_name("setTipAlertCon").get_attribute("innerText")
        print("看盘新姿势" + kpmsg1)
        assert kpmsg1 == "订阅成功"
        time.sleep(2)

    @pytest.mark.run(order=24)
    @allure.step(title='看盘新姿势开关关闭')
    def test_24(self):
        global driver
        # 点击取消订阅看盘新姿势
        driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div/ul/li[8]/div/label/i").click()
        kpmsg2 = driver.find_element_by_class_name("setTipAlertCon").get_attribute("innerText")
        print("看盘新姿势" + kpmsg2)
        assert kpmsg2 == "退订成功"
        time.sleep(2)

    @pytest.mark.run(order=25)
    @allure.step(title='投顾服务开关打开')
    def test_25(self):
        global driver
        # 点击订阅投顾服务
        driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div/ul/li[9]/div/label/i").click()
        tgmsg1 = driver.find_element_by_class_name("setTipAlertCon").get_attribute("innerText")
        print("投顾服务" + tgmsg1)
        assert tgmsg1 == "订阅成功"
        time.sleep(2)

    @pytest.mark.run(order=26)
    @allure.step(title='投顾服务开关关闭')
    def test_26(self):
        global driver
        # 点击取消订阅投顾服务
        driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div/ul/li[9]/div/label/i").click()
        tgmsg2 = driver.find_element_by_class_name("setTipAlertCon").get_attribute("innerText")
        print("投顾服务" + tgmsg2)
        assert tgmsg2 == "退订成功"
        time.sleep(2)

    @pytest.mark.run(order=27)
    @allure.step(title='点击同花顺小蜜的问号')
    def test_27(self):
        global driver
        # 点击同花顺小蜜的问号
        driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div[2]/div/div[2]/i").click()
        xmtc = driver.find_element_by_class_name("xmAlertTip").is_displayed()
        print(xmtc)
        assert xmtc == True
        print("弹出弹窗")
        time.sleep(2)

    @pytest.mark.run(order=28)
    @allure.step(title='点击我知道了')
    def test_28(self):
        global driver
        # 点击我知道了
        driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div[4]/div/span/a").click()
        xmtc = driver.find_element_by_class_name("xmAlertTip").is_displayed()
        print(xmtc)
        assert xmtc == False
        print("点击我知道了取消弹窗")
        time.sleep(2)

    @pytest.mark.run(order=29)
    @allure.step(title='点击进入智能监控')
    def test_29(self):
        global driver
        # 点击进入智能监控
        driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div[2]/ul/li/div").click()
        znjk = driver.current_url
        print("跳转的链接是" + driver.current_url)
        assert znjk == "https://eq.10jqka.com.cn/newscenter/perReco.html"
        time.sleep(2)

    @pytest.mark.run(order=30)
    @allure.step(title='股票操作')
    def test_30(self):
        global driver
        # 点击编辑按钮
        driver.find_element_by_xpath("/html/body/section/div/span[2]").click()
        time.sleep(2)

        # 点击全选
        driver.find_element_by_xpath("/html/body/section[2]/div[3]/div").click()

        # 点击删除
        driver.find_element_by_xpath("/html/body/section[2]/div[3]/div[2]").click()

        # 点击完成
        driver.find_element_by_xpath("/html/body/section[2]/div[3]/div[3]").click()

        # 点击编辑按钮
        driver.find_element_by_xpath("/html/body/section/div/span[2]").click()

        # 点击添加关注股票按钮
        driver.find_element_by_xpath("/html/body/section[2]/div").click()
        srk = driver.find_element_by_xpath("/html/body/section[3]/div[1]/div[1]/input").is_displayed()
        assert srk == True
        print("输入框存在")

    @pytest.mark.run(order=31)
    @allure.step(title='搜索股票')
    def test_31(self):
        global driver
        # 点击输入框
        driver.find_element_by_xpath("//input[@type='text']").click()

        # 输入0033
        driver.find_element_by_xpath("//input[@type='text']").send_keys("0033")
        ss = driver.find_element_by_xpath("/html/body/section[3]/div[2]/div/span[3]/ins").is_displayed()
        assert ss == True
        print("搜索结果存在")
    
    @pytest.mark.run(order=32)
    @allure.step(title='对第一个答案添加关注')
    def test_32(self):
        global driver
        # 对第一个答案添加关注
        driver.find_element_by_xpath("/html/body/section[3]/div[2]/div/span[3]/ins").click()
        gz = driver.find_element_by_xpath("/html/body/section[3]/div[2]/div[1]/span[3]/i").get_attribute("innerText")
        print(gz)
        assert gz == "已关注"

    @pytest.mark.run(order=33)
    @allure.step(title='关闭搜索')
    def test_33(self):
        # 点击x按钮
        global driver
        driver.find_element_by_xpath("/html/body/section[3]/div/div/span[2]").click()
        srk1 = driver.find_element_by_xpath("//input[@type='text']").get_attribute("innerText")
        print("输入框" + srk1)
        assert srk1 == ""

    @pytest.mark.run(order=34)
    @allure.step(title='删除股票')
    def test_34(self):
        global driver
        # 点击取消按钮
        driver.find_element_by_xpath("/html/body/section[3]/div/div[2]").click()

        # 勾选关注的第一个内容
        driver.find_element_by_xpath("/html/body/section[2]/div[2]/div[2]/div/div/ins").click()

        # 点击删除按钮
        driver.find_element_by_xpath("/html/body/section[2]/div[3]/div[2]").click()
        sctc = driver.find_element_by_xpath("/html/body/section[2]/div[4]/div[2]").is_displayed()
        assert sctc == True

        # 确定删除
        driver.find_element_by_xpath("/html/body/section[2]/div[4]/div[2]/div/span[2]").click()
        print("成功删除关注的股票")
        time.sleep(2)

    @pytest.mark.run(order=35)
    @allure.step(title='返回到智能监控页面')
    def test_35(self):
        # 点击完成按钮
        global driver
        driver.find_element_by_xpath("/html/body/section[2]/div[3]/div[3]").click()
        assert driver.find_element_by_xpath("/html/body/section[1]/div[1]/span[1]").is_displayed() == True
        print("返回到智能监控页面")

    @pytest.mark.run(order=36)
    @allure.step(title='返回到自定义设置页面')
    def test_36(self):
        # 返回自定义设置页面
        global driver
        driver.back()
        assert driver.current_url == "https://eq.10jqka.com.cn/newscenter/main.html"
        print("返回到自定义设置页面")

    @pytest.mark.run(order=37)
    @allure.step(title='点击使用须知打开弹窗')
    def test_37(self):
        # 点击使用须知
        driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div[2]/ul/li[2]/p/span[2]").click()
        time.sleep(2)
        assert driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div[3]/div/div[1]/h5").is_displayed() == True
        print("点击使用须知打开弹窗")
        time.sleep(2)

    @pytest.mark.run(order=38)
    @allure.step(title='点击我知道了')
    def test_38(self):
        # 点击我知道了
        driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div[3]/div/div[1]/span/a[2]").click()
        time.sleep(2)
        assert driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div[3]/div/div[1]/h5").is_displayed() == False
        # assert driver.find_element_by_class_name("cjAlertCon tradeBox").is_displayed() == False
        print("点击我知道了关闭弹窗")
        time.sleep(2)

    @pytest.mark.run(order=39)
    @allure.step(title='刷新回到消息中心')
    def test_39(self):
        driver.refresh()
        assert driver.current_url == "https://eq.10jqka.com.cn/newscenter/main.html"
        print("刷新回到消息中心")

    @pytest.mark.run(order=40)
    @allure.step(title='点击进入今日头条')
    def test_40(self):
        # 点击进入今日头条
        driver.find_element_by_xpath("//*[@id=\"fastread\"]/div/div/div[2]/div[2]/div").click()

        # 时间判断
        print(driver.find_element_by_xpath("/html/body/section[1]/div[1]/div[3]/h5/span").get_attribute("innerText"))
        print(time.strftime('%Y.%m.%d', time.localtime(time.time())))

    @pytest.mark.run(order=41)
    @allure.step(title='回到消息中心')
    def test_41(self):
        driver.back()
        assert driver.current_url == "https://eq.10jqka.com.cn/newscenter/main.html"
        print("回到消息中心")

    @pytest.mark.run(order=42)
    @allure.step(title='关闭标签页')
    def test_close(self):
        global driver
        driver.quit()
        print("关闭标签页")

if __name__ == '__main__' :
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    pytest.main("-s -q D:\\wyz\\study\\mine\\autotestwyz\\test_wyz.py  --alluredir D:\\wyz\\study\\mine\\autotestwyz\\TEST\\report-{0}".format(now))
    os.system("D:\\wyz\\allure-2.7.0\\bin\\allure generate D:\\wyz\\study\\mine\\autotestwyz\\TEST\\report-{0}/ -o D:\\wyz\\study\\mine\\autotestwyz\\TEST\\report-{0}/html".format(now))
