from models import User
from locators import MainLocators, LoginLocators, RegisterLocators, RecoverLocators
from conftest import BaseURL
from selenium.webdriver.support import expected_conditions as conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestLogin:
    """Вход в личный кабинет через кнопку 'Войти в аккаунт' на главной странице"""
    def test_login_in_login_btn_success(self, driver):
        driver.get(BaseURL.MAIN_URL)

        driver.find_element(*MainLocators.account_btn).click()
        driver.find_element(*LoginLocators.email_input).send_keys(User.email)
        driver.find_element(*LoginLocators.password_input).send_keys(User.password)
        driver.find_element(*LoginLocators.login_btn).click()

        WebDriverWait(driver, 10).until(conditions.visibility_of_element_located(MainLocators.place_order_button))
        order_btn = driver.find_element(*MainLocators.place_order_button).text

        assert (driver.current_url == BaseURL.MAIN_URL) and (order_btn == 'Оформить заказ')

    """Вход в личный кабинет через кнопку 'Личный кабинет' на главной странице"""
    def test_login_in_account_btn_success(self, driver):
        driver.get(BaseURL.MAIN_URL)

        driver.find_element(*MainLocators.account_btn).click()
        driver.find_element(*LoginLocators.email_input).send_keys(User.email)
        driver.find_element(*LoginLocators.password_input).send_keys(User.password)
        driver.find_element(*LoginLocators.login_btn).click()

        WebDriverWait(driver, 10).until(conditions.visibility_of_element_located(MainLocators.place_order_button))
        order_btn = driver.find_element(*MainLocators.place_order_button).text

        assert (driver.current_url == BaseURL.MAIN_URL) and (order_btn == 'Оформить заказ')

    """Вход в личный кабинет через форму регистрации"""
    def test_login_in_registration_form_success(self, driver):
        driver.get(BaseURL.REGISTER_URL)

        driver.find_element(*RegisterLocators.login_btn).click()
        driver.find_element(*LoginLocators.email_input).send_keys(User.email)
        driver.find_element(*LoginLocators.password_input).send_keys(User.password)
        driver.find_element(*LoginLocators.login_btn).click()

        WebDriverWait(driver, 10).until(conditions.visibility_of_element_located(MainLocators.place_order_button))
        order_btn = driver.find_element(*MainLocators.place_order_button).text

        assert (driver.current_url == BaseURL.MAIN_URL) and (order_btn == 'Оформить заказ')

    """Вход в личный кабинет через форму восстановления"""
    def test_login_in_recover_form_success(self, driver):
        driver.get(BaseURL.RECOVER_URL)
        
        driver.find_element(*RecoverLocators.login_btn).click()
        driver.find_element(*LoginLocators.email_input).send_keys(User.email)
        driver.find_element(*LoginLocators.password_input).send_keys(User.password)
        driver.find_element(*LoginLocators.login_btn).click()
        
        WebDriverWait(driver, 10).until(conditions.visibility_of_element_located(MainLocators.place_order_button))
        order_btn = driver.find_element(*MainLocators.place_order_button).text
        
        assert (driver.current_url == BaseURL.MAIN_URL) and (order_btn == 'Оформить заказ')