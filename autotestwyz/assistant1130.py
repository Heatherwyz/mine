
# -*- encoding=utf8 -*-
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.webdriver import WebDriver
# from airtest_selenium.proxy import WebChrome
__author__ = "WYZ"

#浏览器设置
chrome_options = Options()
chrome_options.add_argument('--headless')  # 设置为无头模式
chrome_options.add_argument('--disable-gpu')  # 设置为不使用gpu
# chrome_options.add_argument("window-size=1024,768") # 设置浏览器默认窗口大小
# chrome_options.add_argument("--no-sandbox") # 设置沙盒模式
chrome_options.add_argument(
    "--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E302 IHexin/10.30.10 (Royal Flush) userid/386199259 innerversion/I037.08.334 build/10.30.13 hxtheme/1 hxFont/normal VoiceAssistantVer/0 hxnoimage/0")
# driver = webdriver.Chrome(chrome_options=chrome_options)
driver = webdriver.Chrome()
driver.set_window_size(375, 812) # 设置浏览器窗口大小
driver.implicitly_wait(10)  # 设置隐式等待时间为10s
print("浏览器设置完成")

#登录
driver.get("http://upass.10jqka.com.cn/login")
driver.find_element_by_id("username").click()
driver.find_element_by_id("username").send_keys("wyzt6")
driver.find_element_by_id("password").click()
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/form/div/ul/li[4]/font").click()
driver.find_element_by_name("submit").click()
print("登录成功")

# 打印cookie
# print(driver.get_cookies())
# print("-   -"*20)
#进入消息中心首页
driver.get("https://eq.10jqka.com.cn/newscenter/main.html")
print("成功进入消息中心首页")

#将获取到的cookie放入消息中心首页
for cookie in driver.get_cookies():
    driver.add_cookie(cookie)
print("cookie更新成功")
time.sleep(2)

#点击进入自定义设置页面
driver.find_element_by_xpath("//*[@id=\"customSetTip\"]/div").click()

#点击互动消息按钮进行订阅
driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div/ul/li/div/label/i").click()
hdmsg1 = driver.find_element_by_class_name("setTipAlertCon").text
print("互动消息"+hdmsg1)
assert hdmsg1 == "订阅成功"
time.sleep(2)

#点击互动消息按钮进行取消订阅
driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div/ul/li/div/label/i").click()
hdmsg2 = driver.find_element_by_class_name("setTipAlertCon").text
print("互动消息"+hdmsg2)
assert hdmsg2 == "退订成功"
time.sleep(2)

#点击新股提醒进行订阅
driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div/ul/li[5]/div/label/i").click()
xgtxmsg1 = driver.find_element_by_class_name("setTipAlertCon").text
print("新股提醒"+xgtxmsg1)
assert xgtxmsg1 == "订阅成功"
time.sleep(2)

#点击新股提醒取消订阅
driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div/ul/li[5]/div/label/i").click()
xgtxmsg2 = driver.find_element_by_class_name("setTipAlertCon").text
print("新股提醒"+xgtxmsg2)
assert xgtxmsg2 == "退订成功"
time.sleep(2)

#点击同顺号进行订阅
driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div/ul/li[6]/div/label/i").click()
tshxmsg1 = driver.find_element_by_class_name("setTipAlertCon").text
print("同顺号"+tshxmsg1)
assert tshxmsg1 == "订阅成功"
time.sleep(2)

#点击同顺号取消订阅
driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div/ul/li[6]/div/label/i").click()
tshxmsg2 = driver.find_element_by_class_name("setTipAlertCon").text
print("同顺号"+tshxmsg2)
assert tshxmsg2 == "退订成功"
time.sleep(2)

#点击保险服务进行订阅
driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div/ul/li[7]/div/label/i").click()
bxfwmsg1 = driver.find_element_by_class_name("setTipAlertCon").text
print("保险服务"+bxfwmsg1)
assert bxfwmsg1 == "订阅成功"
time.sleep(2)

#点击保险服务取消订阅
driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div/ul/li[7]/div/label/i").click()
bxfwmsg2 = driver.find_element_by_class_name("setTipAlertCon").text
print("保险服务"+bxfwmsg2)
assert bxfwmsg2 == "退订成功"
time.sleep(2)

#点击订阅看盘新姿势
driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div/ul/li[8]/div/label/i").click()
kpmsg1 = driver.find_element_by_class_name("setTipAlertCon").text
print("看盘新姿势"+kpmsg1)
assert kpmsg1 == "订阅成功"
time.sleep(2)

#点击取消订阅看盘新姿势
driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div/ul/li[8]/div/label/i").click()
kpmsg2 = driver.find_element_by_class_name("setTipAlertCon").text
print("看盘新姿势"+kpmsg2)
assert kpmsg2 == "退订成功"
time.sleep(2)

#点击订阅投顾服务
driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div/ul/li[9]/div/label/i").click()
tgmsg1 = driver.find_element_by_class_name("setTipAlertCon").text
print("投顾服务"+tgmsg1)
assert tgmsg1 == "订阅成功"
time.sleep(2)

#点击取消订阅投顾服务
driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div/ul/li[9]/div/label/i").click()
tgmsg2 = driver.find_element_by_class_name("setTipAlertCon").text
print("投顾服务"+tgmsg2)
assert tgmsg2 == "退订成功"
time.sleep(2)

#点击同花顺小蜜的问号
driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div[2]/div/div[2]/i").click()
xmtc = driver.find_element_by_class_name("xmAlertTip").is_displayed()
print(xmtc)
assert xmtc == True
print("弹出弹窗")
time.sleep(2)

#点击我知道了
driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div[4]/div/span/a").click()
xmtc = driver.find_element_by_class_name("xmAlertTip").is_displayed()
print(xmtc)
assert xmtc == False
print("点击我知道了取消弹窗")
time.sleep(2)

#点击进入智能监控
driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div[2]/ul/li/div").click()
znjk = driver.current_url
print ("跳转的链接是"+driver.current_url)
assert znjk == "https://eq.10jqka.com.cn/newscenter/perReco.html"
time.sleep(2)

#点击编辑按钮
driver.find_element_by_xpath("/html/body/section/div/span[2]").click()
time.sleep(2)

#点击全选
driver.find_element_by_xpath("/html/body/section[2]/div[3]/div").click()

#点击删除
driver.find_element_by_xpath("/html/body/section[2]/div[3]/div[2]").click()

#点击完成
driver.find_element_by_xpath("/html/body/section[2]/div[3]/div[3]").click()

#点击编辑按钮
driver.find_element_by_xpath("/html/body/section/div/span[2]").click()

#点击添加关注股票按钮
driver.find_element_by_xpath("/html/body/section[2]/div").click()
srk = driver.find_element_by_xpath("/html/body/section[3]/div[1]/div[1]/input").is_displayed()
assert srk == True
print("输入框存在")

#点击输入框
driver.find_element_by_xpath("//input[@type='text']").click()

#输入0033
driver.find_element_by_xpath("//input[@type='text']").send_keys("0033")
ss = driver.find_element_by_xpath("/html/body/section[3]/div[2]/div/span[3]/ins").is_displayed()
assert ss == True
print("搜索结果存在")

#对第一个答案添加关注
driver.find_element_by_xpath("/html/body/section[3]/div[2]/div/span[3]/ins").click()
gz = driver.find_element_by_xpath("/html/body/section[3]/div[2]/div[1]/span[3]/i").text
print(gz)
assert  gz == "已关注"

#点击x按钮
driver.find_element_by_xpath("/html/body/section[3]/div/div/span[2]").click()
srk1 = driver.find_element_by_xpath("//input[@type='text']").text
print("输入框"+srk1)
assert srk1 == ""

#点击取消按钮
driver.find_element_by_xpath("/html/body/section[3]/div/div[2]").click()

#勾选关注的第一个内容
driver.find_element_by_xpath("/html/body/section[2]/div[2]/div[2]/div/div/ins").click()

#点击删除按钮
driver.find_element_by_xpath("/html/body/section[2]/div[3]/div[2]").click()
sctc = driver.find_element_by_xpath("/html/body/section[2]/div[4]/div[2]").is_displayed()
assert sctc == True

#确定删除
driver.find_element_by_xpath("/html/body/section[2]/div[4]/div[2]/div/span[2]").click()
print("成功删除关注的股票")
time.sleep(2)

#点击完成按钮
driver.find_element_by_xpath("/html/body/section[2]/div[3]/div[3]").click()
assert driver.find_element_by_xpath("/html/body/section[1]/div[1]/span[1]").is_displayed() == True
print("返回到智能监控页面")

#返回自定义设置页面
driver.back()
assert driver.current_url == "https://eq.10jqka.com.cn/newscenter/main.html"
print("返回到自定义设置页面")


#点击使用须知
driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div[2]/ul/li[2]/p/span[2]").click()
time.sleep(2)
assert driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div[3]/div/div[1]/h5").is_displayed() == True
print("点击使用须知打开弹窗")
time.sleep(2)

#点击我知道了
driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div[3]/div/div[1]/span/a[2]").click()
time.sleep(2)
assert driver.find_element_by_xpath("//*[@id=\"customSetColumn\"]/div[3]/div/div[1]/h5").is_displayed() == False
#assert driver.find_element_by_class_name("cjAlertCon tradeBox").is_displayed() == False
print("点击我知道了关闭弹窗")
time.sleep(2)

driver.refresh()
assert driver.current_url == "https://eq.10jqka.com.cn/newscenter/main.html"
print("刷新回到消息中心")


driver.quit()
print("关闭标签页")