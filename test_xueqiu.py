
#coding=utf-8

import pytest
import unittest

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestXueqiu(unittest.TestCase):

    stock_name=""

    def setUp(self):
        print("setup")
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "demo"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"
        # 中文键盘
        caps["unicodeKeyboard"]="true"
        caps["resetKeyboard"] = "true"
        #tips
        caps["ignoreUnimportantViews"] = "true"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)


    def test_alibaba_search(self):
        self.driver.find_element_by_xpath(
            "//*[@text='自选' and contains(@resource-id, 'tab_name')]")
        self.driver.find_element_by_xpath(
            "//*[@text='自选' and contains(@resource-id, 'tab_name')]")
        self.driver.find_element_by_xpath(
            "//*[@text='自选' and contains(@resource-id, 'tab_name')]").click()
        self.driver.find_element_by_id("action_create_cube").click()
        self.driver.find_element_by_id("search_input_text").send_keys("alibaba")

        # self.driver.find_element_by_id("search_input_text").send_keys("阿里巴巴")

        # if len(self.driver.find_elements_by_id("follow_btn")) > 0:
        #     self.driver.find_element_by_id("follow_btn").click()
        #     assert self.driver.find_elements_by_id("follow_btn").__getattribute__("resource-id") == "followed_btn"
        #     self.driver.find_element_by_xpath("//*[@text='下次再说']").click()


        # assert 1 == len(self.driver.find_elements_by_xpath(
        #     "//*[contains(@resource-id, 'portfolio_stockName') and @text='拼多多']"))

    def test_add_us(self):
        self.driver.find_element_by_xpath(
            "//*[@text='自选' and contains(@resource-id, 'tab_name')]")
        self.driver.find_element_by_xpath(
            "//*[@text='自选' and contains(@resource-id, 'tab_name')]")
        self.driver.find_element_by_xpath(
            "//*[@text='自选' and contains(@resource-id, 'tab_name')]").click()
        self.driver.find_element_by_xpath("//*[@text='美股']").click()
        self.driver.find_element_by_id("recommend_name_one").click()
        self.driver.implicitly_wait(10)
        stock_name=self.driver.find_element_by_id("action_bar_stock_name").text
        print(stock_name)
        self.driver.find_element_by_xpath("//*[@text='加自选']")
        self.driver.find_element_by_xpath("//*[@text='加自选']")
        self.driver.find_element_by_xpath("//*[@text='加自选']").click()
        self.driver.find_element_by_xpath("//*[@text='下次再说']").click()

        assert 1 == len(self.driver.find_elements_by_xpath("//*[@text='设自选']"))

        self.driver.back()

        self.driver.find_element_by_xpath("//*[@text='美股']").click()
        assert 1 == len(self.driver.find_elements_by_xpath("//*[@text='"+stock_name+"']"))
        self.driver.find_element_by_xpath("//*[@text='全部']").click()
        assert 1 == len(self.driver.find_elements_by_xpath("//*[@text='"+stock_name+"']"))


    def test_delete_us(self):
        # global stock_name
        self.driver.find_element_by_xpath(
            "//*[@text='自选' and contains(@resource-id, 'tab_name')]")
        self.driver.find_element_by_xpath(
            "//*[@text='自选' and contains(@resource-id, 'tab_name')]")
        self.driver.find_element_by_xpath(
            "//*[@text='自选' and contains(@resource-id, 'tab_name')]").click()
        self.driver.find_element_by_xpath("//*[@text='美股']").click()

        elements = self.driver.find_elements_by_id("portfolio_stockName")
        stock_name=elements[0].text
        print("*************"+stock_name)

        TouchAction(self.driver).long_press(elements[0]).perform()
        self.driver.find_element_by_xpath("//*[@text='删除']").click()

        assert 0 == len(self.driver.find_elements_by_xpath("//*[@text='"+stock_name+"']"))
        self.driver.find_element_by_xpath("//*[@text='全部']").click()
        assert 0 == len(self.driver.find_elements_by_xpath("//*[@text='" + stock_name + "']"))


    @pytest.mark.parametrize("stock_name",["百度","特斯拉","京东","阿里巴巴","哔哩哔哩","拼多多",
                                          "迅雷","大众仓储","苏格兰皇家银行","美国银行","爱奇艺","优信"
                                          "蔚来","58同城","Facebook","摩根大通","腾讯音乐","卡夫亨氏",
                                          "陌陌","AMD","格林电视","众美联","协同制药","Endava"])
    def test_add_batch(self,stock_name):
        self.test_add_stock(stock_name)


    def test_add_stock(self,stock_name):
        self.driver.find_element_by_id("tv_search").click()
        self.driver.find_element_by_id("search_input_text").send_keys("百度")
        if len(self.driver.find_elements_by_xpath("//*[@text='下次再说']")):
            self.driver.find_elements_by_xpath("//*[@text='下次再说']").clear()
        self.driver.find_element_by_id("follow_btn").click()


