from locators import MainLocators, LoginLocators, UserLocators
from conftest import BaseURL
from selenium.webdriver.support import expected_conditions as conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestProfileArea:
    """Проверка перехода в ЛК с главной страницы по кнопке 'Личный кабинет' """
    def test_transition_to_pesonal_area_from_main_page_success(self, driver, login_driver):
        driver = login_driver
        WebDriverWait(driver, 10).until(conditions.visibility_of_element_located(MainLocators.personal_account_btn))
        driver.find_element(*MainLocators.personal_account_btn).click()
        WebDriverWait(driver, 10).until(conditions.visibility_of_element_located(UserLocators.exit_btn))
        save_btn_displayed = driver.find_element(*UserLocators.save_btn).is_displayed()

        assert driver.current_url == BaseURL.USER_URL and save_btn_displayed

    """Проверка перехода из ЛК в конструктор по клику на кнопку 'Конструктор' """
    def test_transition_from_personal_area_to_constructor_by_click_constructor_btn_success(self, driver, login_driver):
        driver = login_driver
        WebDriverWait(driver, 10).until(conditions.visibility_of_element_located(MainLocators.personal_account_btn))
        driver.find_element(*MainLocators.personal_account_btn).click()
        WebDriverWait(driver, 10).until(conditions.visibility_of_element_located(UserLocators.exit_btn))
        driver.find_element(*UserLocators.constructor_btn).click()
        WebDriverWait(driver, 10).until(conditions.visibility_of_element_located(MainLocators.bun))
        bun_displayed = driver.find_element(*MainLocators.bun).is_displayed()

        assert driver.current_url == BaseURL.MAIN_URL and bun_displayed

    """Проверка перехода из ЛК в конструктор по клику на лого """
    def test_transition_from_personal_area_to_constructor_by_click_logo_success(self, driver, login_driver):
        driver = login_driver
        WebDriverWait(driver, 10).until(conditions.visibility_of_element_located(MainLocators.personal_account_btn))
        driver.find_element(*MainLocators.personal_account_btn).click()
        WebDriverWait(driver, 10).until(conditions.visibility_of_element_located(UserLocators.exit_btn))
        driver.find_element(*UserLocators.logo_btn).click()
        WebDriverWait(driver, 10).until(conditions.visibility_of_element_located(MainLocators.bun))
        bun_displayed = driver.find_element(*MainLocators.bun).is_displayed()

        assert driver.current_url == BaseURL.MAIN_URL and bun_displayed

    """Проверка выхода из ЛК"""
    def test_logout_from_personal_area_success(self, driver, login_driver):
        driver = login_driver
        WebDriverWait(driver, 10).until(conditions.visibility_of_element_located(MainLocators.personal_account_btn))
        driver.find_element(*MainLocators.personal_account_btn).click()
        WebDriverWait(driver, 10).until(conditions.visibility_of_element_located(UserLocators.exit_btn))
        driver.find_element(*UserLocators.exit_btn).click()
        WebDriverWait(driver, 10).until(conditions.visibility_of_element_located(LoginLocators.login_btn))
        login_btn_displayed = driver.find_element(*LoginLocators.login_btn).is_displayed()

        assert driver.current_url == BaseURL.LOGIN_URL and login_btn_displayed