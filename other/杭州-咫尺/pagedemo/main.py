# _*_ coding:utf-8 _*_
__author__ = 'Heather'

import unittest
import sys
from pagedemo.common import HTMLTestRunner
from pagedemo.testcase.testSearchPage import TestSearchPage

reload(sys)
sys.setdefaultencoding("utf-8")
if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(TestSearchPage('testSearch'))

    # 定义报告输出路径
    htmlPath = u"page_demo_Report.html"
    fp = file(htmlPath, "wb")

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u"百度测试",
                                           description=u"测试用例结果")

    runner.run(testunit)

    fp.close()