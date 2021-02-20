from Selenium.DAZN.locators import schedule_page_locators as locators
from Selenium.DAZN.assets.lib import Lib
from selenium.webdriver.common.by import By


class SchedulePageObject(object):

    def __init__(self, driver, *args, **kwargs):
        self.driver = driver

    def wait_for_the_page_to_be_open(self):
        Lib.wait_for_element(self, locators.CALENDAR_SCROLLER, By.CSS_SELECTOR)

    def date_scroller(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.CALENDAR_SCROLLER)

    def today_tile(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.TODAY_TILE_SELECTED)

    def active_tile(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.DATETILE_SELECTED)

    def date_tiles(self):
        return self.driver.find_elements(By.CSS_SELECTOR, locators.DATETILE_TILE)

    def month_names(self):
        return self.driver.find_elements(By.CSS_SELECTOR, locators.MONTHS_NAMES)

    def sport_fiter_dropdown_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.SPORTFILTER_DROPDOWN_BUTTON)

    def date_back_arrow(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.DATE_SCROLLER_BACK_ARROW)

    def date_forward_arrow(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.DATE_SCROLLER_FORWARD_ARROW)
