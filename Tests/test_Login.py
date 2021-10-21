
import pytest
from selenium import webdriver
from Pages.HomePage import HomePage
from Config.config import configData
import datetime
from Utilities.customLogger import LogGen
import pytest_ordering
from Pages.HomePage import HomePage
from Utilities import XLUtils


class TestLogin:
    #logger = LogGen.loggen()

    @classmethod
    def setup_class(cls):
        if configData.BROWSER == 'Chrome':
            cls.driver = webdriver.Chrome(executable_path=configData.CHROME_EXECUTABLE)
        elif configData.BROWSER == 'Firefox':
            cls.driver = webdriver.Firefox(executable_path=configData.FIREFOX_EXECUTABLE)
        else:
            cls.driver = webdriver.Chrome(executable_path=configData.CHROME_EXECUTABLE)
        cls.driver.get(configData.BASE_URL)
        cls.driver.maximize_window()
        driver = cls.driver

    @classmethod
    def teardown_class(cls):
        print('End')
        cls.driver.close()
        cls.driver.quit()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_001_Validate_homePageTitle(self):
        self.logger.info("****************** test_001_homePageTitle ******************")
        if self.driver.title == configData.HOME_PAGE_TITLE:
            assert True
        else:
            assert False



    def test_002_Validate_Login(self):


        self.hp = HomePage(self.driver)
        self.hp.clicksiginlink()

        if self.hp.isLoginModalPresent():
            self.hp.setusername(configData.USER_NAME)
            self.hp.setpassword(configData.PASSWORD)
            self.hp.clickSignInBtn()
            self.driver.implicitly_wait(10)
            if self.hp.getusername() != False:
                if self.hp.getusername().strip() == "Hi " + configData.USER:
                    assert True
                else:
                    False
            else:
                assert False
        else:
            assert False

    def test_003_Validate_Signout(self):
        self.hp = HomePage(self.driver)
        self.driver.implicitly_wait(10)
        if self.hp.clicklogoutlink():
            if self.hp.isSignInLinkPresent():
                assert True
            else:
                assert False
        else:
            assert False







