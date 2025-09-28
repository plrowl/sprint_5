from selenium.webdriver.support import expected_conditions as EC
from locators import Locators as L
from selenium.webdriver.common.by import By
import data, time

class TestAdCreation:

    def test_create_ad_unauthorized(self, driver, url, wait):
        driver.get(url)
        wait.until(EC.element_to_be_clickable(L.BUTTON_CREATE_AD)).click()
        wait.until(EC.visibility_of_element_located(L.AD_ERROR_WINDOW))
        assert wait.until(EC.visibility_of_element_located(L.TEXT_AD_ERROR)).is_displayed()

    def test_create_ad_authorized(self, driver, url, wait):
        driver.get(url)

        wait.until(EC.element_to_be_clickable(L.BUTTON_LOGIN)).click()
        wait.until(EC.visibility_of_element_located(L.INPUT_EMAIL))
        driver.find_element(*L.INPUT_EMAIL).send_keys(data.VALID_EMAIL)
        driver.find_element(*L.INPUT_PASSWORD).send_keys(data.VALID_PASSWORD)
        wait.until(EC.element_to_be_clickable(L.SUBMIT_LOGIN_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(L.USER_AVATAR))

        wait.until(EC.element_to_be_clickable(L.BUTTON_CREATE_AD)).click()

        wait.until(EC.visibility_of_element_located(L.AD_NAME))
        driver.find_element(*L.AD_NAME).send_keys(f"Тест-{int(time.time()*1000)}")
        driver.find_element(*L.AD_DESCRIPTION).send_keys("Описание для автотеста")
        driver.find_element(*L.AD_PRICE_INPUT).send_keys("125")

        wait.until(EC.element_to_be_clickable(L.INPUT_DROPDOWN_CATEGORY)).click()
        wait.until(EC.element_to_be_clickable(L.TEXT_DROPDOWN_CHOOSE_CATEGORY)).click()
        wait.until(EC.element_to_be_clickable(L.BUTTON_DROPDOWN_CITY)).click()
        wait.until(EC.element_to_be_clickable(L.DROPDOWN_CHOOSE_CITY_VALUE)).click()

        wait.until(EC.element_to_be_clickable(L.INPUT_RADIOBUTTON_AD)).click()

        wait.until(EC.element_to_be_clickable(L.BUTTON_AD_PUBLISH)).click()

        wait.until(EC.element_to_be_clickable(L.USER_AVATAR)).click()
        wait.until(EC.visibility_of_element_located(L.TEXT_MYAD_SECTION))

        card = wait.until(EC.visibility_of_element_located(L.MY_AD_CARD_BY_TITLE))
        assert card.is_displayed()
