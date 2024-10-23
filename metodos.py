from selenium.webdriver import Keys
from localizadores import Localizadores
import helpers
import data

class Metodos:
    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*Localizadores.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*Localizadores.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*Localizadores.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*Localizadores.to_field).get_property('value')

    def set_route(self, address_from, address_to):
        helpers.wait_elements(self.driver, Localizadores.from_field)
        helpers.wait_elements(self.driver, Localizadores.to_field)
        self.set_from(address_from)
        self.set_to(address_to)

    def click_order_taxi_button(self):
        helpers.wait_elements(self.driver, Localizadores.order_taxi_button)
        self.driver.find_element(*Localizadores.order_taxi_button).click()

    def click_confort_fee_button(self):
        helpers.wait_elements(self.driver, Localizadores.confort_fee_button)
        self.driver.find_element(*Localizadores.confort_fee_button).click()

    def fill_phone_fild(self):
        self.driver.find_element(*Localizadores.phone_field).click()
        helpers.wait_elements(self.driver, Localizadores.phone_field_popup)
        self.driver.find_element(*Localizadores.phone_field_popup).send_keys(data.Data.phone_number)
        self.driver.find_element(*Localizadores.phone_button).click()
        validation_code = helpers.retrieve_phone_code(self.driver)
        self.driver.find_element(*Localizadores.validation_code_field).send_keys(validation_code)
        self.driver.find_element(*Localizadores.confirm_phone_button).click()

    def add_credit_card(self):
        self.driver.find_element(*Localizadores.payment_method).click()
        self.driver.find_element(*Localizadores.add_card).click()
        self.driver.find_element(*Localizadores.card_number_field).send_keys(data.Data.card_number)
        self.driver.find_element(*Localizadores.card_code_field).send_keys(data.Data.card_code)
        self.driver.find_element(*Localizadores.card_code_field).send_keys(Keys.TAB)
        self.driver.find_element(*Localizadores.add_card_button).click()
        self.driver.find_element(*Localizadores.close_add_card_modal).click()

    def add_driver_comment(self):
        self.driver.find_element(*Localizadores.driver_comment).send_keys(data.Data.message_for_driver)

    def add_blanket_handkerchiefs(self):
        self.driver.find_element(*Localizadores.blanket_handkerchiefs).click()

    def add_icecream(self):
        self.driver.find_element(*Localizadores.icecream_counter).click()
        self.driver.find_element(*Localizadores.icecream_counter).click()

    def click_taxi_button(self):
        self.driver.find_element(*Localizadores.get_taxi_button).click()
