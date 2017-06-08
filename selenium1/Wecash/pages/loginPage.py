# -*- coding:UTF-8 -*-

__author__='lq'

import sys
from selenium.webdriver.common.by import By
from pages.basePage import BasePage

reload(sys)
sys.setdefaultencoding("utf-8")

#loginpage类
class LoginPage(BasePage):
    #元素集

    #定位器
    username = (By.ID, "phone")
    password = (By.ID,"password")
    login_btn = (By.XPATH, '//*[@id="app"]/form/button')
    forgot_password = (By.XPATH, '//*[@id="app"]/div[2]/a[1]')
    ver_login = (By.XPATH, '//*[@id="app"]/div[2]/a[2]')
    register = (By.CLASS_NAME, 'register')

    #Action输入用户名
    def set_username(self, username):
        name = self.driver.find_element(*LoginPage.username)
        name.clear()
        name.send_keys(username)
    #输入密码
    def set_password(self, password):
        pwd = self.driver.find_element(*LoginPage.password)
        pwd.clear()
        pwd.send_keys(password)
    #登录
    def click_login(self):
        loginbtn = self.driver.find_element(*LoginPage.login_btn)
        loginbtn.click()
    #忘记密码
    def forgotpassword(self):
        fogotbtn = self.driver.find_element(*LoginPage.forgot_password)
        fogotbtn.click()
    #验证码登录
    def loginbymessage(self):
        verbtn = self.driver.find_element(*LoginPage.ver_login)
        verbtn.click()
    #注册
    def sign_up(self):
        registerbtn = self.driver.find_element(*LoginPage.register)
        registerbtn.click()





