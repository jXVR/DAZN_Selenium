from locators import landing_page_locators as locators
from assets.urls import MAIN_URL
from assets.lib import Lib
from selenium.webdriver.common.by import By


class LandingPageObject(object):

    def __init__(self, driver, *args, **kwargs):
        self.driver = driver

    def open_page(self):
        self.driver.get(MAIN_URL)

    def wait_for_the_page_to_be_open(self):
        Lib.wait_for_element(self, locators.OPEN_BROWSE, By.CSS_SELECTOR)

    def landing_page_as_open_browse(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.OPEN_BROWSE)

    def landing_page_sign_in_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.SIGN_IN_BUTTON)
