import pytest
from Tests.test_base import BaseTest
from Pages.HomePage import HomePage
from Config.config import TesData
from Pages.LoginPage import LoginPage

class Test_Home(BaseTest):

    def test_home_page_title(self):

        self.loginpage = LoginPage(self.driver)
        homePage = self.loginpage.do_login(TesData.USERNAME,TesData.PASSWORD)
        title = homePage.get_homepage_title(TesData.HOME_PAGE_TITLE)
        assert title == TesData.HOME_PAGE_TITLE

    def test_home_page_header(self):
        self.loginpage = LoginPage(self.driver)
        homePage = self.loginpage.do_login(TesData.USERNAME, TesData.PASSWORD)
        homePage_header = homePage.get_shop_name()
        assert homePage_header == TesData.HOME_PAGE_HEADER

    def test_cart_link_avaliablity(self):
        self.loginpage = LoginPage(self.driver)
        homePage = self.loginpage.do_login(TesData.USERNAME, TesData.PASSWORD)
        assert homePage.is_cart_ready_to_click()



