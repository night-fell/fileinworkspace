# -*- coding:utf-8 -*-

from selenium import webdriver
from time import sleep

if __name__ == '__main__':
    wd = webdriver.Chrome()
    wd.get("http://m.wecash.net")
    sleep(10)
    wd.close()