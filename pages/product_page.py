from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
        self.solve_quiz_and_get_code()
        self.should_be_book_in_basket()
        

    def should_be_book_in_basket(self):
        assert (self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_BASKET)).text == (self.browser.find_element(*ProductPageLocators.BOOK_NAME)).text, "The name of the book in the basket does not match"
        assert (self.browser.find_element(*ProductPageLocators.BOOK_PRICE)).text == (self.browser.find_element(*ProductPageLocators.BASKET_PRICE)).text, "The price of the book in the basket does not match"

        
