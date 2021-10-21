import pytest
from selenium import webdriver
from Pages.HomePage import HomePage
from Config.config import configData
import datetime
from Utilities.customLogger import LogGen
import pytest_ordering
from Pages.HomePage import HomePage
from Pages.PLPPage import PLPPage
from Pages.MiscPage import MiscPage
from Pages.PDPPage import PDPPage
from Utilities import XLUtils
from selenium.webdriver.common.keys import Keys

class TestHomePage():

    testDataFilePath = ".//TestData//HomePageData.xlsx"

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

    def test_001_Validate_homePageTitle(self):
        if self.driver.title == configData.HOME_PAGE_TITLE:
            assert True
        else:
            assert False

    def test_002_Validate_Main_Menu(self):
        self.hp = HomePage(self.driver)
        self.plp = PLPPage(self.driver)
        if self.hp.clickMainMenuItem(XLUtils.readData(self.testDataFilePath, 'HomePage', 2, 1)):
            if self.plp.isComponentBreadCrumbpRESENT(XLUtils.readData(self.testDataFilePath, 'HomePage', 2, 1)):
                self.hp.clickLogo()
                assert True
            else:
                self.hp.clickLogo()
                assert False
        else:
            self.hp.clickLogo()
            assert False

    def test_003_Validate_ExclusionsApply(self):

        self.driver.find_element_by_tag_name('body').send_keys(Keys.END)
        self.hp = HomePage(self.driver)
        self.mp = MiscPage(self.driver)
        if self.hp.isHomePagePopUpPresent():
            self.driver.implicitly_wait(20)
            self.hp.closeHomePagePopUp()
        past_num_of_tabs = len(self.driver.window_handles)
        if self.hp.isExclusionsApplyLinkPresent():
            self.hp.clickExclusionsApplyLink()
            if (len(self.driver.window_handles) - past_num_of_tabs) > 0:
                self.driver.switch_to_window(self.driver.window_handles[len(self.driver.window_handles)-1])
                if self.mp.isDealsAndOffersPagePresent():
                    self.driver.close()
                    self.driver.switch_to_window(self.driver.window_handles[len(self.driver.window_handles)-1])
                    self.hp.clickScrolledDownLogo()
                    assert True
                else:
                    self.hp.clickScrolledDownLogo()
                    assert False
            else:
                self.hp.clickScrolledDownLogo()
                assert False
        else:
            self.hp.clickScrolledDownLogo()
            assert False

    def test_004_Validate_Our_Favorite(self):
        self.hp = HomePage(self.driver)
        self.pdp = PDPPage(self.driver)

        if self.hp.isOurFavoriteItemPresent():
            productName = self.driver.find_element(*self.hp.OUR_FAVOURITE_FIRST_ITEM).get_attribute('title')
            if self.hp.clickOurFavoriteItem():
                if self.pdp.isPDPItemNamePresent():
                   if productName.strip().upper() == self.driver.find_element(*self.pdp.PDP_ITEM_NAME).text.strip().upper():
                       self.hp.clickLogo()
                       assert True
                   else:
                       self.hp.clickLogo()
                       assert False
                else:
                    self.hp.clickLogo()
                    assert False
            else:
                self.hp.clickLogo()
                assert False
        else:
            self.hp.clickLogo()
            assert False

    def test_005_Validate_Shop_By_Category(self):

        self.hp = HomePage(self.driver)
        self.plp = PLPPage(self.driver)
        if self.hp.selectShopByCatItem(XLUtils.readData(self.testDataFilePath, 'HomePage', 2, 3)):
            if self.plp.isComponentBreadCrumbpRESENT(XLUtils.readData(self.testDataFilePath, 'HomePage', 2, 4).strip().upper()):
                self.hp.clickLogo()
                assert True

            else:
                self.hp.clickLogo()
                assert False
        else:
            self.hp.clickLogo()
            assert False

    def test_006_Validate_Registered_Mail_ID_Registration(self):

        self.hp = HomePage(self.driver)
        self.hp.clicksiginlink()

        if self.hp.isLoginModalPresent():
            if self.hp.clickSignUpLink():
                if self.hp.isSignUpModalLabelPresent():
                    self.hp.setsignupfirstname(configData.SIGN_UP_FIRST_NAME)
                    self.hp.setsignuplastname(configData.SIGN_UP_LAST_NAME)
                    self.hp.setsignupemail(configData.USER_NAME)
                    self.hp.setsignuppassword(configData.PASSWORD)
                    self.hp.clickSignUpBtn()
                    if self.hp.isExistingEmailErrorMsgPresent():
                        self.hp.clickSignUpModalCancel()
                        self.hp.clickLogo()
                        assert True
                    else:
                        self.hp.clickLogo()
                        assert False
                else:
                    self.hp.clickLogo()
                    assert False
            else:
                self.hp.clickLogo()
                assert False
        else:
            self.hp.clickLogo()
            assert False

    def test_007_Validate_Wrong_Email_Password_Reset(self):

        self.hp = HomePage(self.driver)
        self.hp.clicksiginlink()

        if self.hp.clickForgotPasswordLink():

            if self.hp.isResetPasswordModalLabelPresent():
                self.hp.setresetpasswordemail(XLUtils.readData(self.testDataFilePath, 'HomePage', 2, 6))
                if self.hp.clickResetPasswordBtn():
                    if self.hp.isNotRegisteredEmailErrMsgPresent():
                        self.hp.clickResetPasswordModalCancel()
                        self.hp.clickLogo()
                        assert True
                    else:
                        self.hp.clickLogo()
                        assert False
                else:
                    self.hp.clickLogo()
                    assert False
            else:
                self.hp.clickLogo()
                assert False
        else:
            self.hp.clickLogo()
            assert False






