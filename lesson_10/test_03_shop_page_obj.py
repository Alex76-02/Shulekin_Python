import pytest
import allure
from selenium import webdriver
from AutorizPageShop import AutorizPageShop
from CartPageShop import CartPageShop
from CheckoutPageShop import CheckoutPageShop
from SwagPageShop import SwagPageShop
from ResultPageShop import ResultPageShop


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@allure.epic("ТЕСТИРОВАНИЕ МАГАЗИНА")
@allure.title("Проверка покупки конкретных товаров")
@allure.description("Проверка работоспособности магазина")
@allure.feature("Проверка выполнения ТЗ")
@allure.severity("blocker")
def test_shop(driver):
    with allure.step("Авторизация в магазине"):
        form_page = AutorizPageShop(driver)
        form_page.autoriz()
    with allure.step("Добавление четырех товаров в корзину"):
        form_page = CartPageShop(driver)
        form_page.cart()
    with allure.step("Нажатие кнопки checkout"):
        form_page = CheckoutPageShop(driver)
        form_page.checkout()
    with allure.step("Заполнение формы данными покупателя"):
        form_page = SwagPageShop(driver)
        form_page.swag()
    with allure.step("Вычисление суммы покупки"):
        form_page = ResultPageShop(driver)
        sum = form_page.result()
    with allure.step("ПРОВЕРКА корректности вычисления суммы покупки"):
        assert sum == "Total: $58.29"
