from selenium.webdriver.common.by import By


class ResultPageShop:
    """
    Класс страницы итогового результата
    """
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/checkout-step-two.html")
        self._driver.maximize_window()

    def result(self) -> str:
        """
        Возврат итоговой суммы покупки
        """
        sum = self._driver.find_element(
            By.CSS_SELECTOR, "[data-test='total-label']"
            ).text
        return sum
