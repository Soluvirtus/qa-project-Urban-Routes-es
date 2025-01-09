# Proyecto de Pruebas Automatizadas con Selenium
_Por Antonio Ávila Martínez_

Este proyecto utiliza Selenium y Pytest para realizar pruebas automatizadas de una aplicación web de servicios de taxis privados con nuevas funciones incorporadas. El proyecto está estructurado utilizando el método Page Object Model (POM), lo que facilita el mantenimiento y la escalabilidad de las pruebas.

## Descripción de los Archivos

### 1. `main.py`
Este archivo es el punto de entrada para ejecutar las pruebas. Contiene una clase `TestUrbanRoutes` con múltiples métodos de prueba que verifican diferentes funcionalidades de la aplicación. Usa Pytest para ejecutar las pruebas.

### 2. `data.py`
Este archivo contiene una clase `Data` que almacena datos estáticos y configuraciones utilizadas en las pruebas. Almacena información como URLs, direcciones, números de teléfono y datos de tarjetas de crédito.

### 3. `UrbanRoutesPage.py`
Este archivo define una clase `UrbanRoutesPage` que contiene los localizadores y métodos necesarios para interactuar con los elementos de la página web. Cada método realiza una acción específica, como llenar un campo de texto o hacer clic en un botón.

### 4. `helpers.py`
Este archivo contiene funciones auxiliares que se utilizan en múltiples pruebas. Incluye funciones para esperar elementos (`wait_elements`) y recuperar códigos de confirmación (`retrieve_phone_code`).

## Desglose del Flujo de Trabajo

### Inicio de Pruebas (`main.py`)
- Las pruebas se inician y se configuran con la clase `TestUrbanRoutes`.
- El método `setup_class` configura el driver de Selenium para Chrome y maximiza la ventana del navegador.

### Datos (`data.py`)
- `data.py` proporciona los datos necesarios para las pruebas, como URLs y credenciales.

### Métodos de Interacción (`UrbanRoutesPage.py`)
- `UrbanRoutesPage` define las acciones que se pueden realizar en la página web, utilizando los localizadores que están también en este archivo.
- Ejemplo: `set_route` usa `wait_elements` para esperar que los campos "from" y "to" estén disponibles, y luego los llena con direcciones.

### Funciones Auxiliares (`helpers.py`)
- `wait_elements` espera que un elemento esté presente en la página.
- `retrieve_phone_code` extrae un código de confirmación de los logs de la red.

## Ejemplo de una Prueba

### `test_set_route`
Navega a la URL, establece una ruta de origen a destino y verifica que los valores establecidos sean correctos.

```python
def test_set_route(self):
    self.driver.get(Data.urban_routes_url)
    routes_page = UrbanRoutesPage(self.driver)
    address_from = Data.address_from
    address_to = Data.address_to
    routes_page.set_route(address_from, address_to)
    assert routes_page.get_from() == address_from
    assert routes_page.get_to() == address_to

    
   ```
### Instalación de python.
Desde una terminal linux escribe 
`sudo apt install python3`

### Instructivo para la Instalación de Librerías Necesarias, Clonar Repositorio y Ejecutar las Pruebas.

Para instalar todas las librerías necesarias.
Asegúrate de tener pip instalado y ejecuta los siguientes comandos:

```sh
# Clona el repositorio
git clone https://github.com/Soluvirtus/qa-project-Urban-Routes-es

# Cambia al directorio del proyecto
cd qa-project-Urban-Routes-es

# Instala pytest
pip install pytest

# Instala selenium
pip install selenium

# Ejecuta las pruebas
pytest main.py
 
   ```
¡Y eso es todo! Ahora tienes Python, las librerías necesarias y puedes ejecutar las pruebas de este programa.