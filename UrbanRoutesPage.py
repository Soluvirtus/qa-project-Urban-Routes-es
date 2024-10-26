"""
UrbanRoutesPage.py

Este archivo define la clase UrbanRoutesPage, que contiene todos los elementos de la página web( localizadores y
métodos). Los localizadores se utilizan para encontrar y manipular elementos en la página y cada método realiza una
acción específica, como llenar un campo de texto o hacer clic en un botón."""

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import helpers
import data


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    order_taxi_button = (By.XPATH, "//button[@class='button round']")
    confort_fee_button = (By.XPATH, "//img[@alt='Comfort']")

    phone_field = (By.CSS_SELECTOR, ".np-text")
    phone_field_popup = (By.ID, "phone")
    phone_button = (By.XPATH, "//button[@type='submit']")
    confirm_phone_button = (By.XPATH, "(//button[@type='submit'])[2]")
    validation_code_field = (By.ID, "code")

    payment_method = (By.CSS_SELECTOR, ".pp-text")
    add_card = (By.CSS_SELECTOR, ".pp-plus")
    card_number_field = (By.ID, "number")
    card_code_field = (By.NAME, "code")
    add_card_button = (By.XPATH, "(//button[@type='submit'])[3]")
    close_add_card_modal = (By.CSS_SELECTOR, ".payment-picker .active > .close-button")
    card_img = (By.XPATH, "//img[@alt='card']")

    driver_comment = (By.ID, "comment")
    blanket_handkerchiefs = (By.CSS_SELECTOR, ".r:nth-child(1) .slider")
    blanket_handkerchiefs_input = (By.CSS_SELECTOR, ".r:nth-child(1) .switch-input")
    icecream_counter_value = (By.CSS_SELECTOR, ".r:nth-child(1) .counter-value")
    icecream_counter = (By.CSS_SELECTOR, ".r:nth-child(1) .counter-plus")

    get_taxi_button = (By.CSS_SELECTOR, ".smart-button-main")
    order_header_title = (By.CSS_SELECTOR, ".order-header-title")
    driver_img = (By.CSS_SELECTOR, ".order-button > img:nth-child(2)")

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        """
                      Establece la dirección de origen.
                      """
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        """
                        Establece la dirección de destino.
                        """
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        """
                       Obtiene la dirección de origen.
                       """
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        """
                      Obtiene la dirección de destino.
                      """
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, address_from, address_to):
        """
                      Establece una ruta desde una dirección de origen a una de destino.
                      """
        helpers.wait_elements(self.driver, self.from_field)
        helpers.wait_elements(self.driver, self.to_field)
        self.set_from(address_from)
        self.set_to(address_to)

    def click_order_taxi_button(self):
        """
                        Hace clic en el botón de ordenar taxi.
                        """
        helpers.wait_elements(self.driver, self.order_taxi_button)
        self.driver.find_element(*self.order_taxi_button).click()

    def click_confort_fee_button(self):
        """
                       Hace clic en el botón de tarifa confort.
                       """
        helpers.wait_elements(self.driver, self.confort_fee_button)
        self.driver.find_element(*self.confort_fee_button).click()

    def fill_phone_fild(self):
        """
                       Llena el campo de número de teléfono.
                       """
        self.driver.find_element(*self.phone_field).click()
        helpers.wait_elements(self.driver, self.phone_field_popup)
        self.driver.find_element(*self.phone_field_popup).send_keys(data.Data.phone_number)
        self.driver.find_element(*self.phone_button).click()
        validation_code = helpers.retrieve_phone_code(self.driver)
        self.driver.find_element(*self.validation_code_field).send_keys(validation_code)
        self.driver.find_element(*self.confirm_phone_button).click()

    def add_credit_card(self):
        """
                       Agrega una tarjeta de crédito.
                       """
        self.driver.find_element(*self.payment_method).click()
        self.driver.find_element(*self.add_card).click()
        self.driver.find_element(*self.card_number_field).send_keys(data.Data.card_number)
        self.driver.find_element(*self.card_code_field).send_keys(data.Data.card_code)
        self.driver.find_element(*self.card_code_field).send_keys(Keys.TAB)
        self.driver.find_element(*self.add_card_button).click()
        self.driver.find_element(*self.close_add_card_modal).click()

    def add_driver_comment(self):
        """
                       Agrega un comentario para el conductor.
                       """
        self.driver.find_element(*self.driver_comment).send_keys(data.Data.message_for_driver)

    def add_blanket_handkerchiefs(self):
        """
                       Agrega mantas y pañuelos.
                       """
        self.driver.find_element(*self.blanket_handkerchiefs).click()

    def add_icecream(self):
        """
                       Agrega helados.
                       """
        self.driver.find_element(*self.icecream_counter).click()
        self.driver.find_element(*self.icecream_counter).click()

    def click_taxi_button(self):
        """
                       Hace clic en el botón de buscar taxi.
                       """
        self.driver.find_element(*self.get_taxi_button).click()
