# -*- coding:utf-8 -*-
import fun
import json, os
import sys
import time
import logging

t1 = time.time()
# reload(sys)

# sys.setdefaultencoding('utf8')
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument("window-size=1024,768")
# chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument(
    "--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E302 IHexin/10.30.10 (Royal Flush) userid/386199259 innerversion/I037.08.334 build/10.30.13 hxtheme/1 hxFont/normal VoiceAssistantVer/0 hxnoimage/0")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.set_window_size(375, 812)  # 设置浏览器窗口大小

# 跳转url
driver.get("https://vaserviece.10jqka.com.cn/mobilecfxf/prime/v2/index.html")

# 加载cookie，并刷新页面
sys.argv = ["autotestzz", "ths123"]
fun.loadCookie(driver, sys.argv[0], sys.argv[1])  # sys.argv[1]为用户名，sys.argv[2]为账号密码
# 财富先锋首页-加载动画
ele1 = fun.wait_ele_close(driver, 'classname', 'loading-now')
if ele1:
    print(ele1 + '，加载动画未消失')

# 财富先锋首页-数据接口
homepage_dict = fun.get_jiekou('http://vaserviece.10jqka.com.cn/mobilecfxf/prime/getInfo.php?op=index')

# 财富先锋首页-财富大盘-左上标题，‘财富大盘’
ele2 = fun.find_element(driver, 'xpath', '//*[@id="wrap"]/section[1]/h2/span')
if type(ele2) == str:
    print("首页财富大盘模块左上标题元素查找异常，" + ele2)
else:
    if ele2.text != "财富大盘":
        print("首页财富大盘模块左上标题文案错误")

# 财富先锋首页-财富大盘-右上副标题，‘大盘资讯 资金动态 赚钱效应’
ele3 = fun.find_element(driver, 'xpath', '//*[@id="wrap"]/section[1]/h2/ins')
if type(ele3) == str:
    print("首页财富大盘模块右上标题元素查找异常，" + ele3)
else:
    if ele3.text != "大盘资讯 资金动态 赚钱效应":
        print("首页财富大盘模块右上副标题文案错误")
    # 跳转财富大盘页面
    ele3.click()
    # 财富大盘页面-大盘趋势分析-标题
    cfdp1 = fun.find_element(driver, 'xpath', '//*[@id="root"]/div/div[1]/div[2]/h3')
    if type(cfdp1) == str:
        print("财富大盘页面大盘趋势分析标题元素查找异常，" + cfdp1)
    else:
        if cfdp1.text != "大盘趋势分析":
            print("财富大盘页面大盘趋势分析标题文案错误")
    # 财富大盘页面-大盘趋势-按钮
    cfdp2 = fun.find_element(driver, 'xpath', '//*[@id="root"]/div/div[1]/div[1]')
    if type(cfdp2) == str:
        print("财富大盘页面大盘趋势按钮元素查找异常，" + cfdp2)
    else:
        if cfdp2.text != "大盘趋势":
            print("财富大盘页面大盘趋势分析标题文案错误")
    # 财富大盘页面-大盘资讯标签
    cfdp3 = fun.find_element(driver, 'xpath',
                             '//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div')
    if type(cfdp3) == str:
        print("财富大盘页面大盘资讯标签元素查找异常，" + cfdp3)
    else:
        cfdp3.click()
        if cfdp3.text != "大盘资讯":
            print("财富大盘页面大盘资讯标签文案错误")
        # 财富大盘页面-大盘资讯标签-第一条数据
        cfdp4 = fun.find_element(driver, 'xpath', '//*[@id="root"]/div/div[3]/div[1]/div/div[2]/div[1]/div/div[1]')
        if type(cfdp4) == str:
            print("财富大盘页面大盘资讯标签第一条数据元素查找异常，" + cfdp4)
    # 财富大盘页面-资金动态标签
    cfdp5 = fun.find_element(driver, 'xpath',
                             '//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div/div[2]/div/div/div[2]/div')
    if type(cfdp5) == str:
        print("财富大盘页面资金动态标签元素查找异常，" + cfdp5)
    else:
        cfdp5.click()
        if cfdp5.text != "资金动态":
            print("财富大盘页面资金动态标签文案错误")
        # 财富大盘页面-大盘资讯标签-拓赢资金
        cfdp6 = fun.find_element(driver, 'xpath', '//*[@id="root"]/div/div[3]/div[1]/div/div[2]/div[2]/div/div[1]')
        if type(cfdp6) == str:
            print("财富大盘页面资金动态标签拓赢资金元素查找异常，" + cfdp6)
        # 财富大盘页面-大盘资讯标签-融资买入
        cfdp7 = fun.find_element(driver, 'xpath', '//*[@id="root"]/div/div[3]/div[1]/div/div[2]/div[2]/div/div[2]')
        if type(cfdp7) == str:
            print("财富大盘页面资金动态标签融资买入元素查找异常，" + cfdp7)
        # 财富大盘页面-大盘资讯标签-融资买入
        cfdp8 = fun.find_element(driver, 'xpath', '//*[@id="root"]/div/div[3]/div[1]/div/div[2]/div[2]/div/div[3]')
        if type(cfdp8) == str:
            print("财富大盘页面资金动态标签场外资金元素查找异常，" + cfdp8)
    # 财富大盘页面-赚钱效应标签
    cfdp9 = fun.find_element(driver, 'xpath',
                             '//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div/div[2]/div/div/div[3]/div')
    if type(cfdp9) == str:
        print("财富大盘页面赚钱效应标签元素查找异常，" + cfdp9)
    else:
        cfdp9.click()
        if cfdp9.text != "赚钱效应":
            print("财富大盘页面赚钱效应标签文案错误")
        # 财富大盘页面-赚钱效应标签-涨停效应
        cfdp10 = fun.find_element(driver, 'xpath', '//*[@id="root"]/div/div[3]/div[1]/div/div[2]/div[3]/div/div[1]')
        if type(cfdp10) == str:
            print("财富大盘页面赚钱效应标签涨停效应元素查找异常，" + cfdp10)
        # 财富大盘页面-赚钱效应标签-热点效应
        cfdp11 = fun.find_element(driver, 'xpath', '//*[@id="root"]/div/div[3]/div[1]/div/div[2]/div[3]/div/div[2]')
        if type(cfdp11) == str:
            print("财富大盘页面赚钱效应标签热点效应元素查找异常，" + cfdp11)
        # 财富大盘页面-赚钱效应标签-分化效应
        cfdp12 = fun.find_element(driver, 'xpath', '//*[@id="root"]/div/div[3]/div[1]/div/div[2]/div[3]/div/div[3]')
        if type(cfdp12) == str:
            print("财富大盘页面赚钱效应标签分化效应元素查找异常，" + cfdp12)
        # 财富大盘页面-赚钱效应标签-涨跌效应
        cfdp13 = fun.find_element(driver, 'xpath', '//*[@id="root"]/div/div[3]/div[1]/div/div[2]/div[3]/div/div[4]')
        if type(cfdp13) == str:
            print("财富大盘页面赚钱效应标签涨跌效应元素查找异常，" + cfdp13)
    # 返回到上一级页面-财富先锋首页
    fun.back_to_lastpage(driver)

# 财富先锋首页-财富大盘-大盘趋势分析-标题，‘大盘趋势分析’
ele4 = fun.find_element(driver, 'xpath', '//*[@id="wrap"]/section[1]/div/h3')
if type(ele4) == str:
    print("大盘趋势分析标题元素查找异常，" + ele4)
else:
    if ele4.text != "大盘趋势分析":
        print("大盘趋势分析标题文案错误")

# 财富先锋首页-财富大盘-大盘趋势分析-内容标题
ele5 = fun.find_element(driver, 'xpath', '//*[@id="wrap"]/section[1]/div/h4')
if type(ele5) == str:
    print("大盘趋势分析内容标题元素查找异常，" + ele5)
else:
    if ele5.text != homepage_dict['data']['stockMarket']['summary']:
        print("大盘趋势分析内容标题文案错误，与接口返回不符。应为：" + homepage_dict['data']['stockMarket']['summary'] + " ，实际为：" + ele5.text)

# 财富先锋首页-财富大盘-大盘趋势分析-内容
ele6 = fun.find_element(driver, 'xpath', '//*[@id="wrap"]/section[1]/div/p')
if type(ele6) == str:
    print("大盘趋势分析内容标题元素查找异常，" + ele6)
else:
    if ele6.text != homepage_dict['data']['stockMarket']['analysis']:
        print("大盘趋势分析内容文案错误，与接口返回不符。")

# 财富先锋首页-财富热点-左上标题，‘财富热点’
ele7 = fun.find_element(driver, 'xpath', '//*[@id="wrap"]/section[2]/h2/span')
if type(ele7) == str:
    print("首页财富热点模块左上标题元素查找异常，" + ele7)
else:
    if ele7.text != "财富热点":
        print("首页财富热点模块左上标题文案错误")

# 财富先锋首页-财富热点-右上副标题，‘大盘资讯 资金动态 赚钱效应’
ele8 = fun.find_element(driver, 'xpath', '//*[@id="wrap"]/section[2]/h2/ins')
if type(ele8) == str:
    print("首页财富热点模块右上标题元素查找异常，" + ele8)
else:
    if ele8.text != "拓赢板块 热点事件 潜在机会":
        print("首页财富热点模块右上副标题文案错误，应为<拓赢板块 热点事件 潜在机会>，实际为<" + ele8.text + '>')
    # 跳转财富热点页面
    ele8.click()
    # 财富热点页面-拓赢板块标签
    cfrd1 = fun.find_element(driver, 'xpath', '/html/body/section[1]/div/p[1]')
    if type(cfrd1) == str:
        print("财富热点页面拓赢板块标签元素查找异常，" + cfrd1)
    else:
        cfrd1.click()
        if cfrd1.text != "拓赢板块":
            print("财富热点页面拓赢板块标签文案错误")
        # 财富热点页面-拓赢板块标签-概念板块标签
        cfrd2 = fun.find_element(driver, 'xpath', '//*[@id="tybk"]/div[1]/div[1]/p[1]')
        if type(cfrd2) == str:
            print("财富热点页面拓赢板块-概念板块标签元素查找异常，" + cfrd2)
        else:
            cfrd2.click()
            if cfrd2.text != "概念板块":
                print("财富热点页面拓赢板块-概念板块标签文案错误")
            # 财富热点页面-拓赢板块标签-概念板块标签-板块列表第一条
            cfrd2_list1 = fun.find_element(driver, 'xpath', '//*[@id="concept"]/div[1]')
            if type(cfrd2_list1) == str:
                print("财富热点页面拓赢板块-概念板块列表第一条元素查找异常，" + cfrd2_list1)
            else:
                # 财富热点页面-拓赢板块标签-概念板块标签-板块列表第一条-股票列表第一条
                cfrd2_list1_child1 = fun.find_element(driver, 'xpath', '//*[@id="concept"]/div[1]/div[2]/div[2]')
                if type(cfrd2_list1_child1) == str:
                    print("财富热点页面拓赢板块-概念板块标签-板块列表第一条的第一只股票元素查找异常，" + cfrd2_list1_child1)
                else:
                    cfrd2_list1_child1_zdf = cfrd2_list1_child1.find_element_by_xpath('p[2]/span')
                    # print('财富热点页面拓赢板块-概念板块标签-板块列表第一条的第一只股票涨跌幅'+fun.get_color(cfrd2_list1_child1_zdf))
        # 财富热点页面-拓赢板块标签-行业板块标签
        cfrd3 = fun.find_element(driver, 'xpath', '//*[@id="tybk"]/div[1]/div[1]/p[2]')
        if type(cfrd3) == str:
            print("财富热点页面拓赢板块-行业板块标签元素查找异常，" + cfrd3)
        else:
            cfrd3.click()
            if cfrd3.text != "行业板块":
                print("财富热点页面拓赢板块-行业板块标签文案错误")
            # 财富热点页面-拓赢板块标签-行业板块标签-板块列表第一条
            cfrd3_list1 = fun.find_element(driver, 'xpath', '//*[@id="industry"]/div[1]')
            if type(cfrd3_list1) == str:
                print("财富热点页面拓赢板块-行业板块列表第一条元素查找异常，" + cfrd3_list1)
            else:
                # 财富热点页面-拓赢板块标签-行业板块标签-板块列表第一条-股票列表第一条
                cfrd3_list1_child1 = fun.find_element(driver, 'xpath', '//*[@id="industry"]/div[1]/div[2]/div[2]')
                if type(cfrd3_list1_child1) == str:
                    print("财富热点页面拓赢板块-行业板块标签-板块列表第一条的第一只股票元素查找异常，" + cfrd3_list1_child1)
                else:
                    cfrd3_list1_child1_zdf = cfrd3_list1_child1.find_element_by_xpath('p[2]/span')
                    # print('财富热点页面拓赢板块-行业板块标签-板块列表第一条的第一只股票涨跌幅' + fun.get_color(cfrd3_list1_child1_zdf))
        # 财富热点页面-拓赢板块标签-地域板块标签
        cfrd4 = fun.find_element(driver, 'xpath', '//*[@id="tybk"]/div[1]/div[1]/p[3]')
        if type(cfrd4) == str:
            print("财富热点页面拓赢板块-地域板块标签元素查找异常，" + cfrd4)
        else:
            cfrd4.click()
            if cfrd4.text != "地域板块":
                print("财富热点页面拓赢板块-地域板块标签文案错误")
            # 财富热点页面-拓赢板块标签-地域板块标签-板块列表第一条
            cfrd4_list1 = fun.find_element(driver, 'xpath', '//*[@id="region"]/div[1]')
            if type(cfrd4_list1) == str:
                print("财富热点页面拓赢板块-地域板块列表第一条元素查找异常，" + cfrd4_list1)
            else:
                # 财富热点页面-拓赢板块标签-地域板块标签-板块列表第一条-股票列表第一条
                cfrd4_list1_child1 = fun.find_element(driver, 'xpath', '//*[@id="region"]/div[1]/div[2]/div[2]')
                if type(cfrd4_list1_child1) == str:
                    print("财富热点页面拓赢板块-地域板块标签-板块列表第一条的第一只股票元素查找异常，" + cfrd4_list1_child1)
                else:
                    cfrd4_list1_child1_zdf = cfrd4_list1_child1.find_element_by_xpath('p[2]/span')
                    # print('财富热点页面拓赢板块-地域板块标签-板块列表第一条的第一只股票涨跌幅' + fun.get_color(cfrd4_list1_child1_zdf))
    # 财富热点页面-热点事件标签
    cfrd5 = fun.find_element(driver, 'xpath', '/html/body/section[1]/div/p[2]')
    if type(cfrd5) == str:
        print("财富热点页面热点事件标签元素查找异常，" + cfrd5)
    else:
        cfrd5.click()
        # 财富热点页面-热点事件标签-全部类型列表-第一条数据
        cfrd5_child = fun.find_element(driver, 'xpath', '//*[@id="contentContainer"]/div[2]/div[1]/div[1]')
        if type(cfrd5_child) == str:
            print("财富热点页面热点事件标签全部类型列表-第一条数据元素查找异常，" + cfrd5_child)
    # 财富热点页面-潜在机会标签
    cfrd6 = fun.find_element(driver, 'xpath', '/html/body/section[1]/div/p[3]')
    if type(cfrd6) == str:
        print("财富热点页面潜在机会标签元素查找异常，" + cfrd6)
    else:
        cfrd6.click()
        # 财富热点页面-潜在机会标签-第一条数据
        cfrd6_child = fun.find_element(driver, 'xpath', '//*[@id="qzjh"]/div[2]/div[4]/div[1]')
        if type(cfrd6_child) == str:
            print("财富热点页面潜在机会标签列表第一条数据元素查找异常，" + cfrd6_child)
    # 返回到上一级页面-财富先锋首页
    fun.back_to_lastpage(driver)

# 财富先锋首页-财富热点-板块热点-板块列表第一条
ele9 = fun.find_element(driver, 'xpath', '//*[@id="wrap"]/section[2]/ul/li[1]/div')
if type(ele9) == str:
    print("首页财富热点模块板块热点板块列表第一条元素查找异常，" + ele9)
else:
    # 财富先锋首页-财富热点-板块热点-板块列表第一条-数据校验
    ele9_child1 = ele9.find_element_by_xpath('span[1]')
    if ele9_child1.text != homepage_dict['data']['hot'][0]['plate']:
        print("首页财富热点模块板块热点板块列表第一条板块名错误，与接口返回不符。应为：" + homepage_dict['data']['hot'][0][
            'plate'] + " ，实际为：" + ele9_child1.text)
    ele9_child2 = ele9.find_element_by_xpath('span[2]')
    if ele9_child2.text != homepage_dict['data']['hot'][0]['percent']:
        print("首页财富热点模块板块热点板块列表第一条涨跌幅错误，与接口返回不符。应为：" + homepage_dict['data']['hot'][0][
            'percent'] + " ，实际为：" + ele9_child2.text)
    # 校验涨跌幅的字体颜色
    print('首页财富热点模块板块热点板块列表第一条涨跌幅' + fun.get_color(ele9_child2))
    ele9_child3 = ele9.find_element_by_xpath('span[3]')
    if ele9_child3.text != homepage_dict['data']['hot'][0]['superOrganizationTotal']:
        print("首页财富热点模块板块热点板块列表第一条超级机构数值错误，与接口返回不符。应为：" + homepage_dict['data']['hot'][0][
            'superOrganizationTotal'] + " ，实际为：" + ele9_child3.text)
    ele9_child4 = ele9.find_element_by_xpath('span[4]')
    if ele9_child4.text != homepage_dict['data']['hot'][0]['organizationTotal']:
        print("首页财富热点模块板块热点板块列表第一条机构数值错误，与接口返回不符。应为：" + homepage_dict['data']['hot'][0][
            'organizationTotal'] + " ，实际为：" + ele9_child4.text)
    # 点击板块列表第一条展开股票列表
    ele9.click()
    # 财富先锋首页-财富热点-板块热点-板块列表-股票列表第一条
    ele10 = fun.find_element(driver, 'xpath', '//*[@id="wrap"]/section[2]/ul/li[1]/ul/li[2]')
    if type(ele10) == str:
        print("首页财富热点模块板块热点板块列表第一条元素查找异常，" + ele10)
    else:
        # 财富先锋首页-财富热点-板块热点-板块列表-股票列表第一条-数据校验
        ele10_child1 = ele10.find_element_by_xpath('//*[@id="wrap"]/section[2]/ul/li[1]/ul/li[2]/p[1]/span')
        if ele10_child1.text != homepage_dict['data']['hot'][0]['detail'][0]['stockName']:
            print("首页财富热点模块板块热点板块列表第一个板块股票列表第一条股票名错误，与接口返回不符。应为：" +
                  homepage_dict['data']['hot'][0]['detail'][0]['stockName'] + " ，实际为：" + ele10_child1.text)
        ele10_child2 = ele10.find_element_by_xpath('p[1]/ins')
        if ele10_child2.text != homepage_dict['data']['hot'][0]['detail'][0]['stockCode']:
            print("首页财富热点模块板块热点板块列表第一个板块股票列表第一条股票代码错误，与接口返回不符。应为：" +
                  homepage_dict['data']['hot'][0]['detail'][0]['stockCode'] + " ，实际为：" + ele10_child2.text)
        ele10_child3 = ele10.find_element_by_xpath('p[2]/b')
        if ele10_child3.text != homepage_dict['data']['hot'][0]['detail'][0]['stockCode']:
            print("首页财富热点模块板块热点板块列表第一个板块股票列表第一条现价错误，与接口返回不符。应为：" +
                  homepage_dict['data']['hot'][0]['detail'][0]['price'] + " ，实际为：" + ele10_child3.text)

# 财富先锋首页-财富策略-左上标题，‘财富策略’
ele11 = fun.find_element(driver, 'xpath', '//*[@id="wrap"]/section[3]/h2/span')
if type(ele11) == str:
    print("首页财富策略模块左上标题元素查找异常，" + ele11)
else:
    if ele11.text[0:4] != "财富策略":
        print("首页财富策略模块左上标题文案错误，应为<财富策略>，实际为<" + ele11.text[0:4] + ">")

# 财富先锋首页-财富策略-右上副标题，‘全部财富策略’
ele12 = fun.find_element(driver, 'xpath', '//*[@id="wrap"]/section[3]/h2/ins')
if type(ele12) == str:
    print("首页财富策略模块右上标题元素查找异常，" + ele12)
else:
    if ele12.text != "全部财富策略":
        print("首页财富策略模块右上副标题文案错误，应为<全部财富策略>，实际为<" + ele12.text + '>')
    # 跳转财富策略页面
    ele12.click()
    # 财富策略页面-股票跟踪与指导
    cfcl1 = fun.find_element(driver, 'xpath', '/html/body/div[1]/a')
    if type(cfcl1) == str:
        print("财富策略页面-股票跟踪与指导元素查找异常，" + cfcl1)
    else:
        # 跳转至股票跟踪与指导页面
        cfcl1.click()
        gpgz_list_1 = fun.find_element(driver, 'xpath', '//*[@id="followstock"]/tr[1]')
        if type(gpgz_list_1) == str:
            print("财富策略页面-股票跟踪与指导页面-第一只股票元素查找异常，" + gpgz_list_1)
        # 返回财富策略页面
        fun.back_to_lastpage(driver)
    # 财富策略页面-财富策略选股
    cfcl2 = fun.find_element(driver, 'xpath', '/html/body/div[2]')
    if type(cfcl2) == str:
        print("财富策略页面-财富策略选股元素查找异常，" + cfcl2)
    else:
        # 财富策略页面-财富策略选股-左上标题
        cfcl3 = fun.find_element(driver, 'xpath', '/html/body/div[2]/h3')
        if type(cfcl3) == str:
            print("财富策略页面-财富策略选股左上标题元素查找异常，" + cfcl3)
        else:
            if cfcl3.text != "财富策略选股":
                print("财富策略页面-财富策略选股左上标题文案错误，应为<财富策略选股>，实际为<" + cfcl3.text + '>')
        # 财富策略页面-财富策略选股-短线策略选股-分时突破选股
        cfcl4 = fun.find_element(driver, 'xpath', '/html/body/div[2]/a[1]')
        if type(cfcl4) == str:
            print("财富策略页面-财富策略选股-短线策略选股-分时突破选股元素查找异常，" + cfcl4)
        else:
            cfcl4_title = cfcl4.find_element_by_xpath('h3')
            if cfcl4_title.text != "分时突破选股独家":
                print("财富策略页面-财富策略选股-短线策略选股-分时突破选股标题文案错误，应为<分时突破选股>，实际为<" + cfcl4_title.text + '>')
            # 跳转至分时突破选股页面
            cfcl4_title.click()
            # 分时突破页面-选择条件-统计时间-开盘到现在按钮
            fstp_time_now = fun.find_element(driver, 'id', 'timenow')
            if type(fstp_time_now) == str:
                print("分时突破页面-选择条件-统计时间-开盘到现在按钮元素查找异常，" + fstp_time_now)
            else:
                fstp_time_now.click()
            # 分时突破页面-选择条件-信号类型-突或积按钮
            fstp_type_tuorji = fun.find_element(driver, 'id', 'infotuorji')
            if type(fstp_type_tuorji) == str:
                print("分时突破页面-选择条件-信号类型-突或积按钮元素查找异常，" + fstp_type_tuorji)
            else:
                fstp_type_tuorji.click()
            # 分时突破页面-选择条件-执行选股按钮
            fstp_button = fun.find_element(driver, 'xpath', '/html/body/div[1]/a')
            if type(fstp_button) == str:
                print("分时突破页面-选择条件-执行选股按钮元素查找异常，" + fstp_button)
            else:
                fstp_button.click()
                # 分时突破页面-选股结果-加载动画
                fstp_loading = fun.wait_ele_close(driver, 'xpath', '//*[@id="quotetuandji"]/tr/td/img')
                if fstp_loading:
                    print("分时突破页面-选股结果-加载动画未消失")
                else:
                    # 分时突破页面-选股结果
                    fstp_result = fun.find_element(driver, 'xpath', '//*[@id="quotetuandji"]/tr/td')
                    if type(fstp_result) == str:
                        print("分时突破页面-选股结果元素查找异常，" + fstp_result)
                    else:
                        if fstp_result.text == '暂无符合条件的股票，请注意股市风险！':
                            print("分时突破页面-选股结果为空")
                        else:
                            # 分时突破页面-选股结果-第一只股票
                            fstp_result_1 = fun.find_element(driver, 'xpath', '//*[@id="quotetuandji"]/tr[1]')
                            if type(fstp_result_1) == str:
                                print("分时突破页面-选股结果-第一只股票元素查找异常")
            # 返回财富策略页面
            fun.back_to_lastpage(driver)
        # 财富策略页面-财富策略选股-短线策略选股-超级机构
        cfcl5 = fun.find_element(driver, 'xpath', '/html/body/div[2]/a[2]')
        if type(cfcl5) == str:
            print("财富策略页面-财富策略选股-短线策略选股-超级机构元素查找异常，" + cfcl5)
        else:
            cfcl5_title = cfcl5.find_element_by_xpath('h3')
            if cfcl5_title.text != "超级机构":
                print("财富策略页面-财富策略选股-短线策略选股-超级机构标题文案错误，应为<超级机构>，实际为<" + cfcl5_title.text + '>')
            # 跳转至超级机构页面
            cfcl5_title.click()
            # 超级机构页面-日期
            cjjg_date = fun.find_element(driver, 'id', 'todaydate')
            if type(cjjg_date) == str:
                print("超级机构页面-日期元素查找异常，" + cjjg_date)
            else:
                # 判断日期是否是交易日
                if fun.get_jyr(cjjg_date.text[4:8]):
                    print("超级机构页面-日期" + cjjg_date.text + "是交易日")
                else:
                    print("超级机构页面-日期" + cjjg_date.text + "不是交易日")
                # 超级机构页面-选股结果-加载动画
                cjjg_loading = fun.wait_ele_close(driver, 'xpath', '//*[@id="selecteddisplayinfo"]/tr/td/img')
                if cjjg_loading:
                    print("超级机构页面-选股结果-加载动画未消失")
                else:
                    # 超级机构页面-选股结果
                    cjjg_result = fun.find_element(driver, 'xpath', '//*[@id="selecteddisplayinfo"]/tr[1]/td')
                    if type(cjjg_result) == str:
                        print("超级机构页面-选股结果元素查找异常，" + cjjg_result)
                    else:
                        if cjjg_result.text == '由于股市行情不佳，暂无符合条件的股票，请注意股市风险！':
                            print("超级机构页面-选股结果为空")
                        else:
                            # 超级机构页面-选股结果-第一只股票
                            cjjg_result_1 = fun.find_element(driver, 'xpath', '//*[@id="selecteddisplayinfo"]/tr[1]')
                            if type(cjjg_result_1) == str:
                                print("超级机构页面-选股结果-第一只股票元素查找异常")
            # 返回财富策略页面
            fun.back_to_lastpage(driver)
        # 财富策略页面-财富策略选股-短线策略选股-主力决策
        cfcl6 = fun.find_element(driver, 'xpath', '/html/body/div[2]/a[3]')
        if type(cfcl6) == str:
            print("财富策略页面-财富策略选股-短线策略选股-主力决策元素查找异常，" + cfcl6)
        else:
            cfcl6_title = cfcl6.find_element_by_xpath('h3')
            if cfcl6_title.text != "主力决策":
                print("财富策略页面-财富策略选股-短线策略选股-主力决策标题文案错误，应为<主力决策>，实际为<" + cfcl6_title.text + '>')
            # 跳转至主力决策页面
            cfcl6_title.click()
            # 主力决策页面-日期
            zljc_date = fun.find_element(driver, 'id', 'todaydate')
            if type(zljc_date) == str:
                print("主力决策页面-日期元素查找异常，" + zljc_date)
            else:
                # 判断日期是否是交易日
                if fun.get_jyr(zljc_date.text[4:8]):
                    print("主力决策页面-日期" + zljc_date.text + "是交易日")
                else:
                    print("主力决策页面-日期" + zljc_date.text + "不是交易日")
            # 主力决策页面-选股结果-加载动画
            zljc_loading = fun.wait_ele_close(driver, 'xpath', '//*[@id="selecteddisplayinfo"]/tr/td/img')
            if zljc_loading:
                print("主力决策页面-选股结果-加载动画未消失")
            else:
                # 主力决策页面-选股结果
                zljc_result = fun.find_element(driver, 'xpath', '//*[@id="selecteddisplayinfo"]/tr[1]/td')
                if type(zljc_result) == str:
                    print("主力决策页面-选股结果元素查找异常，" + zljc_result)
                else:
                    if zljc_result.text == '由于股市行情不佳，暂无符合条件的股票，请注意股市风险！':
                        print("主力决策页面-选股结果为空")
                    else:
                        # 主力决策页面-选股结果-第一只股票
                        zljc_result_1 = fun.find_element(driver, 'xpath', '//*[@id="selecteddisplayinfo"]/tr[1]')
                        if type(zljc_result_1) == str:
                            print("主力决策页面-选股结果-第一只股票元素查找异常")
            # 返回财富策略页面
            fun.back_to_lastpage(driver)
        # 财富策略页面-财富策略选股-中长线策略选股-云策略选股
        cfcl7 = fun.find_element(driver, 'xpath', '/html/body/div[2]/a[4]')
        if type(cfcl7) == str:
            print("财富策略页面-财富策略选股-短线策略选股-云策略选股元素查找异常，" + cfcl7)
        else:
            cfcl7_title = cfcl7.find_element_by_xpath('h3')
            if cfcl7_title.text != "云策略选股new":
                print("财富策略页面-财富策略选股-短线策略选股-云策略选股标题文案错误，应为<主力决策>，实际为<" + cfcl7_title.text + '>')
            # 跳转至云策略选股页面
            cfcl7_title.click()
            # 云策略选股页面-日期
            ycl_date = fun.find_element(driver, 'id', 'stockdate')
            if type(ycl_date) == str:
                print("云策略选股页面-日期元素查找异常，" + ycl_date)
            else:
                # 判断日期是否是交易日
                if fun.get_jyr(ycl_date.text.replace('-', '')[4:8]):
                    print("云策略选股页面-日期" + ycl_date.text + "是交易日")
                else:
                    print("云策略选股页面-日期" + ycl_date.text + "不是交易日")
                # 云策略选股页面-选股结果
                zljc_result = fun.find_element(driver, 'id', 'stockArea')
                if type(zljc_result) == str:
                    print("云策略选股页面-选股结果元素查找异常，" + zljc_result)
                # xpath中仅有一个table时/table和/table[1]是否等价待验证
            # 返回财富策略页面
            fun.back_to_lastpage(driver)
        # 财富策略页面-财富策略选股-中长线策略选股-价值挖掘
        cfcl8 = fun.find_element(driver, 'xpath', '/html/body/div[2]/a[5]')
        if type(cfcl8) == str:
            print("财富策略页面-财富策略选股-短线策略选股-价值挖掘元素查找异常，" + cfcl8)
        else:
            cfcl8_title = cfcl8.find_element_by_xpath('h3')
            if cfcl8_title.text != "价值挖掘":
                print("财富策略页面-财富策略选股-短线策略选股-云策略选股标题文案错误，应为<价值挖掘>，实际为<" + cfcl8_title.text + '>')
            # 跳转至价值挖掘页面
            cfcl8_title.click()
            # 价值挖掘页面-加载动画
            jzwj_loading = fun.wait_ele_close(driver, 'xpath', '/html/body/div[1]/img')
            if jzwj_loading:
                print("价值挖掘页面-加载动画未消失")
            else:
                # 价值挖掘页面-券商研究标签-板块列表第一条
                jzwj_qsyj_list_1 = fun.find_element(driver, 'xpath', '//*[@id="valuediginfo"]/table/tbody/tr[2]')
                if type(jzwj_qsyj_list_1) == str:
                    print("价值挖掘页面-券商研究标签-板块列表第一条元素查找异常，" + jzwj_qsyj_list_1)
                else:
                    # 点击板块列表展开股票列表
                    jzwj_qsyj_list_1.click()
                    # 价值挖掘页面-券商研究标签-板块列表第一条-股票列表第一条
                    # 发现这里股票列表在页面加载完成的时候就已经写入dom中，继续使用封装的find_element()来查找元素变得毫无作用，应该除了判断是否存在外，还应判断是否可见
            # 返回财富策略页面
            fun.back_to_lastpage(driver)
        # 财富策略页面-财富策略选股-中长线策略选股-内部交易
        cfcl9 = fun.find_element(driver, 'xpath', '/html/body/div[2]/a[6]')
        if type(cfcl9) == str:
            print("财富策略页面-财富策略选股-短线策略选股-内部交易元素查找异常，" + cfcl9)
        else:
            cfcl9_title = cfcl9.find_element_by_xpath('h3')
            if cfcl9_title.text != "内部交易":
                print("财富策略页面-财富策略选股-短线策略选股-内部交易标题文案错误，应为<内部交易>，实际为<" + cfcl9_title.text + '>')
            # 跳转至内部交易页面
            cfcl9_title.click()
            # 内部交易页面-加载动画
            nbjy_loading = fun.wait_ele_close(driver, 'xpath', '/html/body/div[1]/img')
            if nbjy_loading:
                print("内部交易页面-加载动画未消失")
            else:
                # 内部交易页面-市场动向标签-上交所-交易日
                nbjy_scdx_sjs_date = fun.find_element(driver, 'id', 'date')
                if type(nbjy_scdx_sjs_date) == str:
                    print("内部交易页面-市场动向标签-上交所-交易日元素查找异常，" + nbjy_scdx_sjs_date)
                else:
                    # 判断日期是否是交易日
                    if fun.get_jyr(nbjy_scdx_sjs_date.text[4:8]):
                        print("内部交易页面-市场动向标签-上交所-日期" + nbjy_scdx_sjs_date.text + "是交易日")
                    else:
                        print("内部交易页面-市场动向标签-上交所-日期" + nbjy_scdx_sjs_date.text + "不是交易日")
                # 内部交易页面-市场动向标签-上交所标签-大盘指数行情-涨跌幅
                nbjy_scdx_sjs_zdf = fun.find_element(driver, 'id', 'zdf')
                if type(nbjy_scdx_sjs_zdf) == str:
                    print("内部交易页面-市场动向标签-上交所-大盘指数行情-涨跌幅元素查找异常，" + nbjy_scdx_sjs_zdf)
                else:
                    print("内部交易页面-市场动向标签-上交所-大盘指数行情-涨跌幅" + fun.get_color(nbjy_scdx_sjs_zdf))
                # 内部交易页面-市场动向标签-深交所标签
                nbjy_scdx_szs = fun.find_element(driver, 'xpath', '/html/body/div[2]/ul/li[2]/a')
                if type(nbjy_scdx_szs) == str:
                    print("内部交易页面-市场动向标签-深交所标签元素查找异常，" + nbjy_scdx_szs)
                else:
                    # 页面切换至深交所标签
                    nbjy_scdx_szs.click()
                    # 内部交易页面-市场动向标签-深交所标签-加载动画
                    nbjy_scdx_szs_loading = fun.wait_ele_close(driver, 'xpath', '/html/body/div[1]/img')
                    if nbjy_scdx_szs_loading:
                        print("内部交易页面-市场动向标签-深交所标签-加载动画未消失")
                    else:
                        # 内部交易页面-市场动向标签-深交所标签-交易日
                        nbjy_scdx_szs_date = fun.find_element(driver, 'id', 'date')
                        if type(nbjy_scdx_szs_date) == str:
                            print("内部交易页面-市场动向标签-上交所-交易日元素查找异常，" + nbjy_scdx_szs_date)
                        else:
                            # 判断日期是否是交易日
                            if fun.get_jyr(nbjy_scdx_szs_date.text[4:8]):
                                print("内部交易页面-市场动向标签-深交所-日期" + nbjy_scdx_szs_date.text + "是交易日")
                            else:
                                print("内部交易页面-市场动向标签-深交所-日期" + nbjy_scdx_szs_date.text + "不是交易日")
                        # 内部交易页面-市场动向标签-深交所标签-大盘指数行情-涨跌幅
                        nbjy_scdx_szs_zdf = fun.find_element(driver, 'id', 'zdf')
                        if type(nbjy_scdx_szs_zdf) == str:
                            print("内部交易页面-市场动向标签-深交所-大盘指数行情-涨跌幅元素查找异常，" + nbjy_scdx_szs_zdf)
                        else:
                            print("内部交易页面-市场动向标签-深交所-大盘指数行情-涨跌幅" + fun.get_color(nbjy_scdx_szs_zdf))
                        # 内部交易页面-内部增持标签
                        nbjy_nbzc = fun.find_element(driver, 'xpath', '/html/body/div[1]/ul/li[2]')
                        if type(nbjy_nbzc) == str:
                            print("内部交易页面-内部增持标签元素查找异常，" + nbjy_nbzc)
                        else:
                            # 页面切换至内部增持标签
                            nbjy_nbzc.click()
                            # 内部交易页面-内部增持标签-加载动画
                            nbjy_nbzc_loading = fun.wait_ele_close(driver, 'xpath', '/html/body/div[1]/img')
                            if nbjy_nbzc_loading:
                                print("内部交易页面-市场动向标签-深交所标签-加载动画未消失")
                            else:
                                # 内部交易页面-内部增持标签-股东增持-股票列表第一条
                                nbjy_nbzc_gdzc_list_1 = fun.find_element(driver, 'xpath',
                                                                         '/html/body/table/tbody/tr[1]')
                                if type(nbjy_nbzc_gdzc_list_1) == str:
                                    print("内部交易页面-内部增持标签-股东增持-股票列表第一条元素查找异常，" + nbjy_nbzc_gdzc_list_1)
            # 返回财富策略页面
            fun.back_to_lastpage(driver)
    # 返回到上一级页面-财富先锋首页
    fun.back_to_lastpage(driver)

# 财富先锋首页-财富策略-左上更新时间
ele13 = fun.find_element(driver, 'xpath', '//*[@id="wrap"]/section[3]/h2/span/b')
if type(ele13) == str:
    print("首页财富策略模块左上更新时间元素查找异常，" + ele13)
else:
    print(fun.get_today(ele13))

# 财富先锋首页-财富策略-股票列表第一条
ele14 = fun.find_element(driver, 'xpath', '//*[@id="wrap"]/section[3]/ul[2]/li[1]')
if type(ele14) == str:
    print("首页财富策略模块股票列表第一条元素查找异常，" + ele14)
else:
    # 校验股票涨跌幅字体颜色
    ele14_child1 = ele14.find_element_by_xpath('span')
    print('首页财富策略模块股票列表第一条涨跌幅' + fun.get_color(ele14_child1))

# 财富先锋首页-其他功能-左上标题，“其他功能”
ele15 = fun.find_element(driver, 'xpath', '//*[@id="wrap"]/section[4]/h2/span')
if type(ele15) == str:
    print("首页其他功能模块左上标题元素查找异常，" + ele15)
else:
    if ele15.text != "其他功能":
        print("首页其他功能模块左上标题文案错误，应为<其他功能>，实际为<" + ele15.text + '>')

# 财富先锋首页-其他功能-图标列表
ele16 = fun.find_element(driver, 'xpath', '//*[@id="wrap"]/section[4]/ul/li[1]')
if type(ele16) == str:
    print("首页其他功能模块“我的股票”元素查找异常，" + ele16)
ele17 = fun.find_element(driver, 'xpath', '//*[@id="wrap"]/section[4]/ul/li[2]')
if type(ele17) == str:
    print("首页其他功能模块“专属投顾”元素查找异常，" + ele17)
ele18 = fun.find_element(driver, 'xpath', '//*[@id="wrap"]/section[4]/ul/li[3]')
if type(ele18) == str:
    print("首页其他功能模块“高端投资决策”元素查找异常，" + ele18)
ele19 = fun.find_element(driver, 'xpath', '//*[@id="wrap"]/section[4]/ul/li[4]')
if type(ele19) == str:
    print("首页其他功能模块“投顾助手”元素查找异常，" + ele19)
ele20 = fun.find_element(driver, 'xpath', '//*[@id="wrap"]/section[4]/ul/li[5]')
if type(ele20) == str:
    print("首页其他功能模块“拓赢分析”元素查找异常，" + ele20)
ele21 = fun.find_element(driver, 'xpath', '//*[@id="wrap"]/section[4]/ul/li[6]')
if type(ele21) == str:
    print("首页其他功能模块“专属指标”元素查找异常，" + ele21)

# 财富先锋首页-联系我们-电话
ele22 = fun.find_element(driver, 'xpath', '//*[@id="wrap"]/section[5]/div[1]/a/span[2]')
if type(ele22) == str:
    print("首页联系我们模块电话元素查找异常，" + ele22)
else:
    if ele22.text != "0571-56768855":
        print("首页联系我们模块电话文案错误，应为<0571-56768855>，实际为<" + ele22.text + '>')

# 财富先锋首页-联系我们-邮箱
ele23 = fun.find_element(driver, 'xpath', '//*[@id="wrap"]/section[5]/div[2]/a/span[2]')
if type(ele23) == str:
    print("首页联系我们模块邮箱元素查找异常，" + ele23)
else:
    if ele23.text != "phonevip@myhexin.com":
        print("首页联系我们模块邮箱文案错误，应为<phonevip@myhexin.com>，实际为<" + ele23.text + '>')

driver.quit()

t2 = time.time() - t1
print('脚本运行结束，运行总时长为：' + str(t2) + ' 秒')
