
import pytest
from selenium import webdriver
from Pages.HomePage import HomePage
from Config.config import configData
import datetime
from Utilities.customLogger import LogGen
import pytest_ordering
from Pages.HomePage import HomePage
from Utilities import XLUtils


class TestLoginDDT:

    testDataFilePath = ".//TestData//LoginData.xlsx"

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

            for i in range(2, XLUtils.getRowCount(self.testDataFilePath, 'Sheet1')+1):
                self.hp.setusername(XLUtils.readData(self.testDataFilePath, 'Sheet1', i, 1))
                self.hp.setpassword(XLUtils.readData(self.testDataFilePath, 'Sheet1', i, 2))
                self.hp.clickSignInBtn()
                self.driver.implicitly_wait(10)
                if self.hp.getusername() != False:
                    if self.hp.getusername().strip() == "Hi " + XLUtils.readData(self.testDataFilePath, 'Sheet1', i, 3):
                        XLUtils.writeDate(self.testDataFilePath, 'Sheet1', i, 5, 'Yes')
                    else:
                        XLUtils.writeDate(self.testDataFilePath, 'Sheet1', i, 5, 'No')
                else:
                    XLUtils.writeDate(self.testDataFilePath, 'Sheet1', i, 5, 'No')
        else:
            assert False

        counter = 0

        for i in range(2, XLUtils.getRowCount(self.testDataFilePath, 'Sheet1') + 1):
            if XLUtils.readData(self.testDataFilePath, 'Sheet1', i, 4) == XLUtils.readData(self.testDataFilePath, 'Sheet1', i, 5):
                counter = counter + 1
        if counter == XLUtils.getRowCount(self.testDataFilePath, 'Sheet1') - 1:
            assert True
        else:
            assert False













