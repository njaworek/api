import os
import unittest
from appium import webdriver
import time

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestowanieAplikacji(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platfomVersion'] = '7.0'
        desired_caps['deviceName'] = 'Gigaset GS170'
        desired_caps['app'] = PATH('C:\APP\ApiDemos-debug.apk')
        desired_caps['appPackage'] = 'io.appium.android.apis'
        desired_caps['appActivity'] = 'io.appium.android.apis.ApiDemos'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def testing_wifi_options_api_demo(self):
        el = self.driver.find_element_by_xpath("//android.widget.TextView[@content-desc='Preference']")
        el.click()
        time.sleep(1)
        el2 = self.driver.find_element_by_xpath("//android.widget.TextView[@content-desc='3. Preference dependencies']")
        el2.click()
        time.sleep(1)
        #checkbox = self.driver.find_element_by_class_name("android.widget.CheckBox")
        #checkbox.click()
        #self.assertIsNotNone(checkbox)
        #time.sleep(3)

        elements = self.driver.find_elements_by_android_uiautomator("new UiSelector().checkable(true)")
        amount_of_checkboxes = len(elements)
        print "Checkboksow jest:"
        print amount_of_checkboxes
        elements[0].click()
        el3 = self.driver.find_element_by_xpath("//android.widget.TextView[@text='WiFi settings']")
        el3.click()
        els = self.driver.find_element_by_class_name('android.widget.EditText')
        els.send_keys("12345")
        ok = self.driver.find_element_by_id("button1")
        ok.click()
        self.driver.keyevent(4)
        time.sleep(1)
        self.driver.keyevent(4)
        time.sleep(1)
        self.driver.keyevent(4)
        time.sleep(1)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieAplikacji)
    unittest.TextTestRunner(verbosity=2).run(suite)