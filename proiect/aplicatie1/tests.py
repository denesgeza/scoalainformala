import datetime
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Create your tests here.
from proiect.settings import USERNAME, PASSWORD


class LocationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('http://127.0.0.1:8000/')
        username = self.driver.find_element(by=By.NAME, value='username')
        username.send_keys(USERNAME)
        password = self.driver.find_element(by=By.NAME, value='password')
        password.send_keys(PASSWORD)
        submit = self.driver.find_element(by=By.CLASS_NAME, value='btn-info')
        submit.submit()
        self.logs = open('logs.txt', mode='a')

    def test_form(self):
        if value := 'table' in self.driver.page_source:
            self.logs.write(f'{value}, {datetime.datetime.now()} \n')
        assert value

    def test_add_location(self):
        adauga = self.driver.find_element(by=By.ID, value='id_adaugare')
        adauga.click()
        city = self.driver.find_element(by=By.NAME, value='city')
        city.send_keys('Bucuresti')
        country = self.driver.find_element(by=By.NAME, value='country')
        country.send_keys('Romania')
        submit = self.driver.find_element(by=By.ID, value='add_location_submit')
        submit.submit()
        if value := 'table' in self.driver.page_source:
            self.logs.write(f'{value}, {datetime.datetime.now()} \n')
        assert value
