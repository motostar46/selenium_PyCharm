import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    request.addfinalizer(driver.quit)
    return driver