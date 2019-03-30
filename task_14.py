import time
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
    wd.implicitly_wait(3)
    request.addfinalizer(wd.quit)
    return wd


def test_new_windows(driver):
    test_example.test_login(driver)
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    driver.find_element_by_css_selector("a[title=Edit]").click()

    main_window = driver.current_window_handle
    old_windows = driver.window_handles
    wait = WebDriverWait(driver, 10)

    list_links = driver.find_elements_by_css_selector(".fa-external-link")
    for every_link in list_links:
        every_link.click()
        wait.until(EC.number_of_windows_to_be(len(old_windows) + 1))
        new_window = list(set(driver.window_handles) - set(old_windows))
        driver.switch_to_window(new_window[0])
        driver.close()
        driver.switch_to_window(main_window)

