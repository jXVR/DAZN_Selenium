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
    schedule_page.date_scroller().is_displayed()

def test_today_date_is_selected(browser):
    schedule_page = SchedulePageObject(browser)
    day = datetime.datetime.now().day
    assert f'{day}' == schedule_page.today_tile().get_attribute("innerText").split("\n")[0]
    assert 'TODAY' == schedule_page.today_tile().get_attribute("innerText").split("\n")[1]

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
        sleep(1)
    assert max_forward_date.strftime("%d\n%a").upper() == schedule_page.date_tiles()[-1].get_attribute("innerText")
    assert schedule_page.month_names()[-1].is_displayed()
    assert schedule_page.month_names()[-1].get_attribute("innerText") == max_forward_date.strftime("%B")

def test_max_past_date_is_displayed(browser):
    schedule_page = SchedulePageObject(browser)
    max_past_date = (datetime.datetime.now() - datetime.timedelta(30))
    while not schedule_page.date_tiles()[0].is_displayed():
        schedule_page.date_back_arrow().click()
        sleep(1)
    assert max_past_date.strftime("%d\n%a").upper() == schedule_page.date_tiles()[0].get_attribute("innerText")
    assert schedule_page.month_names()[0].is_displayed()
    assert schedule_page.month_names()[0].get_attribute("innerText") == max_past_date.strftime("%B")

# click on last date and validate if it's highlighted
# back to current date
# select 2 sports from dropdown menu and scroll to max forward again