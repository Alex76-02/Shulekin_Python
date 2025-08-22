import pytest
import allure
from selenium import webdriver
from pages.FormPage import FormPage


@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )
    yield driver
    driver.quit()


@allure.epic("ЗАПОЛНЕНИЕ ФОРМЫ")
@allure.title("Заполнение тестовой формы")
@allure.description(
    "Проверка работоспособности формы с незаполненным полем Zip code"
    )
@allure.feature("Проверка выполнения ТЗ")
@allure.severity("blocker")
def test_input_data_form(driver):
    form_page = FormPage(driver)
    with allure.step("Заполнение формы"):
        form_page.input_data_form()
    with allure.step("Поиск поля Zip code (незаполненное поле) "):
        field_zip = form_page.find_field_zip()
    with allure.step("ПРОВЕРКА подсвечивания красным незаполненного поля"):
        assert field_zip == "alert py-2 alert-danger"
    with allure.step("Поиск и создание списка заполненных полей "):
        field_class = form_page.find_field_class()
        index = 0
    with allure.step("ПРОВЕРКА корректности отображения заполненных полей"):
        while index < len(field_class):
            assert field_class[index] == "alert py-2 alert-success"
            index += 1
