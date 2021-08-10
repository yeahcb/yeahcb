import time

from appium import webdriver
from time import sleep
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import assert_that, close_to
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestWX:

    def setup(self):

        des_caps = {
            'platformName': 'android',
            'platformVersion': '9.0',
            'appPackage': 'com.tencent.wework',
            'appActivity': '.launch.LaunchSplashActivity',
            'noReset': 'true',
            'deviceName': '430acc49',
            'automationName': 'UiAutomator2'
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):

        self.driver.quit()

    def test_add_contact(self):
        """
        1、打开【企业微信】应用
        2、进入 通讯录
        3、点击 添加成员
        4、点击 手动输入添加
        5、输入 姓名、手机
        6、点击 保存
        7、返回上一页
        8、拿到新联系人的属性"可见" 为 true

        :return:
        """
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="添加成员"]').click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/d4p').click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/bd9').send_keys('徐天真')
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/g9o').send_keys('17655543876')
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/alt').click()
        back_locator = (MobileBy.ID, 'com.tencent.wework:id/isd')
        WebDriverWait(self.driver, 60).until(expected_conditions.element_to_be_clickable(back_locator))
        self.driver.find_element(*back_locator).click()
        contact_element = self.driver.find_element(MobileBy.XPATH, '//*[@text="徐天真"]')
        element_display = contact_element.get_attribute("displayed")
        if element_display == 'true':
            print("创建成功")
        else:
            print("创建失败")




