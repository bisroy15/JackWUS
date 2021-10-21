import time

import pytest
from selenium import webdriver
from Pages.HomePage import HomePage
from Config.config import configData
import datetime
from Utilities.customLogger import LogGen
import pytest_ordering
from Pages.HomePage import HomePage
from Pages.SearchPage import SearchPage
from Utilities import XLUtils

class TestSearch():
    testDataFilePath = ".//TestData//SearchData.xlsx"

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
        #cls.driver.close()
        #cls.driver.quit()


    def test_001_Validate_Appearance_Top_Suggestion_Modal(self):

        self.hp = HomePage(self.driver)
        if self.hp.isSearchEditFieldPresent():
            #self.hp.setSearchText(XLUtils.readData(self.testDataFilePath, 'Sheet1', 2, 1))

            self.driver.find_element(*self.hp.SEARCH_EDIT_FIELD).send_keys(XLUtils.readData(self.testDataFilePath, 'Sheet1', 2, 1))
            time.sleep(2)
            if self.hp.isTopSuggestionModalPresent():
                self.hp.clickLogo()
                assert True
            else:
                self.hp.clickLogo()
                assert False
        else:
            self.hp.clickLogo()
            assert False

    def test_002_Validate_Search_Result(self):

        self.hp = HomePage(self.driver)

        if self.hp.isSearchEditFieldPresent():
            self.hp.setSearchText(XLUtils.readData(self.testDataFilePath, 'Sheet1', 2, 2))
            self.sp = SearchPage(self.driver)
            if self.sp.isSearchResultBreadCrumbPresent() and self.sp.isSearchResultNumberMatching(XLUtils.readData(self.testDataFilePath, 'Sheet1', 2, 3)):
                assert True
            else:
                assert False
        else:
            assert False