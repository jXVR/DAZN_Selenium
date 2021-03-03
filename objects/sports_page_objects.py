from Selenium.DAZN.locators import sports_page_locators as locators
from Selenium.DAZN.assets.lib import Lib
from selenium.webdriver.common.by import By


class SportsPageObject(object):

    def __init__(self, driver, *args, **kwargs):
        self.driver = driver

    def wait_for_the_page_to_be_open(self):
        Lib.wait_for_element(self, locators.SPORT_PAGE_TITLE, By.CSS_SELECTOR)

    def page_title(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.SPORT_PAGE_TITLE)

    def competitions_tiles(self):
        return self.driver.find_elements(By.CSS_SELECTOR, locators.TILES_NAMES)

    def rail_names(self):
        return self.driver.find_elements(By.CSS_SELECTOR, locators.RAIL_TITLE)