"""
localizadores.py

Este archivo define la clase Localizadores, que contiene todos los elementos de la página web.
Los localizadores se utilizan en metodos.py para encontrar y manipular elementos en la página.
"""
from selenium.webdriver.common.by import By


class Localizadores:
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
