

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Config.config import configData



class SearchPage:

    BREADCRUMB_SEARCH = (By.XPATH, '/html/body/main/div[4]/div/div/div/nav/ul/li[3]')
    NUMBER_OF_ITEMS_RETURNED = (By.XPATH, '/html/body/main/div[4]/div/div/div/div[3]/div/div/div/div[1]/div[2]/div[1]/div/span')

    def __init__(self, driver):
        self.driver = driver

    def isSearchResultBreadCrumbPresent(self):
        try:
            if WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.BREADCRUMB_SEARCH)).text.strip().upper() == 'SEARCH':
                return True
            else:
                return False
        except:
            return False

    def isSearchResultNumberMatching(self, number):
        if WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.NUMBER_OF_ITEMS_RETURNED)).text.strip() == str(number) + ' Products':
            return True
        else:
            return False