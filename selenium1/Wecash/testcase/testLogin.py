# -*- coding:UTF-8 -*-
__author__='lq'
import unittest
import sys
from selenium import webdriver
from pages.loginPage import LoginPage
import time
reload(sys)
sys.setdefaultencoding("utf-8")

# 登录测试用例
class Test_Login(unittest.TestCase):
    """测试用户登录"""
    def setUp(self):
        # 设置浏览器为手机模式
        mobileEmulation = {'deviceName': 'Apple iPhone 5'}
        options = webdriver.ChromeOptions()
        options.add_experimental_option('mobileEmulation', mobileEmulation)
        # 生成web对象
        self.driver = webdriver.Chrome(chrome_options=options)
        # 打开指定URL
        self.driver.get("http://m.wecash.net/wep/user/login.html")
    def tearDown(self):
        self.driver.close()

    def user_login(self, username="", password=""):
        login_page = LoginPage(self.driver)
        login_page.set_username(username)
        login_page.set_password(password)
        # 单击登录按钮
        login_page.click_login()
        time.sleep(5)

    def user_login1(self):
        """用户名为空"""
        self.user_login(password="opklnm")
        #time.sleep(2)
        self.assertEqual(self.driver.current_url, u"http://m.wecash.net/wep/login/login.html")
        #result = LoginPage.username_null()
        #self.assertTrue(result)
    def user_login2(self):
        """密码为空"""
        self.user_login(username='13514284833')
        time.sleep(2)
        self.assertEqual(self.driver.current_url, u"http://m.wecash.net/wep/login/login.html")

    def user_login3(self):
        """密码错误"""
        self.user_login(username='15110185703', password="111111")
        time.sleep(2)
        self.assertEqual(self.driver.current_url, u"http://m.wecash.net/wep/login/login.html")

    def user_login4(self):
        """账号未注册"""
        self.user_login(username='13514284833', password="opklnm")
        time.sleep(2)
        self.assertEqual(self.driver.current_url, u"http://m.wecash.net/wep/login/login.html")

    def user_login5(self):
        """用户名、密码正确"""
        self.user_login(username='15110185703', password="opklnm")
        time.sleep(2)
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="app"]/footer/div[1]/div').text, u"闪银奇异")

"""
    def test_Login(self):

        login_page.set_username("15110185703")
        #点击忘记密码
        login_page.forgotpassword()
        time.sleep(5)
        #返回登录页
        self.driver.back()
        #快速注册
        login_page.sign_up()
        time.sleep(5)
        # 返回登录页
        self.driver.back()
        #验证码登录
        login_page.loginbymessage()
        time.sleep(5)
        # 密码登录
        login_page.loginbymessage()
        time.sleep(5)
        #输入密码
        login_page.set_password("opklnm")

"""




