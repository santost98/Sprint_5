import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import BASE_URL
from locators import (
    buns_block,
    sauces_block,
    fillings_block,
    selected_button,
    header_of_page_constructor
)


class TestConstructorSection:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)
        self.driver.get(BASE_URL)
        # Ждем загрузки страницы конструктора
        self.wait.until(EC.presence_of_element_located(header_of_page_constructor))

    def test_switch_to_sauces_section(self):
        """Проверка переключения на раздел 'Соусы'"""
        self.driver.find_element(*sauces_block).click()
        selected = self.driver.find_element(*selected_button)
        assert "Соусы" in selected.text, "Раздел 'Соусы' не выбран"

    def test_switch_to_fillings_section(self):
        """Проверка переключения на раздел 'Начинки'"""
        self.driver.find_element(*fillings_block).click()
        selected = self.driver.find_element(*selected_button)
        assert "Начинки" in selected.text, "Раздел 'Начинки' не выбран"

    def test_switch_to_buns_section(self):
        """Проверка переключения на раздел 'Булки'"""
        # Сначала переключимся на другой раздел
        self.driver.find_element(*fillings_block).click()
        # Затем вернемся к булкам
        self.driver.find_element(*buns_block).click()
        selected = self.driver.find_element(*selected_button)
        assert "Булки" in selected.text, "Раздел 'Булки' не выбран"

    def test_default_selected_section(self):
        """Проверка, что по умолчанию выбран раздел 'Булки'"""
        selected = self.driver.find_element(*selected_button)
        assert "Булки" in selected.text, "По умолчанию должен быть выбран раздел 'Булки'"

