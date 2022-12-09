from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert "Your basket is empty." in self.browser.find_element(*BasketPageLocators.NO_GOODS_IN_BASKET).text, \
           "Goods is presented, but should not be"

    
    def should_not_be_goods_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.GOODS_IN_BASKET), \
           "Goods is presented, but should not be"
