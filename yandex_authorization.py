import os
from dotenv import load_dotenv
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
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
    