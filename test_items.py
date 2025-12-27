from data import Urls
from locators import GoodsPageLocators as Loc


class TestLanguageSwitch:

    def test_language_switch_shows_correct_text_basket_btn(self, browser):
        browser.get(Urls.link)
        add_to_basket_btn = browser.find_element(*Loc.BASKET_BTN)

        assert add_to_basket_btn.is_displayed(), "'Add to basket button' is not displayed"

