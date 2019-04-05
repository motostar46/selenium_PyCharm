from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class ItemPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def choose_small_item_size(self):
        try:
            self.driver.find_element_by_css_selector("[value=Small]").click()
        except NoSuchElementException:
            print("This item has no sizes")

    def add_to_cart(self):
        _quantity = self.driver.find_element_by_css_selector("#cart .quantity").text
        self.driver.find_element_by_css_selector("[name=add_cart_product]").click()
        self.wait.until(lambda d: not(d.find_element_by_css_selector("#cart .quantity").text == _quantity))

    def checkout(self):
        self.driver.find_element_by_partial_link_text("Checkout").click()









