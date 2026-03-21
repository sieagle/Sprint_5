from models import User, NewRandomUser
from locators import RegisterLocators, LoginLocators
from conftest import BaseURL
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected


class TestRegistrationPage:
    """Проверка повторной регистрации пользователя"""
    def test_double_registration_chexpectedk_error(self, driver):
        driver = driver
        driver.get(BaseURL.REGISTER_URL)
        WebDriverWait(driver, 5).until(expected.visibility_of_element_located(RegisterLocators.registration_btn))
        driver.find_element(*RegisterLocators.name_input).send_keys(User.user_name)
        driver.find_element(*RegisterLocators.email_input).send_keys(User.email)
        driver.find_element(*RegisterLocators.password_input).send_keys(User.password)
        driver.find_element(*RegisterLocators.registration_btn).click()
        WebDriverWait(driver, 3).until(expected.visibility_of_element_located(RegisterLocators.error_message_double_reg))   
        error = driver.find_element(*RegisterLocators.error_message_double_reg).text

        assert (error == 'Такой пользователь уже существует') and (driver.current_url == BaseURL.REG_PAGE_URL)
    """Проверка регистрации пользователя с некорректным паролем (менее 6 символов)"""
    def test_registration_incorrexpectedt_password_chexpectedk_error(self, driver):
        driver = driver
        driver.get(BaseURL.REGISTER_URL)
        WebDriverWait(driver, 5).until(expected.visibility_of_element_located(RegisterLocators.registration_btn))
        driver.find_element(*RegisterLocators.name_input).send_keys(User.user_name)
        driver.find_element(*RegisterLocators.email_input).send_keys(User.email)
        driver.find_element(*RegisterLocators.password_input).send_keys(12345)
        driver.find_element(*RegisterLocators.registration_btn).click()
        WebDriverWait(driver, 3).until(expected.visibility_of_any_elements_located(RegisterLocators.error_message_incorrect_password))
        error = driver.find_element(*RegisterLocators.error_message_incorrect_password).text

        assert (error == 'Некорректный пароль') and (driver.current_url == BaseURL.REGISTER_URL)
    """Проверка регистрации пользователя"""
    def test_registration_success(self, driver):
        driver = driver
        driver.get(BaseURL.REGISTER_URL)
        WebDriverWait(driver, 5).until(expected.visibility_of_element_located(RegisterLocators.registration_btn))
        driver.find_element(*RegisterLocators.name_input).send_keys(NewRandomUser.user_name)
        driver.find_element(*RegisterLocators.email_input).send_keys(NewRandomUser.email)
        driver.find_element(*RegisterLocators.password_input).send_keys(NewRandomUser.password)
        driver.find_element(*RegisterLocators.registration_btn).click()
        WebDriverWait(driver, 5).until(expected.visibility_of_element_located(LoginLocators.login_account_btn))
        login_btn_displayed = driver.find_element(*LoginLocators.login_account_btn).is_displayed()

        assert driver.current_url == BaseURL.LOGIN_URL and login_btn_displayed