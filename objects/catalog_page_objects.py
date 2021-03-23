from Selenium.DAZN.locators import catalog_page_locators as locators
from Selenium.DAZN.locators import navigation_panel_locators as navigation_locators
from Selenium.DAZN.assets.lib import Lib
from selenium.webdriver.common.by import By


class CatalogPageObject(object):

    def __init__(self, driver, *args, **kwargs):
        self.driver = driver

    def wait_for_the_page_to_be_open(self):
        Lib.wait_for_element(self, locators.PLAYER_CONTAINER, By.CSS_SELECTOR)

    def schedule_button(self):
        return self.driver.find_elements(By.CSS_SELECTOR, navigation_locators.NAVIGATION_BUTTONS)[1]

    def sports_dropdown(self):
        return self.driver.find_elements(By.CSS_SELECTOR, navigation_locators.NAVIGATION_BUTTONS)[2]

    def wait_for_the_sports_dropdown(self):
        Lib.wait_for_element(self, navigation_locators.SPORTS_MENU_DROPDOWN_CONTAINER, By.CSS_SELECTOR)

    def sports_dropdown_items(self):
        return self.driver.find_elements(By.CSS_SELECTOR, navigation_locators.SPORTS_MENU_ITEM)

    def rails(self):
        return self.driver.find_elements(By.CSS_SELECTOR, locators.RAILS)

    def player_container(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.PLAYER_CONTAINER)

    def onboarding_banner(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.ONBOARDING_BANNER)

    def onboarding_banner_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.ONBOARDING_BANNER_BUTTON)

    def rail_next_arrow(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.RAIL_NEXT_ARROW)

    def rail_previous_arrow(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.RAIL_PREVIOUS_ARROW)

    def wait_for_favourite_button(self):
        Lib.wait_for_element(self, locators.FAVOURITE_BUTTON, By.CSS_SELECTOR)

    def favourite_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.FAVOURITE_BUTTON)

    def favourite_list(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.FAVOURITE_LIST)

    def favourite_item(self):
        return self.driver.find_elements(By.CSS_SELECTOR, locators.FAVOURITE_LIST_ELEMENT)

    def favourite_confirmation_banner(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.FAVOURITE_CONFIRMATION)

    def favourite_confirmation_banner_dismiss_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.FAVOURITE_DISMISS_BUTTON)
