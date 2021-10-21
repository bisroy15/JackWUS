

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Config.config import configData
from selenium.webdriver.common.keys import Keys



class HomePage:


    JW_LOGO = (By.XPATH, '/html/body/main/header/div[1]/div[1]/span[1]/a/img')
    JW_LOGO_SCRPLLED_DOWN = (By.XPATH, '/html/body/main/header/div[1]/div[1]/span[2]/a/img')

    ##### Login Modal #####
    SIGN_IN_LINK = (By.XPATH, '/html/body/main/header/div[1]/div[7]/div/ul/li[3]/a/span')
    LOGIN_MODAL_LABEL = (By.XPATH, '//*[@id="gigya-login-form"]/div[1]/div[1]/label[1]/b')
    LOGIN_MODAL_SIGN_UP_LINK = (By.LINK_TEXT, 'Sign Up')
    LOGIN_MODAL_EMAIL = (By.NAME, 'username')
    LOGIN_MODAL_PASSWORD = (By.NAME, 'password')
    LOGIN_MODAL_SIGN_IN_BTN = (By.XPATH, '//*[@id="gigya-login-form"]/div[1]/div[1]/div[11]/input')
    LOGIN_MODAL_FORGOT_PASSWORD_LINK = (By.XPATH, '//*[@id="gigya-login-form"]/div[1]/div[1]/a[2]/b')
    ##### Login Modal #####

    ##### Sign Up Modal #####
    SIGN_UP_MODAL_HEADER = (By.XPATH, '//*[@id="register-site-login"]/div[1]/h2')
    SIGN_UP_FIRST_NAME = (By.NAME, 'profile.firstName')
    SIGN_UP_LAST_NAME = (By.NAME, 'profile.lastName')
    SIGN_UP_EMAIL = (By.NAME, 'email')
    SIGN_UP_PASSWORD = (By.NAME, 'password')
    SIGN_UP_SIGN_UP_BTN = (By.XPATH, '//*[@id="register-site-login"]/div[20]/input')
    SIGN_UP_MODAL_CANCEL_BTN = (By.XPATH, '//*[@id="gigya-register-form"]/div[1]/a')
    ##### Sign Up Modal #####

    ##### Reset Password Modal #####
    RESET_PASSWORD_MODAL_HEADER = (By.XPATH, '//*[@id="gigya-reset-password-form"]/div[1]/label')
    RESET_PASSWORD_EMAIL = (By.NAME, 'username')
    RESET_PASSWORD_RESET_BTN = (By.XPATH, '//*[@id="shiftdown"]/input')
    NOT_REGISTERED_EMAIL_ERROR_MSG = (By.XPATH, '//*[@id="reseterror"]')
    RESET_PASSWORD_MODAL_CANCEL_BTN = (By.XPATH, '//*[@id="gigya-reset-password-form"]/div[1]/a')
    ##### Reset Password Modal #####

    USER_NAME_AFTER_LOGIN = (By.XPATH, '/html/body/main/header/div[1]/div[7]/div/ul/li[3]/p[1]/a')
    LOGOUT_LINK = (By.LINK_TEXT,'Logout')
    INVALID_CREDENTIAL_MESSAGE = (By.XPATH, '//*[@id="gigya-login-form"]/div[1]/div[1]/div[5]/div')
    BLANK_EMAIL_MESSAGE = (By.XPATH, '//*[@id="gigya-login-form"]/div[1]/div[1]/div[7]/div/span')
    BLANK_PASSWORD_MESSAGE = (By.XPATH, '//*[@id="gigya-login-form"]/div[1]/div[1]/div[8]/div/span')
    MAIN_MENU_LINKS = (By.XPATH, '/html/body/main/header/div[1]/nav/div[3]/div/ul/li')
    HOMEPAGE_POPUP = (By.XPATH, '//*[@id="ltkpopup-content"]')
    HOMEPAGE_POPUP_CLOSE_BTN = (By.XPATH, '//*[@id="ltkpopup-close-button"]/a')
    NO_THANK_YOU_LINK_IN_POP_UP = (By.XPATH, '//*[@id="ltkpopup-text-btn"]/a')
    OUR_FAVOURITE_FIRST_ITEM = (By.XPATH, '/html/body/main/div[4]/div/div[1]/div[4]/div[2]/div/div/div/div[5]/div/div[1]/a[1]/img')
    SHOP_BY_CATEGORY_ITEMS = (By.XPATH, '/html/body/main/div[4]/div/div[1]/div[6]/div[2]/div/div/div/div')
    PARTIAL_XPATH_SHOP_BY_CAT_ITEM = '/html/body/main/div[4]/div/div[1]/div[6]/div[2]/div/div/div/div['
    EXISTING_EMAIL_ERROR_MSG = (By.XPATH, '//*[@id="register-site-login"]/div[8]/div/div/span')

    EXCLUSIONS_APPLY_LINK = (By.XPATH, '//*[@id="contactId"]/div[7]/label/a')

    ##### Search #####
    SEARCH_EDIT_FIELD = (By.ID, 'searchText')
    SEARCH_ICON = (By.XPATH, '/html/body/main/header/div[1]/div[7]/div/div/button[1]/img')
    TOP_SUGGESTION_MODAL_HEADER = (By.XPATH, '//*[@id="home"]/div/h2')
    ##### Search #####


    def __init__(self, driver):
        self.driver = driver

    def isTopSuggestionModalPresent(self):
        try:
            return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.TOP_SUGGESTION_MODAL_HEADER))
        except:
            return False

    def isSearchEditFieldPresent(self):
        try:
            return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SEARCH_EDIT_FIELD))
        except:
            return False

    def setSearchText(self, keyword):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SEARCH_EDIT_FIELD)).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SEARCH_EDIT_FIELD)).clear()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SEARCH_EDIT_FIELD)).send_keys(keyword)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SEARCH_EDIT_FIELD)).send_keys(Keys.ENTER)


    def isSearchIconPresent(self):
        try:
            return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SEARCH_ICON))
        except:
            return False

    def clickSearchIcon(self):
        if self.isSearchIconPresent() != False:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SEARCH_ICON)).click()
            return True
        else:
            return True

    def clickResetPasswordModalCancel(self):
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(*self.RESET_PASSWORD_MODAL_CANCEL_BTN))


    def isNotRegisteredEmailErrMsgPresent(self):
        try:
            return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.NOT_REGISTERED_EMAIL_ERROR_MSG))
        except:
            return False

    def isForgotPasswordLinkPresent(self):
        try:
            return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.LOGIN_MODAL_FORGOT_PASSWORD_LINK))
        except:
            return False

    def clickForgotPasswordLink(self):
        if self.isForgotPasswordLinkPresent():
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.LOGIN_MODAL_FORGOT_PASSWORD_LINK)).click()
            return True
        else:
            return False

    def isResetPasswordModalLabelPresent(self):
        try:
            return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.RESET_PASSWORD_MODAL_HEADER))
        except:
            return False

    def setresetpasswordemail(self, email):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.RESET_PASSWORD_EMAIL)).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.RESET_PASSWORD_EMAIL)).clear()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.RESET_PASSWORD_EMAIL)).send_keys(email)

    def clickResetPasswordBtn(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.RESET_PASSWORD_RESET_BTN)).click()
            return True
        except:
            return False


    def clickSignUpModalCancel(self):
        time.sleep(2)
        #WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SIGN_UP_MODAL_CANCEL_BTN)).click()

        self.driver.execute_script("arguments[0].click();", self.driver.find_element(*self.SIGN_UP_MODAL_CANCEL_BTN))

    def isSignUpLinkPresent(self):
        try:
            return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.LOGIN_MODAL_SIGN_UP_LINK))
        except:
            return False

    def isExistingEmailErrorMsgPresent(self):
        try:
            return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.EXISTING_EMAIL_ERROR_MSG))
        except:
            return False

    def clickSignUpLink(self):
        if self.isSignUpLinkPresent():
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.LOGIN_MODAL_SIGN_UP_LINK)).click()
            return True
        else:
            return False

    def isSignUpModalLabelPresent(self):
        if WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SIGN_UP_MODAL_HEADER)).text.strip().upper() == configData.SIGN_UP_MODAL_HEADER:
            return True
        else:
            return False

    def setsignupfirstname(self, firstname):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SIGN_UP_FIRST_NAME)).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SIGN_UP_FIRST_NAME)).clear()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SIGN_UP_FIRST_NAME)).send_keys(firstname)


    def setsignuplastname(self, lastname):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SIGN_UP_LAST_NAME)).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SIGN_UP_LAST_NAME)).clear()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SIGN_UP_LAST_NAME)).send_keys(lastname)

    def setsignupemail(self, email):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SIGN_UP_EMAIL)).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SIGN_UP_EMAIL)).clear()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SIGN_UP_EMAIL)).send_keys(email)

    def setsignuppassword(self, password):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SIGN_UP_PASSWORD)).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SIGN_UP_PASSWORD)).clear()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SIGN_UP_PASSWORD)).send_keys(password)

    def clickSignUpBtn(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SIGN_UP_SIGN_UP_BTN)).click()


    def isShopByCatItemsPresent(self):
        try:
            return len(self.driver.find_elements(*self.SHOP_BY_CATEGORY_ITEMS))
        except:
            return False

    def selectShopByCatItem(self, category):
        if self.isShopByCatItemsPresent() != False:
            for i in range(1, self.isShopByCatItemsPresent() + 1):
                finalXpath = self.PARTIAL_XPATH_SHOP_BY_CAT_ITEM + str(i) + ']/a/span'
                if self.driver.find_element_by_xpath(finalXpath).text.strip().upper() == category.strip().upper():
                    self.driver.execute_script("arguments[0].click();", self.driver.find_element_by_xpath(finalXpath))
                    return True
                    break
                elif i == self.isShopByCatItemsPresent() + 1:
                    return False
        else:
            return False

    def isOurFavoriteItemPresent(self):
        try:
            return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.OUR_FAVOURITE_FIRST_ITEM))
        except:
            return False

    def clickOurFavoriteItem(self):
        if self.isOurFavoriteItemPresent():

            elem = self.driver.find_element(*self.OUR_FAVOURITE_FIRST_ITEM)
            self.driver.execute_script("arguments[0].scrollIntoView();", elem)
            time.sleep(5)
            elem.click()
            return True
        else:
            return False

    def isHomePagePopUpPresent(self):
        try:
            return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.HOMEPAGE_POPUP))
        except:
            return False

    def closeHomePagePopUp(self):
        action = ActionChains(self.driver)
        elem = self.driver.find_element(*self.HOMEPAGE_POPUP_CLOSE_BTN)
        action.move_to_element(elem).click(elem).perform()

    def clickScrolledDownLogo(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.JW_LOGO_SCRPLLED_DOWN)).click()

    def clickLogo(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.JW_LOGO)).click()

    def isMainMenuPresent(self):
        try:
            elemList = self.driver.find_elements(*self.MAIN_MENU_LINKS)
            if len(elemList) > 0:
                return elemList
            else:
                return False
        except:
            return False

    def clickMainMenuItem(self, menuitem):
        try:
            if self.isMainMenuPresent() != False:
                for elem in self.isMainMenuPresent():
                    if elem.text == menuitem:
                        elem.click()
                        return True
        except:
            return False

    def isBlankEmailMsgPresent(self):
        try:
            return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.BLANK_EMAIL_MESSAGE))
        except:
            return False

    def isBlankPasswordMsgPresent(self):
        try:
            return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.BLANK_PASSWORD_MESSAGE))
        except:
            return False

    def isInvalidCredentialMsgPresent(self):
        try:
            return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.INVALID_CREDENTIAL_MESSAGE))
        except:
            return False

    def isSignInLinkPresent(self):
        try:
            return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SIGN_IN_LINK))
        except:
            return False

    def clicksiginlink(self):
        self.driver.find_element(*self.SIGN_IN_LINK).click()

    def setusername(self, email):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.LOGIN_MODAL_EMAIL)).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.LOGIN_MODAL_EMAIL)).clear()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.LOGIN_MODAL_EMAIL)).send_keys(email)

    def setpassword(self, password):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.LOGIN_MODAL_PASSWORD)).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.LOGIN_MODAL_PASSWORD)).clear()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.LOGIN_MODAL_PASSWORD)).send_keys(password)

    def clickSignInBtn(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.LOGIN_MODAL_SIGN_IN_BTN)).click()

    def isLoginModalPresent(self):
        try:
            #elem = self.driver.find_element(*self.LOGIN_MODAL_LABEL)
            return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.LOGIN_MODAL_LABEL))
        except:
            return False

    def getusername(self):
        try:
            return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.USER_NAME_AFTER_LOGIN)).text
            #elem = self.driver.find_element(*self.USER_NAME_AFTER_LOGIN)
            #return elem.text
        except:
            return False

    def clicklogoutlink(self):
        try:

            action = ActionChains(self.driver)
            elem = self.driver.find_element(*self.USER_NAME_AFTER_LOGIN)
            action.move_to_element(elem).perform()
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.LOGOUT_LINK)).click()
            return True
        except:
            return False

    def isExclusionsApplyLinkPresent(self):
        try:
            return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.EXCLUSIONS_APPLY_LINK))
        except:
            return False

    def clickExclusionsApplyLink(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.EXCLUSIONS_APPLY_LINK)).click()






