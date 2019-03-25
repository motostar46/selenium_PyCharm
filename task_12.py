import time
import os
import test_example
import pytest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="session")
def driver(request):
    options = webdriver.ChromeOptions()
    options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    options.add_argument("start-maximized")

    wd = webdriver.Chrome(chrome_options=options)
    request.addfinalizer(wd.quit)
    return wd


def test_add_item_general(driver):
    test_example.test_login(driver)
    driver.implicitly_wait(3)
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog")
    driver.find_element_by_css_selector("[style*='right'] a[href*='edit_product']").click()
    driver.find_element_by_css_selector("[type=radio][value='1']").click()

    item = str(int(time.time()))
    global item_name
    item_name = "test item № " + item

    driver.find_element_by_css_selector("[name='name[en]']").send_keys(item_name)
    driver.find_element_by_css_selector("[name=code]").send_keys(item)
    driver.find_element_by_css_selector("[type=checkbox][value='1-3']").click()
    driver.find_element_by_css_selector("input[name=quantity]").send_keys(20)
    driver.find_element_by_css_selector("input[name=date_valid_from]").send_keys(
        "01012019")
    driver.find_element_by_css_selector("input[name=date_valid_to]").send_keys(
        "01012020")

    image_path = os.path.dirname(__file__) + "/Underwear.jpg"
    driver.find_element_by_css_selector("input[name='new_images[]']").send_keys(image_path)


def test_add_item_information(driver):
    driver.find_element_by_link_text("Information").click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of(driver.find_element_by_id("tab-information")))

    driver.find_element_by_css_selector("[name=manufacturer_id] [value='1']").click()
    driver.find_element_by_css_selector("[name=keywords]").send_keys("underwear")
    driver.find_element_by_css_selector("[name='short_description[en]']").send_keys("good underwear")
    driver.find_element_by_css_selector(".trumbowyg-editor").send_keys("The best underwear in the world "
                                                                       "(made in Ivanovo)")
    driver.find_element_by_css_selector("[name='head_title[en]']").send_keys("check pants")
    driver.find_element_by_css_selector("[name='meta_description[en]']").send_keys("meta")


def test_add_item_prices(driver):
    driver.find_element_by_link_text("Prices").click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of(driver.find_element_by_id("tab-prices")))

    driver.find_element_by_css_selector("[name=purchase_price]").clear()
    driver.find_element_by_css_selector("[name=purchase_price]").send_keys("10")
    driver.find_element_by_css_selector("[value='USD']").click()
    driver.find_element_by_css_selector("[name='prices[USD]']").clear()
    driver.find_element_by_css_selector("[name='prices[USD]']").send_keys("10")
    driver.find_element_by_css_selector("[name='prices[EUR]']").clear()
    driver.find_element_by_css_selector("[name='prices[EUR]']").send_keys("8")

    driver.find_element_by_css_selector("button[name=save]").click()
    assert driver.find_element_by_link_text(item_name), "The item was not created"
