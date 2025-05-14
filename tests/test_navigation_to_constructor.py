import pytest
from data import EXISTING_USER
from helpers import wait_for_element
from locators import (
    button_personal_account,
    header_of_page_constructor,
    button_make_the_order,
    logo,
    input_email_auth,
    input_password_auth,
    button_login,
    button_login_in_main
)


class TestNavigationToConstructor:

    @pytest.fixture
    def login_user(self, driver):
        def _login(email, password):
            driver.get("https://stellarburgers.nomoreparties.site")
            wait_for_element(driver, *button_login_in_main).click()
            wait_for_element(driver, *input_email_auth).send_keys(email)
            wait_for_element(driver, *input_password_auth).send_keys(password)
            wait_for_element(driver, *button_login).click()

        return _login

    def test_navigation_to_constructor_from_account(self, driver, login_user):
        """Проверка перехода в конструктор из личного кабинета через кнопку 'Конструктор'"""
        # Авторизация пользователя
        login_user(EXISTING_USER["email"], EXISTING_USER["password"])

        # Переход в личный кабинет
        wait_for_element(driver, *button_personal_account).click()

        # Клик по кнопке 'Конструктор'
        wait_for_element(driver, *header_of_page_constructor).click()

        # Проверка, что мы в конструкторе (видна кнопка оформления заказа)
        assert wait_for_element(driver, *button_make_the_order).is_displayed(), \
            "Кнопка 'Оформить заказ' не отображается после перехода в конструктор"

    def test_navigation_to_constructor_from_logo(self, driver, login_user):
        """Проверка перехода в конструктор из личного кабинета через логотип"""
        # Авторизация пользователя
        login_user(EXISTING_USER["email"], EXISTING_USER["password"])

        # Переход в личный кабинет
        wait_for_element(driver, *button_personal_account).click()

        # Клик по логотипу
        wait_for_element(driver, *logo).click()

        # Проверка, что мы в конструкторе (видна кнопка оформления заказа)
        assert wait_for_element(driver, *button_make_the_order).is_displayed(), \
            "Кнопка 'Оформить заказ' не отображается после перехода в конструктор через логотип"
