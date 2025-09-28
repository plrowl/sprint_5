from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators as L
from data import *
import time, random


class TestRegistration:

    def test_reg_new_user(self, driver, url):
        driver.get(url)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(L.BUTTON_LOGIN)).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(L.BUTTON_NO_ACCOUNT))


        driver.find_element(*L.BUTTON_NO_ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(L.INPUT_EMAIL))

        email = f"autotest{int(time.time())}{random.randint(100,999)}@gmail.com"
        password = "Qwerty123!"

        driver.find_element(*L.INPUT_EMAIL).send_keys(email)
        driver.find_element(*L.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*L.INPUT_CONFIRM_PASSWORD).send_keys(password)


        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(L.BUTTON_CREATE_ACCOUNT)).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(L.BUTTON_CREATE_AD))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(L.USER_AVATAR))
        name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(L.USER_NAME)).text
        assert "User" in name

    def test_reg_existing_user(self, driver, url):
        driver.get(url)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(L.BUTTON_LOGIN)).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(L.BUTTON_NO_ACCOUNT))

        driver.find_element(*L.BUTTON_NO_ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(L.INPUT_EMAIL))

        driver.find_element(*L.INPUT_EMAIL).send_keys(VALID_EMAIL)
        driver.find_element(*L.INPUT_PASSWORD).send_keys(VALID_PASSWORD)
        driver.find_element(*L.INPUT_CONFIRM_PASSWORD).send_keys(VALID_PASSWORD)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(L.BUTTON_CREATE_ACCOUNT)).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(L.TEXT_EMAIL_ERROR))
        assert driver.find_element(*L.TEXT_EMAIL_ERROR).is_displayed()

    def test_reg_invalid_email_user(self, driver, url):
        driver.get(url)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(L.BUTTON_LOGIN)).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(L.BUTTON_NO_ACCOUNT))

        driver.find_element(*L.BUTTON_NO_ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(L.INPUT_EMAIL))

        driver.find_element(*L.INPUT_EMAIL).send_keys(INVALID_EMAIL)
        driver.find_element(*L.INPUT_PASSWORD).send_keys(PASSWORD_TEXT)
        driver.find_element(*L.INPUT_CONFIRM_PASSWORD).send_keys(PASSWORD_TEXT)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(L.BUTTON_CREATE_ACCOUNT)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(L.TEXT_EMAIL_ERROR))

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(L.TEXT_EMAIL_ERROR))
        assert driver.find_element(*L.TEXT_EMAIL_ERROR).is_displayed()