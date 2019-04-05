from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def remove_all_items_in_cart(self):
        self.driver.find_element_by_css_selector("li.shortcut a").click()
        _items_in_cart = self.driver.find_elements_by_name("remove_cart_item")
        for i in range(len(_items_in_cart)):
            _element_to_remove = self.driver.find_element_by_css_selector("td.item")
            self.driver.find_element_by_name("remove_cart_item").click()
            self.wait.until(ec.staleness_of(_element_to_remove))
