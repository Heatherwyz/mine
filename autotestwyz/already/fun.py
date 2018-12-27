# -*- coding:utf-8 -*-

import json
import os
import sys
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def login(uname, upassword):
    # 设置浏览器属性
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # 设置为无头模式
    chrome_options.add_argument('--disable-gpu')  # 设置为不使用gpu
    chrome_options.add_argument("window-size=1024,768")  # 设置浏览器默认窗口大小
    chrome_options.add_argument("--no-sandbox")  # 设置沙盒模式
    d = webdriver.Chrome(chrome_options=chrome_options)
    d.set_window_size(375, 812)  # 设置浏览器窗口大小
    d.implicitly_wait(10)  # 设置隐式等待时间为10s

    d.get("http://upass.10jqka.com.cn/login?platform=phone#")  # 跳转至登录页

    try:
        element = WebDriverWait(d, 10).until(EC.invisibility_of_element_located((By.ID, "captchaContainer")))
    except Exception as e:
        d.quit()
        raise UserWarning("出现验证码")
    else:
        d.find_element_by_id("username").send_keys(uname)  # 将函数的uname参数作为用户名输入
        d.find_element_by_id("password").send_keys(upassword)  # 将函数的upassword参数作为密码输入

        d.find_element_by_id("submit").click()  # 点击登录按钮

        # print (driver.current_url)  # 输出当前页面的url
        cookies = d.get_cookies()  # 获取当前的cookies
        filename = uname + '_' + time.strftime('%Y%m%d', time.localtime(time.time()))  # 生成文件名：用户名_日期
        josn_cookie = json.dumps(cookies)  # 将获取到的cookie转换为json格式
        file = open(filename, "w")  # 将转换后的cookie写入'用户名_日期'为文件名的文件中
        file.write(josn_cookie)
        file.close()

        d.quit()


def loadCookie(driver, uname, upassword):
    # 获取cookie文件名
    filename = uname + '_' + time.strftime('%Y%m%d', time.localtime(time.time()))
    if not os.path.exists(filename):
        login(uname, upassword)
    # 加载cookie，并刷新页面
    file = open(filename, "r")
    cookies = json.loads(file.read())
    file.close()
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()


def get_today(ele):
    # 判断特定的数据是否更新
    localtime = time.localtime(time.time())  # 获取当前的时间戳
    if localtime.tm_hour < 15:  # 判断当前的时间是否是15点之前
        yesterday = time.strftime("%m-%d", time.localtime(time.time() - 86400))  # 获取昨天的日期，并用“月-日”的格式输出
        if ele.text == '更新于 ' + yesterday:  # 进行字符串拼接，并和元素文案进行比较
            return "昨日已更新"
        else:
            return "昨日未更新"
    else:
        today = time.strftime("%m-%d")  # 获取今天的日期，并用“月-日”的格式输出
        if ele.text == '更新于 ' + today:  # 进行字符串拼接，并和元素文案进行比较
            return "今日已更新"
        else:
            return "今日未更新"


def get_color(ele):
    # 根据涨跌幅判断字体颜色是否正确
    color = ele.value_of_css_property('color')  # 获取当前字体的颜色
    if float(ele.text.strip('%')) < 0:  # 判断元素的涨跌幅是否小于0(去除百分号%)
        yanse = 'rgba(0, 153, 0, 1)'  # rgba(0, 153, 0, 1)为绿色
    elif float(ele.text.strip('%')) > 0:  # 判断元素的涨跌幅是否大于0(去除百分号%)
        yanse = 'rgba(233, 48, 48, 1)'  # rgba(233, 48, 48, 1)为红色
    else:
        yanse = 'rgba(50, 50, 50, 1)'  # rgba(50, 50, 50, 1)为黑灰色
    if color == yanse:  # 判断当前元素颜色和通过涨跌幅得到的颜色是否一致，并输出结果
        return '颜色正确 '
    else:
        return '颜色错误，应为：' + yanse + '，实际为：' + color


def gettype(key_type):
    # 根据元素的类型来定义查找方式
    if key_type == 'id':
        return By.ID
    elif key_type == 'name':
        return By.NAME
    elif key_type == 'classname':
        return By.CLASS_NAME
    elif key_type == 'xpath':
        return By.XPATH


def doaction(element, action):
    if action == "click":
        element.click()
    if action == "type":
        element.type()


def find_element(driver, ele_type, ele_value):
    # 元素查找函数封装
    # 输入：浏览器driver及元素类型和值
    # 输出：元素成功找到返回元素本身，否则返回异常信息(字符串)
    key_type = gettype(ele_type)
    try:
        # 查找元素是否存在
        ele = WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((key_type, ele_value)))
    except Exception as e:
        # 捕捉查找元素的异常，并
        return repr(e)
    else:
        return ele


def wait_ele_close(driver, ele_type, ele_value):
    # 元素查找函数封装，适用于等待指定元素消失/隐藏
    key_type = gettype(ele_type)
    try:
        ele = WebDriverWait(driver, 10, 0.5).until(EC.invisibility_of_element_located((key_type, ele_value)))
    except Exception as e:
        # 捕捉查找元素的异常，并返回异常信息(字符串)
        # 如果这里出现元素超时，应该是该元素一直显示未消失
        return repr(e)


def back_to_lastpage(driver):
    # 返回上一级页面
    driver.back()
    time.sleep(3)


def get_jiekou(url):
    # 根据url获取接口数据
    # 输入：接口url地址
    # 输出：接口返回的json转换后的字典
    import urllib.request
    from io import BytesIO
    import gzip

    headers = {
        'Host': 'vaserviece.10jqka.com.cn',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Accept': 'application/json',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'user=MDphdXRvdGVzdHp6OjpOb25lOjUwMDozOTYxOTkyNTk6NywxMTExMTExMTExMSw0MDs0NCwxMSw0MDs2LDEsNDA7NSwxLDQwOzEsMSw0MDsyLDEsNDA7MywxLDQwOzUsMSw0MDs4LDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxLDQwOjI0Ojo6Mzg2MTk5MjU5OjE1MzQyOTk0NTU6OjoxNDkwMzQyMTYwOjQwMjE0NTowOjEyYTY0MGJhYWRlMTIxMWQwYzI3MTIyNjgyODVmZGYzODpkZWZhdWx0XzI6MA%3D%3D; userid=386199259; u_name=autotestzz; escapename=autotestzz; ticket=d7a10d9e3db57c4df6c3d88338556fd4; hxmPid=pdt_pms_193_hot; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1534211656,1534297292,1534299428,1534387515; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1534387515; v=AhWDvQc54iDmSsbc4lAMwjP_JBrMEskmk8ateJe60Qzb7jtMX2LZ9CMWvU4k'
    }

    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    page = response.read()
    buff = BytesIO(page)  # 把content转为文件对象
    f = gzip.GzipFile(fileobj=buff)
    res = f.read().decode('utf-8')
    return json.loads(res)


def get_jyr(date):
    # 判断一个日期是否是交易日
    # 输入：要判断的日期，两位数月份+两位数日期，例如：0906     注意：无需输入年份，默认是当年
    # 输出：日期判断结果。True为是交易日，False为不是交易日

    year = time.strftime("%Y")  # 获取当前的年份
    filename_for_jyr = 'jyr_' + year
    if not os.path.exists(filename_for_jyr):
        url = 'http://testm.10jqka.com.cn/autotest/test/dxf/getjyr.php'
        request = urllib.request.Request(url=url)
        response = urllib.request.urlopen(request)
        buff = response.read()
        html = buff.decode("utf8")
        response.close()
        fo = open(filename_for_jyr, "w")
        fo.write(html)
        fo.close()
        arr = json.loads(html)
    else:
        fo = open(filename_for_jyr, "r+")
        str = fo.read()
        fo.close()
        arr = json.loads(str)

    if date in arr:
        return True
    else:
        return False
