from selenium import webdriver
from locators import MainLocators, LoginLocators
from models import User
import pytest

class BaseURL:
    MAIN_URL = 'https://stellarburgers.education-services.ru/' # главная страница
    LOGIN_URL = 'https://stellarburgers.education-services.ru/login' # страница логина
    REGISTER_URL = 'https://stellarburgers.education-services.ru/register' # страница регистрации
    RECOVER_URL = 'https://stellarburgers.education-services.ru/forgot-password' # страница восстановления пароля
    USER_URL = 'https://stellarburgers.education-services.ru/account/profile' # страница личного кабинета

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def login_driver(driver):
    driver.get(BaseURL.MAIN_URL)
    driver.find_element(*MainLocators.personal_account_btn).click()
    driver.find_element(*LoginLocators.email_input).send_keys(User.email)
    driver.find_element(*LoginLocators.password_input).send_keys(User.password)
    driver.find_element(*LoginLocators.login_btn).click()
    
    return driver