from selenium.webdriver.common.by import By


class GoodPageLocators:
    BASKET_UPPER_BTN = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    BASKET_BOTTOM_BTN = (By.CSS_SELECTOR, "button.btn-primary.btn-block")
