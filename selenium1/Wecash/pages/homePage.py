#_*_coding:utf-8_*_

__author__='lq'

import sys
from selenium.webdriver.common.by import By
from pages.basePage import BasePage

reload(sys)
sys.setdefaultencoding("utf-8")

#loginpage类
class HomePage(BasePage):
    #元素集

    #定位器
    username = (By.ID, "phone")
    password = (By.ID,"password")
    login_btn = (By.XPATH, '//*[@id="app"]/form/button')

    #Action输入用户名
    def set_username(self, username):
        name = self.driver.find_element(*LoginPage.username)
        name.send_keys(username)
    #输入密码
    def set_password(self, password):
        pwd = self.driver.find_element(*LoginPage.password)
        pwd.send_keys(password)
    #登录
    def click_login(self):
        loginbtn = self.driver.find_element(*LoginPage.login_btn)
        loginbtn.click()