import pytest
from selenium import webdriver
from FormPage import FormPage


@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )
    yield driver
    driver.quit()


def test_input_data_form(driver):
    form_page = FormPage(driver)
    form_page.input_data_form()
    field_zip = form_page.find_field_zip()
    assert field_zip == "alert py-2 alert-danger"

    field_class = form_page.find_field_class()
    index = 0
    while index < len(field_class):
        assert field_class[index] == "alert py-2 alert-success"
        index += 1
