import os
import time
from dotenv import load_dotenv
from selenium.common import TimeoutException
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def _get_info(path_to_config):
    if os.path.exists(path_to_config):
        load_dotenv(path_to_config)
    else:
        raise FileNotFoundError("Файл не был найден")

    return {
        "email": os.getenv("EMAIL"),
        "password": os.getenv("PASSWORD"),
        "login": os.getenv("LOGIN"),
        "phone": os.getenv("PHONE_NUMBER")
    }

def wait_element(browser, delay=3, by=By.TAG_NAME, value=None):
    try: 
        return WebDriverWait(browser, delay).until(
            expected_conditions.presence_of_element_located((by, value))
        )
    except TimeoutException:
        return None

def authorize_by_email(email, password):
    options = Options()
    # options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--fullscreen')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    driver.get("https://passport.yandex.ru/auth")

    wait_element(driver, by=By.ID, value='passp-field-login').send_keys(email)
    time.sleep(2)
    wait_element(driver, by=By.ID, value='passp:sign-in').click()
    time.sleep(2)
    wait_element(driver, by=By.CSS_SELECTOR, value="button.Button2.Button2_size_xxl.Button2_view_contrast-pseudo.Button2_width_max.PasswordButton").click()
    time.sleep(2)
    wait_element(driver, by=By.ID, value='passp-field-passwd').send_keys(password)
    time.sleep(2)
    wait_element(driver, by=By.ID, value='passp:sign-in').click()
    print(driver.current_url)
    time.sleep(10)
    

def authorize_by_login(login, password):
    pass

def authorize_by_phone_number(phone_number, password):
    pass

if __name__ == '__main__':
    info = _get_info("yandex_auth.env")
    email = info.get('email')
    password = info.get('password')
    login = info.get('login')
    phone = info.get('phone')

    authorize_by_email(email, password)