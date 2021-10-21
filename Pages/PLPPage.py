
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities import XLUtils


class PLPPage:
    testDataFilePath = ".//TestData//HomePageData.xlsx"

    #BREADCRUMB_LINK = (By.LINK_TEXT, XLUtils.readData(testDataFilePath, 'HomePage', 2, 1))
    BREADCRUMB = (By.XPATH, '/html/body/main/div[4]/div/div/div/nav/ul/li')

    def __init__(self, driver):
        self.driver = driver

    def isComponentBreadCrumbpRESENT(self, link_text):
        try:
            BREADCRUMB_LINK = (By.LINK_TEXT, link_text)
            return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(BREADCRUMB_LINK))
        except:
            return False

