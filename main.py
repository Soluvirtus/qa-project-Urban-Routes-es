"""
main.py

Este archivo contiene la clase TestUrbanRoutes, que incluye pruebas automatizadas para la aplicación Urban Routes.
Las pruebas verifican funcionalidades clave como establecer rutas, botones de taxi, agregar tarjetas de crédito,
comentarios del conductor, entre otros.

Usa pytest para la ejecución de pruebas.
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from metodos import Metodos
from data import Data
from localizadores import Localizadores
import codigo


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono

        # from selenium.webdriver import DesiredCapabilities
        # capabilities = DesiredCapabilities.CHROME
        # capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        # cls.driver = webdriver.Chrome(desired_capabilities=capabilities)

        """
               Configura el driver de Selenium para Chrome y maximiza la ventana del navegador.
               """
        options = Options()
        options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.maximize_window()

    def test_set_route(self):
        """
                Verifica que se pueda establecer una ruta desde una dirección de origen a una de destino.
                """
        self.driver.get(Data.urban_routes_url)
        routes_page = Metodos(self.driver)
        address_from = Data.address_from
        address_to = Data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_taxi_button(self):
        """
                Verifica que el botón de ordenar taxi esté funcionando correctamente.
                """
        routes_page = Metodos(self.driver)
        routes_page.click_order_taxi_button()
        assert self.driver.find_element(*Localizadores.confort_fee_button).get_property('alt') == "Comfort"

    def test_confort_button(self):
        """
                Verifica que el botón de tarifa confort esté funcionando correctamente.
                """
        routes_page = Metodos(self.driver)
        routes_page.click_confort_fee_button()
        element_showed = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Manta y pañuelos')]")
        assert element_showed.get_attribute("class") == "r-sw-label"

    def test_fill_phone_number(self):
        """
                Verifica que se pueda llenar el campo de número de teléfono correctamente.
                """
        routes_page = Metodos(self.driver)
        routes_page.fill_phone_fild()
        assert self.driver.find_element(*Localizadores.phone_field).text == Data.phone_number

    def test_add_credit_card(self):
        """
                Verifica que se pueda agregar una tarjeta de crédito correctamente.
                """
        routes_page = Metodos(self.driver)
        routes_page.add_credit_card()
        assert self.driver.find_element(*Localizadores.card_img).get_property('alt') == "card"

    def test_add_driver_comment(self):
        """
                Verifica que se pueda agregar un comentario para el conductor correctamente.
                """
        routes_page = Metodos(self.driver)
        routes_page.add_driver_comment()
        assert self.driver.find_element(*Localizadores.driver_comment).get_property("value") == Data.message_for_driver

    def test_add_blanket_handkerchiefs(self):
        """
                Verifica que se pueda agregar mantas y pañuelos correctamente.
                """
        routes_page = Metodos(self.driver)
        routes_page.add_blanket_handkerchiefs()
        assert self.driver.find_element(*Localizadores.blanket_handkerchiefs_input).is_selected()

    def test_add_icecream(self):
        """
               Verifica que se pueda agregar helados correctamente.
               """
        routes_page = Metodos(self.driver)
        routes_page.add_icecream()
        assert self.driver.find_element(*Localizadores.icecream_counter_value).text == '2'

    def test_click_taxi_button(self):
        """
               Verifica que el botón de buscar taxi esté funcionando correctamente.
               """
        routes_page = Metodos(self.driver)
        routes_page.click_taxi_button()
        assert self.driver.find_element(*Localizadores.order_header_title).text == "Buscar automóvil"
        codigo.wait_elements(self.driver, Localizadores.driver_img, 60)
        assert self.driver.find_element(*Localizadores.driver_img).get_property('alt') == "close"

    @classmethod
    def teardown_class(cls):
        """
                Cierra el driver de Selenium.
                """
        cls.driver.quit()
