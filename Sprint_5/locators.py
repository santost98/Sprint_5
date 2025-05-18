from selenium.webdriver.common.by import By

# Регистрация
input_name = By.XPATH, '//label[text()="Имя"]/following-sibling::input'
input_email = By.XPATH, './/label[text()="Email"]/following-sibling::input'
input_password = By.XPATH, './/input[@name="Пароль"]'
button_submit = By.XPATH, '//button[text() = "Зарегистрироваться"]'
notification_incorrect_password = By.XPATH, '//p[text() = "Некорректный пароль"]'
button_login_in_registration_form = By.XPATH, '//a[text() = "Войти"]'

# Вход
input_email_auth = By.XPATH, '//label[text()="Email"]/following-sibling::input'
input_password_auth = By.XPATH, '//input[@name = "Пароль"]'
button_login = By.XPATH, '//button[text()="Войти"]'

# Навигация и восстановление
button_register = By.XPATH, '//a[text() = "Зарегистрироваться"]'
button_forgot_password = By.XPATH, '//a[text() = "Восстановить пароль"]'
button_login_passwd_recovery_form = By.XPATH, '//a[text() = "Войти"]'

# Личный кабинет
button_personal_account = By.XPATH, '//p[text() = "Личный Кабинет"]'
profile = By.XPATH, '//a[@href = "/account/profile"]'
order_history = By.XPATH, '//a[@href = "/account/order-history"]'
button_logout = By.XPATH, '//button[@type = "button"]'

# Главная страница
button_login_in_main = By.XPATH, './/button[text() = "Войти в аккаунт"]'
button_make_the_order = By.XPATH, '//button[text()="Оформить заказ"]'
header_of_page_constructor = By.XPATH, '//p[text() = "Конструктор"]'
logo = By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]'

# Конструктор
selected_button = By.XPATH, '//div[contains(@class, "tab_type_current")]'
buns_block = By.XPATH, '//span[text() = "Булки"]'
sauces_block = By.XPATH, '//span[text() = "Соусы"]'
fillings_block = By.XPATH, '//span[text() = "Начинки"]'