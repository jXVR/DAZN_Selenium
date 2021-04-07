from Selenium.DAZN.locators import catalog_page_locators as locators
from Selenium.DAZN.locators import navigation_panel_locators as navigation_locators
from Selenium.DAZN.assets.lib import Lib
import Selenium.DAZN.assets.urls as urls
from selenium.webdriver.common.by import By
import requests



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

    def rails_names(self):
        return self.driver.find_elements(By.TAG_NAME, 'h2')

    def tiles(self):
        return self.driver.find_elements(By.CSS_SELECTOR, locators.TILES)

    def tiles_within_rail(self, rail):
        return rail.find_elements(By.CSS_SELECTOR, locators.TILES)

    def href_from_tile(self, tile):
        return tile.find_element(By.TAG_NAME, 'a')

    def player_container(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.PLAYER_CONTAINER)

    def onboarding_banner(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.ONBOARDING_BANNER)

    def onboarding_banner_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.ONBOARDING_BANNER_BUTTON)

    def rail_next_arrow(self, rail_counter):
        return self.driver.find_elements(By.CSS_SELECTOR, locators.RAIL_NEXT_ARROW)[rail_counter]

    def rail_previous_arrow(self, rail_counter):
        return self.driver.find_elements(By.CSS_SELECTOR, locators.RAIL_PREVIOUS_ARROW)[rail_counter]

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

    def page_links(self):
        return self.driver.find_elements(By.TAG_NAME, 'a')

    def find_event_with_fav_in_rail(self, rail):
        language_code = 'en'
        country_code = 'DE'
        for counter, tile in enumerate(self.tiles_within_rail(rail)):
            eventId = self.href_from_tile(tile).get_attribute('href').split("/")[-1]
            # print(eventId)
            request = requests.get(
                f'https://{urls.FAVOURITES_HOST}/v2/events/{eventId}/favourites?languageCode={language_code}&countryCode={country_code}')
            # print(counter, request.status_code, eventId)
            if request.status_code == 200:
                return counter, eventId