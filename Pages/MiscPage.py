

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities import XLUtils


class MiscPage:


    # New Page that appears after clicking Exclusions Apply
    DEALS_OFFERS_PAGE_HEADER = (By.XPATH, '//*[@id="header"]/div/div/h1')

    def __init__(self, driver):
        self.driver = driver


    # New Page that appears after clicking Exclusions Apply
    def isDealsAndOffersPagePresent(self):
        if WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.DEALS_OFFERS_PAGE_HEADER)) and WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.DEALS_OFFERS_PAGE_HEADER)).text.strip() == 'DEALS AND OFFERS':
            return True
        else:
            return False


