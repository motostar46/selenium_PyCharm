import pytest
import time


from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()
    options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    options.add_argument("start-maximized")

    wd = webdriver.Chrome(chrome_options=options)
    wd.implicitly_wait(2)

 #   wd = webdriver.Ie()

 #   wd = webdriver.Firefox()
    request.addfinalizer(wd.quit)
    return wd


def test_creating_account(driver):
    for i in range(3):
        driver.get("http://localhost/litecart/en/")
        driver.find_element_by_class_name("product").click()

        try:
            driver.find_element_by_css_selector("[value=Small]").click()
        except NoSuchElementException:
            print("This item has no sizes")

        quantity = driver.find_element_by_css_selector("#cart .quantity").text
        driver.find_element_by_css_selector("[name=add_cart_product]").click()

        wait = WebDriverWait(driver, 10)
        wait.until(lambda d: not(d.find_element_by_css_selector("#cart .quantity").text == quantity))

    driver.find_element_by_partial_link_text("Checkout").click()
    driver.find_element_by_css_selector("li.shortcut a").click()
    items_in_cart = driver.find_elements_by_name("remove_cart_item")
    for item in range(len(items_in_cart)):
        element_to_remove = driver.find_element_by_css_selector("td.item")
        driver.find_element_by_name("remove_cart_item").click()
        wait.until(EC.staleness_of(element_to_remove))
