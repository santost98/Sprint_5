import pytest
from selenium import webdriver

@pytest.fixture(params=["chrome"], scope="function")
def driver(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=options)
    else:
        raise ValueError("Браузер не поддерживается")

    driver.implicitly_wait(5)
    yield driver
    driver.quit()
