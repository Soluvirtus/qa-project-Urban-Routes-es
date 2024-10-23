from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from metodos import Metodos
from data import Data

class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        options = Options()
        options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.maximize_window()

    def test_set_route(self):
        self.driver.get(Data.urban_routes_url)
        routes_page = Metodos(self.driver)
        address_from = Data.address_from
        address_to = Data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_taxi_button(self):
        routes_page = Metodos(self.driver)
        routes_page.click_order_taxi_button()
        assert self.driver.find_element(*Metodos.confort_fee_button).get_property('alt') == "Comfort"

    def test_confort_button(self):
        routes_page = Metodos(self.driver)
        routes_page.click_confort_fee_button()
        element_showed = self.driver.find_element(*Metodos.element_showed)
        assert element_showed.get_attribute("class") == "r-sw-label"

    def test_fill_phone_number(self):
        routes_page = Metodos(self.driver)
        routes_page.fill_phone_fild()
        assert self.driver.find_element(*Metodos.phone_field).text == Data.phone_number

    def test_add_credit_card(self):
        routes_page = Metodos(self.driver)
        routes_page.add_credit_card()
        assert self.driver.find_element(*Metodos.card_img).get_property('alt') == "card"

    def test_add_driver_comment(self):
        routes_page = Metodos(self.driver)
        routes_page.add_driver_comment()
        assert self.driver.find_element(*Metodos.driver_comment).get_property("value") == Data.message_for_driver

    def test_add_blanket_handkerchiefs(self):
        routes_page = Metodos(self.driver)
        routes_page.add_blanket_handkerchiefs()
        assert self.driver.find_element(*Metodos.blanket_handkerchiefs_input).is_selected()

    def test_add_icecream(self):
        routes_page = Metodos(self.driver)
        routes_page.add_icecream()
        assert self.driver.find_element(*Metodos.icecream_counter_value).text == '2'

    def test_click_taxi_button(self):
        routes_page = Metodos(self.driver)
        routes_page.click_taxi_button()
        assert self.driver.find_element(*Metodos.order_header_title).text == "Buscar automóvil"
        helpers.wait_elements(self.driver, Metodos.driver_img, 60)
        assert not self.driver.find_element(*Metodos.order_header_title).text == "Buscar automóvil"
        assert self.driver.find_element(*Metodos.driver_img).get_property('alt') == "close"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
