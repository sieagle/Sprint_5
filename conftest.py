from selenium import webdriver
from locators import MainLocators, LoginLocators
from models import User, NewRandomUser
from urls import BaseURL
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def random_user():
    return NewRandomUser().generate()

@pytest.fixture
def login_driver(driver):
    driver.get(BaseURL.MAIN_URL)
    driver.find_element(*MainLocators.personal_account_btn).click()
    driver.find_element(*LoginLocators.email_input).send_keys(User.email)
    driver.find_element(*LoginLocators.password_input).send_keys(User.password)
    driver.find_element(*LoginLocators.login_btn).click()
    
    return driver