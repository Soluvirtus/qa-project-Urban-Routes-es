from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from localizadores import UrbanRoutesPageLocators

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*UrbanRoutesPageLocators.FROM_FIELD).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*UrbanRoutesPageLocators.TO_FIELD).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*UrbanRoutesPageLocators.FROM_FIELD).get_property('value')

    def get_to(self):
        return self.driver.find_element(*UrbanRoutesPageLocators.TO_FIELD).get_property('value')

    def set_route(self, from_address, to_address):  # Aquí se aseguran los parámetros
        self.set_from(from_address)  # Cambiado 'from_address'
        self.set_to(to_address)  # Cambiado 'to_address'
