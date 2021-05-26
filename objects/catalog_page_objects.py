from locators import catalog_page_locators as locators
from locators import navigation_panel_locators as navigation_locators
from locators import playback_container_locators as playback_locators
from assets.lib import Lib
import assets.urls as urls
from selenium.webdriver.common.by import By
import requests


class CatalogPageObject(object):

    def __init__(self, driver, *args, **kwargs):
        self.driver = driver

    def wait_for_the_page_to_be_open_with_auto_playback(self):
            Lib.wait_for_element(self, playback_locators.VISIBLE_PAUSE_BUTTON, By.CSS_SELECTOR)

    def wait_for_the_page_to_be_open_without_auto_playback(self):
            Lib.wait_for_element(self, locators.TILE_BACKGROUND_IMAGE, By.CSS_SELECTOR)

    def wait_for_slick_arrows_to_be_displayed(self):
        Lib.wait_for_element(self, locators.RAIL_NEXT_ARROW, By.CSS_SELECTOR)

    def wait_for_toast_container(self):
        Lib.wait_for_element(self, locators.TOAST_CONTAINER_CONFIRMATION, By.CSS_SELECTOR)

    def wait_for_video_type_button(self):
        Lib.wait_for_element(self, locators.VIDEO_TYPE_LIST_ELEMENT, By.CSS_SELECTOR)

    def wait_for_favourite_button(self):
        Lib.wait_for_element(self, locators.FAVOURITE_BUTTON, By.CSS_SELECTOR)

    def wait_for_favourite_list(self):
        Lib.wait_for_element(self, locators.FAVOURITE_LIST, By.CSS_SELECTOR)

    def wait_for_reminder_button(self):
        Lib.wait_for_element(self, locators.REMINDER_BUTTON, By.CSS_SELECTOR)

    def schedule_button(self):
        return self.driver.find_elements(By.CSS_SELECTOR, navigation_locators.NAVIGATION_BUTTONS)[1]

    def sports_dropdown(self):
        return self.driver.find_elements(By.CSS_SELECTOR, navigation_locators.NAVIGATION_BUTTONS)[2]

    def wait_for_the_sports_dropdown(self):
        Lib.wait_for_element(self, navigation_locators.SPORTS_MENU_DROPDOWN_CONTAINER, By.CSS_SELECTOR)

    def sports_dropdown_items(self):
        return self.driver.find_elements(By.CSS_SELECTOR, navigation_locators.SPORTS_MENU_ITEM)

    def find_rail_container_by_name(self, text):
        return self.driver.find_element(By.XPATH, f'//h2[text()="{text}"]').find_element(By.XPATH, "..")

    def find_tile_container_by_name(self, text):
        return self.driver.find_element(By.XPATH, f'//*[text()="{text}"]').find_element(By.XPATH, "../..")

    def rails(self):
        return self.driver.find_elements(By.CSS_SELECTOR, locators.RAILS)

    def rails_names(self):
        return self.driver.find_elements(By.TAG_NAME, 'h2')

    def tiles(self):
        return self.driver.find_elements(By.CSS_SELECTOR, locators.TILES)

    def tiles_within_rail(self, rail):
        return rail.find_elements(By.CSS_SELECTOR, locators.TILE_BACKGROUND_IMAGE)

    def player_container(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.PLAYER_CONTAINER)

    def onboarding_banner(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.ONBOARDING_BANNER)

    def onboarding_banner_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.ONBOARDING_BANNER_BUTTON)

    def rail_next_arrow(self, rail_counter):
        return self.driver.find_elements(By.CSS_SELECTOR, locators.RAIL_NEXT_ARROW)[rail_counter]

    def next_arrow_within_rail(self, rail):
        return rail.find_element(By.CSS_SELECTOR, locators.RAIL_NEXT_ARROW)

    def previous_arrow_within_rail(self, rail):
        return rail.find_element(By.CSS_SELECTOR, locators.RAIL_PREVIOUS_ARROW)

    def rail_previous_arrow(self, rail_counter):
        return self.driver.find_elements(By.CSS_SELECTOR, locators.RAIL_PREVIOUS_ARROW)[rail_counter]

    def favourite_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.FAVOURITE_BUTTON)

    def favourite_list(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.FAVOURITE_LIST)

    def favourite_item(self):
        return self.driver.find_elements(By.CSS_SELECTOR, locators.FAVOURITE_LIST_ELEMENT)

    def reminder_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.REMINDER_BUTTON)

    def reminder_button_within_tile(self, tile):
        return tile.find_element(By.CSS_SELECTOR, locators.REMINDER_BUTTON)

    def reminder_clock_inactive(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.REMINDER_IN_RAIL_INACTIVE)

    def reminder_clock_active(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.REMINDER_IN_RAIL_ACTIVE)

    def toast_container_confirmation_banner(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.TOAST_CONTAINER_CONFIRMATION)

    def toast_container_dismiss_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.TOAST_CONTAINER_DISMISS_BUTTON)

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

    def find_tile_location(self, func):
        rails_url = f'https://{urls.RAILS_HOST}/eu/v7/rails?country=de&groupId=home'
        rails_request = requests.get(rails_url)

        for rail_data in rails_request.json()["Rails"]:
            rail_id = rail_data["Id"]
            rail_url = f'https://{urls.RAIL_HOST}/eu/v3/Rail?id={rail_id}&country=de'
            rail_request = requests.get(rail_url)
            rail_name = rail_request.json()["Title"]
            tile_name = func(rail_request.json()["Tiles"])
            if tile_name is not None and "Don't miss" not in rail_name:
                print(f"### Rail Id = {rail_id}, Rail name = {rail_name}")
                return rail_name, tile_name

    def find_tile_name_with_multiple_vod_types(self, tiles):
        for tile in tiles:
            if len(tile["Related"]) > 0:
                tile_name = tile["Title"]
                print(f"### Tile title = {tile_name}")
                return tile_name

    def find_tile_name_with_reminders(self, tiles):
        for tile in tiles:
            if tile["Type"] == "UpComing":
                tile_name = tile["Title"]
                print(f"### Tile title = {tile_name}")
                return tile_name

    def find_tile_name_with_fav(self, tiles):
        for tile in tiles:
            eventId = tile["EventId"]
            request = requests.get(
                f'https://{urls.FAVOURITES_ENDPOINT}/{eventId}/favourites?languageCode=en&countryCode=DE')
            if request.status_code == 200:
                tile_name = tile["Title"]
                print(f"### Tile title = {tile_name}")
                return tile_name
