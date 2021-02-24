import pytest
import Selenium.DAZN.assets.urls as urls
from Selenium.DAZN.objects.schedule_page_objects import SchedulePageObject
from Selenium.DAZN.objects.catalog_page_objects import CatalogPageObject
from Selenium.DAZN.pages_to_test.test_sign_in_page import log_in
from selenium.webdriver import Chrome
from time import sleep
import datetime

@pytest.fixture(scope="session", autouse=True)
def browser():
    driver = Chrome()
    driver.get(urls.SIGN_IN_URL)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_go_to_schedule_page(browser):
    log_in(browser)
    catalog_page = CatalogPageObject(browser)
    schedule_page = SchedulePageObject(browser)
    catalog_page.schedule_button().click()
    schedule_page.wait_for_the_page_to_be_open()

    assert schedule_page.date_scroller().is_displayed()

def test_today_date_is_selected(browser):
    schedule_page = SchedulePageObject(browser)
    day = datetime.datetime.now().day

    assert f'{day}\nTODAY' == schedule_page.active_today_tile().get_attribute("innerText")

def test_month_is_visible(browser):
    schedule_page = SchedulePageObject(browser)
    month = datetime.datetime.now().month

    assert len(schedule_page.month_names()) > 0

    for month_object in schedule_page.month_names():
        if month_object.get_attribute("innerText") == month:
            assert month_object.is_displayed()

def test_max_future_date_is_displayed(browser):
    schedule_page = SchedulePageObject(browser)
    max_forward_date = (datetime.datetime.now() + datetime.timedelta(14))

    while not schedule_page.date_tiles()[-1].is_displayed():
        schedule_page.date_forward_arrow().click()
        sleep(2)

    assert max_forward_date.strftime("%d\n%a").upper() == schedule_page.date_tiles()[-1].get_attribute("innerText")
    assert schedule_page.month_names()[-1].is_displayed()
    assert schedule_page.month_names()[-1].get_attribute("innerText") == max_forward_date.strftime("%B")

def test_max_future_date_can_be_selected(browser):
    schedule_page = SchedulePageObject(browser)
    max_forward_date = (datetime.datetime.now() + datetime.timedelta(14))
    schedule_page.date_tiles()[-1].click()
    sleep(2)

    assert max_forward_date.strftime("%d\n%a").upper() == schedule_page.active_tile().get_attribute("innerText")

def test_max_past_date_is_displayed(browser):
    schedule_page = SchedulePageObject(browser)
    max_past_date = (datetime.datetime.now() - datetime.timedelta(30))

    while not schedule_page.date_tiles()[0].is_displayed():
        schedule_page.date_back_arrow().click()
        sleep(1)

    assert max_past_date.strftime("%d\n%a").upper() == schedule_page.date_tiles()[0].get_attribute("innerText")
    assert schedule_page.month_names()[0].is_displayed()
    assert schedule_page.month_names()[0].get_attribute("innerText") == max_past_date.strftime("%B")

def test_max_past_date_can_be_selected(browser):
    schedule_page = SchedulePageObject(browser)
    max_past_date = (datetime.datetime.now() - datetime.timedelta(30))
    schedule_page.date_tiles()[0].click()
    sleep(2)

    assert max_past_date.strftime("%d\n%a").upper() == schedule_page.active_tile().get_attribute("innerText")

def test_back_to_today(browser):
    schedule_page = SchedulePageObject(browser)
    visible_month_list = [i.get_attribute("innerText") for i in schedule_page.month_names()]
    current_month_index_in_month_list = visible_month_list.index(datetime.datetime.now().strftime("%B"))

    while not schedule_page.today_tile().is_displayed():
        schedule_page.date_forward_arrow().click()
        sleep(1)
    schedule_page.today_tile().click()
    sleep(2)

    assert schedule_page.active_today_tile().is_displayed()
    assert schedule_page.month_names()[current_month_index_in_month_list].is_displayed()

def test_sports_dropdown_content_is_displayed(browser):
    schedule_page = SchedulePageObject(browser)
    schedule_page.sport_filter_dropdown_button().click()
    schedule_page.wait_for_sport_filter_dropdown_content()

    assert schedule_page.sport_filter_items()[0].is_displayed()

def test_select_sport_from_sport_filter(browser):
    schedule_page = SchedulePageObject(browser)
    for sport_object in schedule_page.sport_filter_items():
        if sport_object.get_attribute("innerText") == "Football":
            sport_object.click()

    assert schedule_page.reset_filter_button().is_displayed()
    assert schedule_page.sport_filter_counter().get_attribute("innerText") == "1"

def test_reset_sport_filters(browser):
    schedule_page = SchedulePageObject(browser)
    schedule_page.reset_filter_button().click()
    schedule_page.sport_filter_dropdown_button().click()

    # assert ...

def test_select_multiple_sport_and_dismiss_dropdown(browser):
    schedule_page = SchedulePageObject(browser)
    schedule_page.sport_filter_dropdown_button().click()
    schedule_page.wait_for_sport_filter_dropdown_content()

    schedule_page.sport_filter_items()[2].click()
    schedule_page.sport_filter_items()[4].click()
    schedule_page.sport_filter_dropdown_button().click()

    assert schedule_page.sport_filter_counter().get_attribute("innerText") == "2"
    # assert ...

# back arrow doesn't disappear after scrolling to the end - window resolution dependent
# how to check if "all sports" is selected (counter or filter is not displayed)