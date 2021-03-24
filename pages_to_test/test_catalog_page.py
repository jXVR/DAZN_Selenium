import datetime
import pytest
import Selenium.DAZN.assets.urls as urls
from Selenium.DAZN.objects.catalog_page_objects import CatalogPageObject
from Selenium.DAZN.objects.playback_container_objects import PlaybackContainerObject
from Selenium.DAZN.pages_to_test.test_sign_in_page import log_in
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

@pytest.fixture(scope="session", autouse=True)
def browser():
    driver = Chrome()
    driver.get(urls.SIGN_IN_URL)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture(scope="session", autouse=True)
def catalog_page(browser):
    catalog_page = CatalogPageObject(browser)
    return catalog_page

@pytest.fixture(scope="session", autouse=True)
def playback_container(browser):
    playback_container = PlaybackContainerObject(browser)
    return playback_container

def test_rail_arrow(browser, catalog_page):
    log_in(browser)
    scroll_to_second_rail = ActionChains(browser).move_to_element(catalog_page.rails()[3])
    scroll_to_second_rail.perform()
    move_cursor_to_first_rail = ActionChains(browser).move_to_element(catalog_page.rails()[0])
    move_cursor_to_first_rail.perform()

    assert catalog_page.rail_next_arrow().is_displayed()

    while catalog_page.rail_next_arrow().is_displayed():
        catalog_page.rail_next_arrow().click()
        sleep(1)

    assert catalog_page.rail_previous_arrow().is_displayed()

    while catalog_page.rail_previous_arrow().is_displayed():
        catalog_page.rail_previous_arrow().click()
        sleep(1)

    assert catalog_page.rail_next_arrow().is_displayed()

def test_playback_container_pause_video(browser, catalog_page, playback_container):
    browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
    ActionChains(browser).move_to_element(catalog_page.player_container()).perform()
    playback_container.wait_for_the_page_to_be_open()

    assert playback_container.pause_button().is_displayed()

    playback_container.pause_button().click()
    sleep(1) # 1 second delay between click on pause button and reading the time value
    pause_time = playback_container.visible_current_time().get_attribute("innerText")
    sleep(5) # waiting for 5 seconds to see if the timer value has changed
    assert pause_time == playback_container.visible_current_time().get_attribute("innerText")

def test_playback_container_info_layer(playback_container):
    assert playback_container.info_layer_icon().is_displayed()

def test_playback_container_player_buttons(playback_container):
    assert playback_container.player_buttons_container().is_displayed()

def test_playback_container_fast_forward_button(playback_container):
    assert playback_container.fast_forward_button().is_displayed()

def test_playback_container_rewind_button(playback_container):
    assert playback_container.rewind_button().is_displayed()

def test_playback_container_play_button(playback_container):
    assert playback_container.play_button().is_displayed()

def test_playback_container_timeline(playback_container):
    assert playback_container.timeline().is_displayed()

def test_playback_container_current_time(playback_container):
    assert playback_container.visible_current_time().is_displayed()

def test_playback_container_volume_control(playback_container):
    assert playback_container.volume_control().is_displayed()

def test_playback_container_full_screen_button(playback_container):
    assert playback_container.full_screen_button().is_displayed()

def test_fast_forward_video_button(playback_container):
    click_count = 3
    current_time_string = playback_container.visible_current_time().get_attribute("innerText")
    if len(current_time_string.split(":")) > 2:
        paused_time = datetime.datetime.strptime(current_time_string, "%H:%M:%S")
    else:
        paused_time = datetime.datetime.strptime(current_time_string, "%M:%S")
    forwarded_expected_time = paused_time + datetime.timedelta(seconds=30 * click_count)

    for click in range(click_count):
        playback_container.fast_forward_button().click()

    forwarded_time_string = playback_container.visible_current_time().get_attribute("innerText")
    assert forwarded_expected_time == datetime.datetime.strptime(forwarded_time_string,
                                        ["%H:%M:%S" if len(current_time_string.split(":")) > 2 else "%M:%S"][0])
    sleep(2) # sleep to observe the time change

def test_rewind_video_button(playback_container):
    click_count = 3
    current_time_string = playback_container.visible_current_time().get_attribute("innerText")
    if len(current_time_string.split(":")) > 2:
        paused_time = datetime.datetime.strptime(current_time_string, "%H:%M:%S")
    else:
        paused_time = datetime.datetime.strptime(current_time_string, "%M:%S")
    forwarded_expected_time = paused_time - datetime.timedelta(seconds=30 * click_count)

    for click in range(click_count):
        playback_container.rewind_button().click()

    forwarded_time_string = playback_container.visible_current_time().get_attribute("innerText")
    assert forwarded_expected_time == datetime.datetime.strptime(forwarded_time_string,
                                        ["%H:%M:%S" if len(current_time_string.split(":")) > 2 else "%M:%S"][0])
    sleep(2) # sleep to observe the time change

def test_player_scrub_bar(browser, catalog_page, playback_container):
    ActionChains(browser).move_to_element(catalog_page.player_container()).perform()
    current_time = playback_container.visible_current_time().get_attribute("innerText")
    ActionChains(browser).drag_and_drop_by_offset(playback_container.timeline_progress(), 600, 0).perform()

    assert current_time != playback_container.visible_current_time().get_attribute("innerText")

    sleep(3)  # sleep to observe the time change
    ActionChains(browser).drag_and_drop_by_offset(playback_container.timeline_progress(), -200, 0).perform()
    sleep(3)  # sleep to observe the time change

def test_info_layer_description(browser, playback_container):
    ActionChains(browser).move_to_element(playback_container.info_layer_icon()).perform()
    sleep(1)
    playback_container.info_layer_icon().click()

    assert playback_container.info_layer_description().is_displayed()

def test_player_volume_level(browser, playback_container):
    ActionChains(browser).move_to_element(playback_container.volume_control()).perform()

    assert playback_container.volume_level().is_displayed()

    playback_container.volume_mute_button().click()
    sleep(2) # sleep to observe the time change
    playback_container.volume_unmute_button().click()

def test_enter_full_screen(playback_container):
    windowed_player_size = playback_container.player_frame().size
    playback_container.full_screen_button().click()
    sleep(2) # sleep to observe the time change

    assert playback_container.exit_full_screen_button().is_displayed()

    full_screen_window_size = playback_container.player_frame().size
    playback_container.exit_full_screen_button().click()
    sleep(2) # sleep to observe the time change

    assert playback_container.full_screen_button().is_displayed()
    assert windowed_player_size['height'] < full_screen_window_size['height'] and windowed_player_size['width'] < full_screen_window_size['width']
