import pytest
from selenium import webdriver
from webdrivermanager.chrome import ChromeDriverManager
from webdrivermanager.gecko import GeckoDriverManager

@pytest.fixture(params=["chrome"],scope="class")
def init_driver(request):

    if request.param == "chrome":

        web_driver = webdriver.Chrome(ChromeDriverManager.chrome_driver_base_url)

    if request.param == "firefox":
        web_driver = webdriver.Firefox(GeckoDriverManager().gecko_driver_base_url)

    request.cls.driver = web_driver

    yield
    print("yielded")
    web_driver.close()