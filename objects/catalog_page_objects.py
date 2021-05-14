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
        # change for next object

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

    def wait_for_reminder_button(self):
        Lib.wait_for_element(self, locators.REMINDER_BUTTON_IN_PB_CONTAINER, By.CSS_SELECTOR)

    def reminder_button_in_pb_container(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.REMINDER_BUTTON_IN_PB_CONTAINER)

    def reminder_clock_inactive(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.REMINDER_IN_RAIL_INACTIVE)

    def reminder_clock_active(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.REMINDER_IN_RAIL_ACTIVE)

    def toast_container_confirmation_banner(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.TOAST_CONTAINER_CONFIRMATION)

    def toast_container_dismiss_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.TOAST_CONTAINER_DISMISS_BUTTON)

    def wait_for_video_type_button(self):
        Lib.wait_for_element(self, locators.VIDEO_TYPE_LIST_ELEMENT , By.CSS_SELECTOR)

    def video_type_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.VIDEO_TYPE_BUTTON)

    def video_type_item(self):
        return self.driver.find_elements(By.CSS_SELECTOR, locators.VIDEO_TYPE_LIST_ELEMENT)

    def page_links(self):
        return self.driver.find_elements(By.TAG_NAME, 'a')

    def dialog_modal(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.DIALOG_MODAL)

    def ok_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.OK_BUTTON)

    def find_tile_location_with_fav(self):
        for rail_counter, rail in enumerate(self.rails()):
            tile_counter = self.find_tile_counter_with_fav(rail)
            if tile_counter >= 0:
                return rail_counter, tile_counter

    def find_tile_counter_with_fav(self, rail):
        language_code = 'en'
        country_code = 'DE'
        for counter, tile in enumerate(self.tiles_within_rail(rail)):
            eventId = self.href_from_tile(tile).get_attribute('href').split("/")[-1]
            request = requests.get(
                f'https://{urls.FAVOURITES_HOST}/v2/events/{eventId}/favourites?languageCode={language_code}&countryCode={country_code}')
            if request.status_code == 200:
                return counter

    def find_tile_location_with_multiple_vod_types(self):
        rails_url = f'https://{urls.RAILS_HOST}/eu/v7/rails?country=de&groupId=home'
        rails_request = requests.get(rails_url)

        for rail_counter, rail_name in enumerate(rails_request.json()["Rails"]):
            rail_id = rail_name["Id"]
            rail_url = f'https://{urls.RAIL_HOST}/eu/v3/Rail?id={rail_id}&country=de'
            rail_request = requests.get(rail_url)
            tiles_counter = self.find_tile_counter_with_multiple_vod_types(rail_request.json()["Tiles"])
            if tiles_counter > 0: # check if 'is not None' is working
                return rail_counter, tiles_counter

    def find_tile_counter_with_multiple_vod_types(self, tiles):
        for counter, tile in enumerate(tiles):
            if len(tile["Related"]) > 0:
                return counter

    def find_tile_counter_with_reminders(self, tiles): # add wrapper
        for counter, tile in enumerate(tiles):
            if tile["Type"] == "UpComing":
                return counter

    def find_tile_location_with_reminders(self):
        rails_url = f'https://{urls.RAILS_HOST}/eu/v7/rails?country=de&groupId=home'
        rails_request = requests.get(rails_url)

        for rail_counter, rail_name in enumerate(rails_request.json()["Rails"]):
            rail_id = rail_name["Id"]
            rail_url = f'https://{urls.RAIL_HOST}/eu/v3/Rail?id={rail_id}&country=de'
            rail_request = requests.get(rail_url)
            tiles_counter = self.find_tile_counter_with_reminders(rail_request.json()["Tiles"])
            if tiles_counter is not None:
                return rail_counter, tiles_counter