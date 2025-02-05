import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from yandex_authorization import wait_element, _get_info

class TestAuthorization(unittest.TestCase):
    options = Options()
    # options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--fullscreen')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    info = _get_info("yandex_auth.env")
    email = info.get('email')
    password = info.get('password')
    login = info.get('login')
    phone = info.get('phone')
    
    def setUp(self):
        self.driver.get("https://passport.yandex.ru/auth")

    def test_valid_email(self):
        wait_element(self.driver, by=By.ID, value="passp-field-login").send_keys(self.email)
        wait_element(self.driver, by=By.ID, value="passp:sign-in").click()
        time.sleep(5)

        self.assertTrue(
            self.driver.current_url == "https://passport.yandex.ru/auth/welcome"
         or self.driver.current_url == "https://passport.yandex.ru/auth/push-code")

    def test_invalid_email(self):
        wait_element(self.driver, by=By.ID, value="passp-field-login").send_keys("invalid@email.mailru")
        wait_element(self.driver, by=By.ID, value="passp:sign-in").click()
        time.sleep(5)

        self.assertEqual(  # остался на той же странице
            self.driver.current_url, 
            "https://passport.yandex.ru/auth")  
        self.assertIsNotNone(  # появилась ошибка
            wait_element(self.driver, by=By.ID, value="field:input-login:hint"))

    def test_phone_number(self):
        wait_element(self.driver, by=By.CSS_SELECTOR, value="button.Button2.Button2_size_l.Button2_view_clear").click()
        wait_element(self.driver, by=By.ID, value="passp-field-phone").send_keys(self.phone)
        wait_element(self.driver, by=By.ID, value="passp:sign-in").click()
        time.sleep(5)
        self.assertEqual(self.driver.current_url, "https://passport.yandex.ru/auth/reg")

    def test_empty_email_field(self):
        wait_element(self.driver, by=By.ID, value="passp:sign-in").click()
        time.sleep(5)

        self.assertEqual(  # остался на той же странице
            self.driver.current_url, 
            "https://passport.yandex.ru/auth")  
        self.assertIsNotNone(  # появилась ошибка
            wait_element(self.driver, by=By.ID, value="field:input-login:hint"))