from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TesData
from Pages.HomePage import HomePage

class LoginPage(BasePage):
    """By locators"""
    USER_NAME = (By.ID,"username")
    PASSWORD = (By.ID,"password")
    SIGNINBTN = (By.ID,"signInBtn")

    def __init__(self,driver):

        super().__init__(driver)
        self.driver.get(TesData.BASEURL)

    """Page Actions for login page"""

    """This is used to get the page title"""
    def get_login_page_title(self,title):

        return self.get_title(title)

    """This is used to login to application"""
    def do_login(self, USERNAME, PASSWORD):

        self.do_send_keys(self.USER_NAME,USERNAME)
        self.do_send_keys(self.PASSWORD,PASSWORD)
        self.do_click(self.SIGNINBTN)
        return HomePage(self.driver)

