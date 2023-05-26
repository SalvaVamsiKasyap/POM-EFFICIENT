import pytest
from Tests.test_base import BaseTest
from Pages.LoginPage import LoginPage
from Config.config import TesData
import Config
import pandas as pd

class Test_Login(BaseTest):

    def test_login_page_title(self):

        self.loginpage = LoginPage(self.driver)
        title = self.loginpage.get_login_page_title(TesData.LOGIN_PAGE_TITLE)
        assert title == TesData.LOGIN_PAGE_TITLE

    def get_data():
        dataframe1 = pd.read_excel(r'C:\Users\Lenovo\PycharmProjects\POM\Config\testdata.xlsx')
        #print(dataframe1)
        return dataframe1.values.tolist()

        # each row is returned as a pandas series

        #return [["rahulshettyacademy","learning"],["salva","kasyap"]]

        # workbook = openpyxl.load_workbook(r'C:\Users\Lenovo\PycharmProjects\POM\Config\testdata.xlsx')
        # sheet = workbook["SearchTest"]
        # totalrows = sheet.max_row
        # totalcolumns = sheet.max_column
        # mainList = []
        #
        # for i in range(2,totalrows+1):
        #     dataList = []
        #     for j in range(2,totalcolumns):
        #         data = sheet.cell(row=i,column=j).value
        #         dataList.insert(j,data)
        #     mainList.insert(i,dataList)
        # return mainList


    @pytest.mark.parametrize("username,password", get_data())
    def test_login(self,username,password):

        self.loginpage = LoginPage(self.driver)
        #self.loginpage.do_login(TesData.USERNAME,TesData.PASSWORD)
        self.loginpage.do_login(username, password)


