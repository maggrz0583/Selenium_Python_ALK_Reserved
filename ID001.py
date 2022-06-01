import unittest
from selenium import webdriver
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from time import sleep


class TestRegistration(unittest.TestCase):
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

    def testInvalidEmail(self, span=None):
        driver = self.driver
        # 1. Zaakceptuj popup z cookies
        accept_btn = driver.find_element(By.ID, "cookiebotDialogOkButton")
        accept_btn.click()

        # 2. Najedź na "Konto" - otwiera się menu z opcjami zalogowania/rejestracji
        profile_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[3]/div[2]")
        webdriver.ActionChains(driver).move_to_element(profile_button).perform()

        # 3. Kliknij "Zarejestruj się"
        register = driver.find_element(By.LINK_TEXT, "Zarejestruj się")
        register.click()

        # 4. Wpisz niepoprawny e-mail
        email_input = driver.find_element(By.ID, 'email_id')
        email_input.send_keys("magda$magda.pl")

        # 5. Wpisz imię
        imie_input = driver.find_element(By.ID, 'firstname_id')
        imie_input.send_keys("Magda")

        # 6. Wpisz nazwisko
        nazwisko_input = driver.find_element(By.ID, 'lastname_id')
        nazwisko_input.send_keys("Lena")

        # 7. Wpisz hasło
        haslo_input = driver.find_element(By.ID, 'password_id')
        haslo_input.send_keys("blabla123@")

        # 8. Zaznacz zgody na newsletter
        zgoda_radiobutton = driver.find_element(By.ID, 'is_subscribed_id')
        zgoda_radiobutton.click()

        # 9. Kliknij załóż konto
        register = driver.find_element(By.XPATH, '//*[@id="loginRegisterRoot"]/div/div[2]/div/form/button')
        register.click()



