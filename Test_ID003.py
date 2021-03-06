import unittest
from hashlib import new

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestFilter(unittest.TestCase):
    def setUp(self):
        #Warunki początkowe testu
        # 1. Otwarta strona https://www.reserved.com/pl/pl/
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://www.reserved.com/pl/pl/")
        self.driver.implicitly_wait(30)

    def tearDown(self):
        # Zakończenie testu
        self.driver.quit()

    def testBySize(self, span=None):
        driver = self.driver
        # 1. Zaakceptuj popup z cookies
        accept_btn = driver.find_element(By.ID,"cookiebotDialogOkButton")
        accept_btn.click()

        #2. W Menu głównym najedź na pozycję "Kobieta"
        kobieta = driver.find_element(By.XPATH, '//a[text()="kobieta"]')
        webdriver.ActionChains(driver).move_to_element(kobieta).perform()

        #3. W rozwinietym podmenu kliknij na pozycję "Sukienki"
        sukienki = driver.find_element(By.XPATH, '//a[text()="Sukienki"]')
        sukienki.click()

        #4. Kliknij na przycisk Rozmiary
        filter_size = driver.find_element(By.XPATH, '//*[@id="categoryFilters"]/form/div/div[2]/label')
        filter_size.click()

        #5. Zaznacz wartość "34"
        small = driver.find_element(By.XPATH, '//*[@id="sizes-34"]')
        small.click()

        #6. Kliknij przycisk "Filtruj"
        size_enter = driver.find_element(By.XPATH, '//*[@id="categoryFilters"]/form/div/div[2]/ul/div/button')
        size_enter.click()
