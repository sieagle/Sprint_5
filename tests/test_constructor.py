from locators import MainLocators
from conftest import BaseURL

class TestConstructorPage:
    """Проверка перехода к разделу 'Булки' """
    def test_transition_to_bun_success(self, driver):
        driver.get(BaseURL.MAIN_URL)
        driver.find_element(*MainLocators.sauces_btn).click()
        driver.find_element(*MainLocators.bun_btn).click()
        bun_text = driver.find_element(*MainLocators.bun).text                 
        bun_displayed = driver.find_element(*MainLocators.bun_ul).is_displayed()

        assert bun_text == 'Булки' and bun_displayed
    """Проверка перехода к разделу 'Соусы' """
    def test_transition_to_sauces_success(self, driver):
        driver.get(BaseURL.MAIN_URL)
        driver.find_element(*MainLocators.sauces_btn).click()
        souces = driver.find_element(*MainLocators.sauces).text
        souces_displayed = driver.find_element(*MainLocators.sauces_ul).is_displayed()

        assert souces == 'Соусы' and souces_displayed
    """Проверка перехода к разделу 'Начинки' """
    def test_transition_to_topping_success(self, driver):
        driver.get(BaseURL.MAIN_URL)
        driver.find_element(*MainLocators.toppings_btn).click()
        topping = driver.find_element(*MainLocators.topping).text
        topping_displayed = driver.find_element(*MainLocators.topping_ul).is_displayed()

        assert topping == 'Начинки' and topping_displayed