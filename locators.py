from selenium.webdriver.common.by import By

# ------------------ Регистрация ------------------
input_name = By.XPATH, '//label[text()="Имя"]/following-sibling::input'  # Поле "Имя"
input_email = By.XPATH, './/label[text()="Email"]/following-sibling::input'  # Поле "Email"
input_password = By.XPATH, './/input[@name="Пароль"]'  # Поле "Пароль"
button_submit = By.XPATH, '//button[text() = "Зарегистрироваться"]'  # Кнопка "Зарегистрироваться"
notification_incorrect_password = By.XPATH, '//p[text() = "Некорректный пароль"]'  # Сообщение об ошибке
button_login_in_registration_form = By.XPATH, '//a[text() = "Войти"]'  # Кнопка "Войти" внизу формы регистрации

# ------------------ Авторизация ------------------
input_email_auth = By.XPATH, '//label[text()="Email"]/following-sibling::input'  # Email в форме входа
input_password_auth = By.XPATH, '//input[@name = "Пароль"]'  # Пароль в форме входа
button_login = By.XPATH, '//button[text()="Войти"]'  # Кнопка "Войти"

# ------------------ Навигация ------------------
button_register = By.XPATH, '//a[text() = "Зарегистрироваться"]'  # Кнопка "Зарегистрироваться" на форме входа
button_forgot_password = By.XPATH, '//a[text() = "Восстановить пароль"]'  # Ссылка на восстановление пароля
button_login_passwd_recovery_form = By.XPATH, '//a[text() = "Войти"]'  # Кнопка "Войти" в форме восстановления

# ------------------ Личный кабинет ------------------
button_personal_account = By.XPATH, '//p[text() = "Личный Кабинет"]'  # Кнопка "Личный Кабинет"
profile = By.XPATH, '//a[@href = "/account/profile"]'  # Профиль
order_history = By.XPATH, '//a[@href = "/account/order-history"]'  # История заказов
button_logout = By.XPATH, '//button[@type = "button"]'  # Кнопка "Выйти"

# ------------------ Главная ------------------
button_login_in_main = By.XPATH, './/button[text() = "Войти в аккаунт"]'  # Кнопка "Войти в аккаунт"
button_make_the_order = By.XPATH, '//button[text()="Оформить заказ"]'  # Кнопка "Оформить заказ"
header_of_page_constructor = By.XPATH, '//p[text() = "Конструктор"]'  # Заголовок "Конструктор"
logo = By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]'  # Логотип

# ------------------ Конструктор ------------------
selected_button = By.XPATH, '//div[contains(@class, "tab_type_current")]'  # Активный таб
buns_block = By.XPATH, '//span[text() = "Булки"]'  # Таб "Булки"
sauces_block = By.XPATH, '//span[text() = "Соусы"]'  # Таб "Соусы"
fillings_block = By.XPATH, '//span[text() = "Начинки"]'  # Таб "Начинки"
