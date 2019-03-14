import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time


@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()
    options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    options.add_argument("start-maximized")

    wd = webdriver.Chrome(chrome_options=options)
    request.addfinalizer(wd.quit)
    return wd


def is_element_present(driver, *args):
  try:
    driver.find_element(*args)
    return True
  except NoSuchElementException:
    return False


def test_example(driver):
    driver.implicitly_wait(5)
    driver.get("http://localhost/litecart/admin")

    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    quantity_main_elements = driver.find_elements_by_css_selector("#app->a")

    for i in range(1, len(quantity_main_elements) + 1):
        row = "#app-:nth-of-type(" + str(i) + ")>a"
        driver.find_element_by_css_selector(row).click()

        is_element_present(driver, By.TAG_NAME, "h1")
        quantity_nested_elements = driver.find_elements_by_css_selector(".docs .name")

        if quantity_nested_elements:
            for j in range(len(quantity_nested_elements)):
                nested_elements = driver.find_elements_by_css_selector(".docs .name")
                nested_elements[j].click()
                is_element_present(driver, By.TAG_NAME, "h1")





