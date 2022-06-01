import unittest
from hashlib import new

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestSorting(unittest.TestCase):
    def setUp(self):
        #Warunki początkowe testu
        # 1. Otwarta strona https://www.reserved.com/pl/pl/
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://www.reserved.com/pl/pl/")


    def tearDown(self):
        # Zakończenie testu
        self.driver.quit()

    def testBySize(self, span=None):
        driver = self.driver
        # 1. Zaakceptuj popup z cookies
        driver.implicitly_wait(30)
        accept_btn = driver.find_element(By.ID,"cookiebotDialogOkButton")
        accept_btn.click()

        #2. W Menu głównym najedź na pozycję "Kobieta"
        kobieta = driver.find_element(By.XPATH, '//*[@id="navigation-wrapper"]/div/ul/li[2]/a')
        driver.implicitly_wait(30)
        webdriver.ActionChains(driver).move_to_element(kobieta).perform()

        #3. W rozwinietym podmenu kliknij na pozycję "Sukienki"
        sukienki = driver.find_element(By.LINK_TEXT, 'Sukienki')
        sukienki.click()

        #4. Kliknij na przycisk Rozmiary
        sortuj = driver.find_element(By.XPATH, '//*[@id="categoryFilters"]/form/div/div[2]/label')
        sortuj.click()

        #5. Zaznacz wartość "34"
        small = driver.find_element(By.XPATH, '//*[@id="sizes-34"]')
        small.click()

        #6. Kliknij przycisk "Filtruj"
        size_enter = driver.find_element(By.XPATH, '//*[@id="categoryFilters"]/form/div/div[2]/ul/div/button')
        size_enter.click()