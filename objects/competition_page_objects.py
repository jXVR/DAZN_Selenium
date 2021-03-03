from Selenium.DAZN.locators import competition_page_locators as locators
from Selenium.DAZN.assets.lib import Lib
from selenium.webdriver.common.by import By


class CompetitionPageObject(object):

    def __init__(self, driver, *args, **kwargs):
        self.driver = driver

    def wait_for_the_page_to_be_open(self):
        Lib.wait_for_element(self, locators.COMPETITION_PAGE_TITLE, By.CSS_SELECTOR)

    def page_title(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.COMPETITION_PAGE_TITLE)

    def sports_data_menu(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.SPORTSDATA_MENU_LIST)

    def watch_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.WATCH_BUTTON)

    def standings_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.STANDINGS_BUTTON)

    def matches_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.MATCHES_BUTTON)

    def follow_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.FOLLOW_BUTTON)