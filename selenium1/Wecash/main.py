#_*_ coding:utf-8 _*_

__author__='lq'

import unittest
import sys
from common import HTMLTestRunner
from testcase.testLogin import Test_Login


reload(sys)
sys.setdefaultencoding("utf-8")

if __name__ =='__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(Test_Login('user_login1'))
    testunit.addTest(Test_Login('user_login2'))
    #testunit.addTest(Test_Login('user_login3'))
    #testunit.addTest(Test_Login('user_login4'))
    #testunit.addTest(Test_Login('user_login5'))

    # 定义报告输出路径
    htmlPath = u"wecashReport.html"
    fp = file(htmlPath, "wb")

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"wecash测试", description=u"测试用例 结果")
    runner.run(testunit)

    fp.close()


