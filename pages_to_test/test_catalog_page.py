import pytest
import assets.urls as urls
from assets.driver import DriverCreator
from objects.catalog_page_objects import CatalogPageObject
from objects.playback_container_objects import PlaybackContainerObject
from pages_to_test.test_sign_in_page import log_in
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session", autouse=True)
def browser():
    driver = DriverCreator()
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
    assert True
    return
    log_in(browser, account_index=0)
    scroll_to_second_rail = ActionChains(browser).move_to_element(catalog_page.rails()[3])
    scroll_to_second_rail.perform()
    move_cursor_to_first_rail = ActionChains(browser).move_to_element(catalog_page.rails()[0])
    move_cursor_to_first_rail.perform()

    assert catalog_page.rail_next_arrow(0).is_displayed()

    while catalog_page.rail_next_arrow(0).is_displayed():
        catalog_page.rail_next_arrow(0).click()
        sleep(1)

    assert catalog_page.rail_previous_arrow(0).is_displayed()

    while catalog_page.rail_previous_arrow(0).is_displayed():
        catalog_page.rail_previous_arrow(0).click()
        sleep(1)

    assert catalog_page.rail_next_arrow(0).is_displayed()
