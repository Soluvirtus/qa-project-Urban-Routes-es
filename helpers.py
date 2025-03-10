"""
helpers.py

Este archivo contiene funciones auxiliares que se utilizan en múltiples pruebas.
Incluye funciones para esperar elementos y recuperar códigos de confirmación.
"""


def retrieve_phone_code(driver) -> str:
    """
    Devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación.

    Args:
        driver (WebDriver): El WebDriver de Selenium.

    Returns:
        str: El código de confirmación del teléfono.
    """
    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if
                    log.get("message") and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception(
                "No se encontró el código de confirmación del teléfono.\nUtiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


def wait_elements(driver, element, time=6):
    """
    Espera hasta que un elemento esté presente en la página.

    Args:
        driver (WebDriver): El WebDriver de Selenium.
        element (tuple): El localizador del elemento.
        time (int, opcional): El tiempo máximo de espera en segundos. Por defecto, es 6 segundos.
    """
    from selenium.webdriver.support import expected_conditions
    from selenium.webdriver.support.wait import WebDriverWait
    WebDriverWait(driver, time).until(expected_conditions.presence_of_element_located(element))


def wait(waiting_time=10):
    """
    Pausa la ejecución por un tiempo determinado.

    Args:
        waiting_time (int, opcional): El tiempo de espera en segundos. Por defecto, es 10 segundos.
    """
    import time
    time.sleep(waiting_time)
