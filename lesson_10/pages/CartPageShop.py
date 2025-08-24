from selenium.webdriver.common.by import By


class CartPageShop:
    """
    Класс страницы корзины магазина
    """
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/inventory.html")
        self._driver.maximize_window()

    def cart(self):
        """
        Добавление товаров в корзину
        """
        self._driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt"
            ).click()
        self._driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie"
            ).click()
        self._driver.find_element(
            By.CSS_SELECTOR, "a.shopping_cart_link.shopping_cart_link"
            ).click()
