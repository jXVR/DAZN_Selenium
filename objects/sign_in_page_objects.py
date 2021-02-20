from Selenium.DAZN.locators import sign_in_page_locators as locators
from Selenium.DAZN.assets.urls import SIGN_IN_URL
from Selenium.DAZN.assets.lib import Lib
from selenium.webdriver.common.by import By


class SignInPageObject(object):

    def __init__(self, driver, *args, **kwargs):
        self.driver = driver

    def open_page(self):
        self.driver.get(SIGN_IN_URL)

    def wait_for_the_page_to_be_open(self):
        Lib.wait_for_element(self, locators.SIGN_IN_PAGE_TITLE, By.CSS_SELECTOR)

    def sign_in_page_title(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.SIGN_IN_PAGE_TITLE)

    def start_watching_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.START_WATCHING_BUTTON)

    def email_field(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.EMAIL_FIELD)

    def password_field(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.PASSWORD_FIELD)