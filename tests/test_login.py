import pytest
from data import BASE_URL
import locators as loc

def test_login_from_main_page(driver, registered_user):
    driver.get(BASE_URL)
    driver.find_element(*loc.button_login_in_main).click()

    driver.find_element(*loc.input_email_auth).send_keys(registered_user["email"])
    driver.find_element(*loc.input_password_auth).send_keys(registered_user["password"])
    driver.find_element(*loc.button_login).click()

    assert driver.find_element(*loc.button_make_the_order).is_displayed()

def test_login_from_personal_account(driver, registered_user):
    driver.get(BASE_URL)
    driver.find_element(*loc.button_personal_account).click()

    driver.find_element(*loc.input_email_auth).send_keys(registered_user["email"])
    driver.find_element(*loc.input_password_auth).send_keys(registered_user["password"])
    driver.find_element(*loc.button_login).click()

    assert driver.find_element(*loc.button_make_the_order).is_displayed()

def test_login_from_registration_form(driver, registered_user):
    driver.get(BASE_URL)
    driver.find_element(*loc.button_login_in_main).click()
    driver.find_element(*loc.button_register).click()
    driver.find_element(*loc.button_login_in_registration_form).click()

    driver.find_element(*loc.input_email_auth).send_keys(registered_user["email"])
    driver.find_element(*loc.input_password_auth).send_keys(registered_user["password"])
    driver.find_element(*loc.button_login).click()

    assert driver.find_element(*loc.button_make_the_order).is_displayed()

def test_login_from_forgot_password_form(driver, registered_user):
    driver.get(BASE_URL)
    driver.find_element(*loc.button_login_in_main).click()
    driver.find_element(*loc.button_forgot_password).click()
    driver.find_element(*loc.button_login_passwd_recovery_form).click()

    driver.find_element(*loc.input_email_auth).send_keys(registered_user["email"])
    driver.find_element(*loc.input_password_auth).send_keys(registered_user["password"])
    driver.find_element(*loc.button_login).click()

    assert driver.find_element(*loc.button_make_the_order).is_displayed()


