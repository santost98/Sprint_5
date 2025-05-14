# Автоматизированное тестирование Stellar Burgers

Проект для автоматизации тестирования веб-приложения Stellar Burgers с использованием Selenium WebDriver, pytest и Python.

## Описание

Данный проект включает автотесты для веб-сайта Stellar Burgers, который предоставляет конструктор бургеров и возможность регистрации пользователей. Тесты покрывают следующие функциональные аспекты:

* Регистрация нового пользователя.
* Вход в аккаунт через разные формы (главная страница, форма восстановления пароля и т.д.).
* Проверка работы личного кабинета и конструктора.
* Проверка выхода из аккаунта.

В проекте используется pytest для запуска тестов и Selenium WebDriver для автоматизации действий в браузере.

## Структура проекта

```
PythonProject3/
├── conftest.py              # Конфигурация тестов и фикстуры
├── data.py                  # Тестовые данные
├── helpers.py              # Вспомогательные функции
├── locators.py             # Локаторы элементов
├── tests/                  # Директория с тестами
│   ├── test_login.py
│   ├── test_logout.py
│   ├── test_registration.py
│   ├── test_navigation_to_personal_account.py
│   ├── test_navigation_to_constructor.py
│   └── test_constructor_section.py
└── .gitignore             # Список игнорируемых файлов
```

## Технологии

* Python 3.13.3
* Selenium WebDriver для взаимодействия с браузером
* pytest для выполнения и организации тестов
* webdriver-manager для автоматической установки и управления драйверами

## Как установить проект

1. Клонируйте репозиторий:
```bash
git clone <URL репозитория>
```

2. Создайте и активируйте виртуальное окружение:

Для Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

Для MacOS/Linux:
```bash
python -m venv venv
source venv/bin/activate
```

3. Установите зависимости:
```bash
pip install pytest
pip install selenium
```

## Запуск тестов

Для запуска всех тестов используйте команду:
```bash
pytest -v
```

Для запуска конкретного теста:
```bash
pytest tests/test_login.py -v
```

## Структура тестов

* `test_login.py` - тесты авторизации
* `test_logout.py` - тесты выхода из системы
* `test_registration.py` - тесты регистрации
* `test_navigation_to_personal_account.py` - тесты навигации в личный кабинет
* `test_navigation_to_constructor.py` - тесты навигации в конструктор
* `test_constructor_section.py` - тесты работы с секциями конструктора
