import random
import string
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def generate_random_email():
    name = ''.join(random.choices(string.ascii_lowercase, k=8))
    domain = 'yandex.ru'
    return f'{name}_testov_999@{domain}'

def generate_random_password(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def wait_for_element(driver, by, value, timeout=5):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, value))
    )
