from helpers import generate_random_email, generate_random_password
from data import BASE_URL, VALID_NAME, INVALID_PASSWORD
import locators as loc

def test_successful_registration(driver):
    driver.get(BASE_URL)
    driver.find_element(*loc.button_login_in_main).click()
    driver.find_element(*loc.button_register).click()

    email = generate_random_email()
    password = generate_random_password(8)

    driver.find_element(*loc.input_name).send_keys(VALID_NAME)
    driver.find_element(*loc.input_email).send_keys(email)
    driver.find_element(*loc.input_password).send_keys(password)
    driver.find_element(*loc.button_submit).click()

    # Ожидаем переход на главную страницу (например, наличие кнопки "Оформить заказ")
    assert driver.find_element(*loc.button_make_the_order).is_displayed()

def test_registration_with_invalid_password(driver):
    driver.get(BASE_URL)
    driver.find_element(*loc.button_login_in_main).click()
    driver.find_element(*loc.button_register).click()

    email = generate_random_email()

    driver.find_element(*loc.input_name).send_keys(VALID_NAME)
    driver.find_element(*loc.input_email).send_keys(email)
    driver.find_element(*loc.input_password).send_keys(INVALID_PASSWORD)
    driver.find_element(*loc.button_submit).click()

    # Проверяем наличие текста об ошибке
    error_text = driver.find_element(*loc.notification_incorrect_password).text
    assert error_text == "Некорректный пароль"

