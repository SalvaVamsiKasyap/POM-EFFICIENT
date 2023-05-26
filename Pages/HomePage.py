from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TesData


class HomePage(BasePage):

    """By locators"""

    HOME_PAGE_NAME = (By.XPATH,"//h1[text()='Shop Name']")
    CART_BUTTON = (By.CSS_SELECTOR,"a[class='nav-link btn btn-primary']")

    def __init__(self,driver):

        super().__init__(driver)

    """Page Actions for Home page"""

    """This is used to get title of home page"""

    def get_homepage_title(self,title):

        return self.get_title(title)

    def get_shop_name(self):

        return self.get_element_text(self.HOME_PAGE_NAME)

    def is_cart_ready_to_click(self):

        return self.click_element(self.CART_BUTTON)