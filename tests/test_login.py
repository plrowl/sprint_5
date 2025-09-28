from selenium.webdriver.support import expected_conditions as EC
from locators import Locators as L
import data

class TestLogin:

    def test_login_user(self, driver, url, wait):
        driver.get(url)

        wait.until(EC.element_to_be_clickable(L.BUTTON_LOGIN)).click()
        wait.until(EC.visibility_of_element_located(L.INPUT_EMAIL))

        driver.find_element(*L.INPUT_EMAIL).send_keys(data.VALID_EMAIL)
        driver.find_element(*L.INPUT_PASSWORD).send_keys(data.VALID_PASSWORD)

        wait.until(EC.element_to_be_clickable(L.SUBMIT_LOGIN_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(L.BUTTON_CREATE_AD))
        wait.until(EC.visibility_of_element_located(L.USER_AVATAR))

        assert "User" in wait.until(EC.visibility_of_element_located(L.USER_NAME)).text
