from selenium.webdriver.common.by import By


class FormPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
            )
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def input_data_form(self):
        self._driver.find_element(By.NAME, "first-name").send_keys("Иван")
        self._driver.find_element(By.NAME, "last-name").send_keys("Петров")
        self._driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        self._driver.find_element(By.NAME, "city").send_keys("Москва")
        self._driver.find_element(By.NAME, "country").send_keys("Россия")
        self._driver.find_element(
            By.NAME, "e-mail").send_keys("test@skypro.com")
        self._driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        self._driver.find_element(By.NAME, "job-position").send_keys("QA")
        self._driver.find_element(By.NAME, "company").send_keys("SkyPro")

        self._driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']").click()
        self._driver.implicitly_wait(5)

    def find_field_zip(self):
        input_field_zip = self._driver.find_element(
            By.ID, "zip-code").get_attribute("class")
        return input_field_zip

    def find_field_class(self):
        input_fields = ["#first-name", "#last-name", "#address",
                        "#city", "#country", "#e-mail", "#phone", "#company"
                        ]

        input_field_class_list = list()
        for input_field in input_fields:
            input_field_class = self._driver.find_element(
                By.CSS_SELECTOR, input_field).get_attribute("class")
            input_field_class_list.append(input_field_class)

        return input_field_class_list
