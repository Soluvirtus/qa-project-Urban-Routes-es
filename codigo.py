def retrieve_phone_code(driver) -> str:
    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message") and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\nUtiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code

def wait_elements(driver, element, time=6):
    from selenium.webdriver.support import expected_conditions
    from selenium.webdriver.support.wait import WebDriverWait
    WebDriverWait(driver, time).until(expected_conditions.presence_of_element_located(element))

def wait(waiting_time=10):
    import time
    time.sleep(waiting_time)
