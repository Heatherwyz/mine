# -*- coding:utf-8 -*-
import sys
from imp import reload

__author__ = "Heather"
from selenium.webdriver.common.by import By
from pages.basePage import Page
reload(sys)
sys.setdefaultencoding("utf-8")
class SearchPage(Page):
    search_input = (By.ID,u"kw")
    search_button = (By.ID,u"su")

    def __init__(self,driver,base_url=u"https://www.baidu.com"):
        Page.__init__(self,driver,base_url)

    def gotoBaiduHomePage(self):
        print(u"打开首页",self.base_url)
        self.driver.get(self.base_url)

    def input_serch_text(self,text=u"selenium"):
        print(u"输入搜索关键字： selenium ")

    def click_search_btn(self):
        print(u"点击 百度一下 按钮")
        self.click(self.search_button)