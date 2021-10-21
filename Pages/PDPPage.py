
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities import XLUtils

class PDPPage:

    testDataFilePath = ".//TestData//HomePageData.xlsx"

    PDP_ITEM_NAME = (By.XPATH, '//*[@id="productDetailsPage"]/div/div[2]/div[1]/h1')

    def __init__(self, driver):
        self.driver = driver

    def isPDPItemNamePresent(self):
        try:
            return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.PDP_ITEM_NAME))
        except:
            return False