import pytest
import allure
from selenium import webdriver
from CalcPage import CalcPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )
    yield driver
    driver.quit()


@allure.epic("ТЕСТИРОВАНИЕ КАЛЬКУЛЯТОРА")
@allure.title("Проверка расчета конкретного выражения")
@allure.description("Проверка работоспособности калькулятора")
@allure.feature("Проверка выполнения ТЗ")
@allure.severity("blocker")
def test_calc(driver):
    form_page = CalcPage(driver)
    with allure.step("Установка задержки 45 секунд"):
        form_page.input_delay()
    with allure.step("Ввод данных для вычисления"):
        form_page.input_keys()
    with allure.step("Ожидание задержки 45 секунд + запас 15 секунд"):
        form_page.wait_delay()
    with allure.step("Ожидание результата"):
        form_page.wait_result()
        result = form_page.res()
    with allure.step("ПРОВЕРКА корректности вычисления суммы"):
        assert result == "15"
