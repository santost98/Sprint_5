import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import BASE_URL, EXISTING_USER
from helpers import wait_for_element
from locators import (
    button_personal_account,
    profile,
    button_logout,
    button_login,
    input_email_auth,
    input_password_auth,
    button_login_in_main
)


class TestLogout:

    @pytest.fixture
    def login_user(self, driver):
        def _login(email, password):
            driver.get(BASE_URL)
            wait_for_element(driver, *button_login_in_main).click()
            wait_for_element(driver, *input_email_auth).send_keys(email)
            wait_for_element(driver, *input_password_auth).send_keys(password)
            wait_for_element(driver, *button_login).click()

        return _login

    def test_logout(self, driver, login_user):
        """Проверка выхода из системы"""
        # Авторизация пользователя
        login_user(EXISTING_USER["email"], EXISTING_USER["password"])

        # Переход в личный кабинет
        wait_for_element(driver, *button_personal_account).click()

        # Проверяем, что мы в профиле
        wait_for_element(driver, *profile)

        # Нажимаем кнопку выхода
        wait_for_element(driver, *button_logout).click()

        # Проверяем, что появилась кнопка входа (то есть мы разлогинились)
        assert wait_for_element(driver,
                                *button_login).is_displayed(), "Кнопка входа не отображается после выхода из системы"