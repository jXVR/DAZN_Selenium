import pytest
import assets.urls as urls
from objects.catalog_page_objects import CatalogPageObject
from objects.playback_container_objects import PlaybackContainerObject
from pages_to_test.test_sign_in_page import log_in
from selenium.webdriver.common.action_chains import ActionChains
from seleniumwire.webdriver import Chrome
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


def test_change_video_type(browser, catalog_page, playback_container):
    log_in(browser, account_index=1)

    rail_name, tile_name = catalog_page.find_tile_location(catalog_page.find_tile_name_with_multiple_vod_types)
    rail = catalog_page.find_rail_container_by_name(rail_name)
    tile = catalog_page.find_tile_container_by_name(tile_name)

    ActionChains(browser).move_to_element(rail).perform()

    while not tile.is_displayed():
        catalog_page.next_arrow_within_rail(rail).click()
        sleep(1)  # just for visibility
    tile.click()

    playback_container.wait_for_the_page_to_be_open()
    catalog_page.wait_for_video_type_button()
    playback_container.pause_button().click()
    sleep(1)  # just for visibility
    catalog_page.video_type_button().click()
    sleep(1)  # just for visibility

    assert catalog_page.video_type_item()[0].is_displayed()
    assert catalog_page.video_type_item()[-1].is_displayed()

    catalog_page.video_type_item()[-1].click()
    sleep(1)  # just for visibility
    catalog_page.video_type_button().click()
    sleep(1)  # just for visibility
    catalog_page.video_type_button().click()
    playback_container.wait_for_the_page_to_be_open()
    playback_container.pause_button().click()
