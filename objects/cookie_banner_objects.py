from Selenium.DAZN.locators import cookie_banner_locators as locators
from Selenium.DAZN.assets.urls import MAIN_URL
from Selenium.DAZN.assets.lib import Lib
from selenium.webdriver.common.by import By


class CookieBannerObject(object):

    def __init__(self, driver, *args, **kwargs):
        self.driver = driver

    def wait_for_cookie_banner(self):
        Lib.wait_for_element(self, locators.COOKIE_BANNER, By.CSS_SELECTOR)

    def cookie_banner(self):
        Lib.wait_for_element(self, locators.COOKIE_BANNER, By.CSS_SELECTOR)
        return self.driver.find_element(By.CSS_SELECTOR, locators.COOKIE_BANNER)

    def accept_all_cookies_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.COOKIE_BANNER_ACCEPT_ALL_BUTTON)