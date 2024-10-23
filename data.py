"""
data.py

Este archivo contiene la clase Data con datos estáticos y configuraciones utilizadas en las pruebas.
Almacena información como URLs, direcciones, números de teléfono y datos de tarjetas de crédito.
"""
class Data:
    urban_routes_url = 'https://cnt-ee435e23-734e-4bb3-a1f7-ce95b3190b9a.containerhub.tripleten-services.com/?lng=es'
    address_from = 'East 2nd Street, 601'
    address_to = '1300 1st St'
    phone_number = '+1 123 123 12 12'
    card_number, card_code = '1234 5678 9100', '111'
    message_for_driver = 'Traiga un aperitivo'
