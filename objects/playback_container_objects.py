from Selenium.DAZN.locators import playback_container_locators as locators
from Selenium.DAZN.assets.lib import Lib
from selenium.webdriver.common.by import By


class PlaybackContainerObject(object):

    def __init__(self, driver, *args, **kwargs):
        self.driver = driver

    def wait_for_the_page_to_be_open(self):
        Lib.wait_for_element(self, locators.VISIBLE_PAUSE_BUTTON, By.CSS_SELECTOR)

    def info_layer_icon(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.INFO_LAYER_ICON_CONTAINER)

    def info_layer_description(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.INFO_LAYER_DESCRIPTION)

    def player_buttons_container(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.PLAYER_BUTTONS_CONTAINER)

    def fast_forward_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.VISIBLE_FAST_FORWARD_BUTTON)

    def rewind_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.VISIBLE_REWIND_BUTTON)

    def play_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.VISIBLE_PLAY_BUTTON)

    def pause_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.VISIBLE_PAUSE_BUTTON)

    def timeline(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.VISIBLE_PLAYER_TIMELINE)

    def timeline_progress(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.VISIBLE_PLAYER_TIMELINE_PROGRESS)

    def visible_current_time(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.VISIBLE_PLAYER_CURRENT_TIME)

    def volume_control(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.VISIBLE_PLAYER_VOLUME_CONTROL)

    def volume_level(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.VISIBLE_PLAYER_VOLUME_LEVEL)

    def volume_mute_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.VISIBLE_PLAYER_VOLUME_MUTE_BUTTON)

    def volume_unmute_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.VISIBLE_PLAYER_VOLUME_UNMUTE_BUTTON)

    def full_screen_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.VISIBLE_PLAYER_FULL_SCREEN_BUTTON)

    def exit_full_screen_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.VISIBLE_PLAYER_FULL_SCREEN_EXIT_BUTTON)

    def player_frame(self):
        return self.driver.find_element(By.CSS_SELECTOR, locators.PLAYER_FRAME)




