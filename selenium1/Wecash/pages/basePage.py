# -*- coding:UTF-8 -*-

__author__='lq'

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

#page基类
class BasePage(object):
    """
    Page基类，所有page都应该继承该类
    """
    def __init__(self, driver):
        self.driver = driver

