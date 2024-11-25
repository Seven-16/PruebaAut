import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager 
import time
import os

# log
logging.basicConfig(filename="reporte_test.log", level=logging.INFO)
logging.info("Iniciando prueba con Selenium")


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.maximize_window()

# Abrir
driver.get("http://localhost:5147/")


if not os.path.exists("capturas"):
    os.makedirs("capturas")


driver.get_screenshot_as_file("capturas/captura1.png")
time.sleep(4)

# HTML Report Setup
html_report = """
<html>
<head>
    <title>Reporte de Prueba Selenium</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        h1 {
            color: #4CAF50;
        }
        h2 {
            color: #333;
        }
        .step {
            margin: 10px 0;
            padding: 10px;
            background-color: #f1f1f1;
            border-left: 5px solid #4CAF50;
        }
        .screenshot {
            margin: 10px 0;
        }
        img {
            max-width: 100%;
            height: auto;
        }
        .result {
            color: #333;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <h1>Reporte de Prueba Selenium</h1>
    <h2>Detalles de la prueba ejecutada:</h2>
"""

# Localizar insertar
btnInsertar = driver.find_element(By.ID, "botonInsertar") 
btnInsertar.click()
time.sleep(2)

inputMatricula = driver.find_element(By.ID, "matricula_input") 
inputMatricula.send_keys("20231350")
html_report += f"""
    <div class="step">
        <p>Ingresado Matricula: 20231350</p>
        <div class="screenshot">
            <img src="capturas/captura1.png" alt="Captura 1">
        </div>
    </div>
"""

inputNombre = driver.find_element(By.ID, "nombre_input") 
inputNombre.send_keys("Prueba")
html_report += f"""
    <div class="step">
        <p>Ingresado Nombre: Prueba</p>
    </div>
"""

inputApellido = driver.find_element(By.ID, "apellido_input") 
inputApellido.send_keys("Automatizada")
html_report += f"""
    <div class="step">
        <p>Ingresado Apellido: Automatizada</p>
    </div>
"""

inputCurso = driver.find_element(By.ID, "curso_input") 
inputCurso.send_keys("1ro bachiller")
html_report += f"""
    <div class="step">
        <p>Ingresado Curso: 1ro bachiller</p>
    </div>
"""

inputMotivo = driver.find_element(By.ID, "motivo_input") 
inputMotivo.send_keys("Le cogió el sueño")
html_report += f"""
    <div class="step">
        <p>Ingresado Motivo: Le cogió el sueño</p>
    </div>
"""


driver.get_screenshot_as_file("capturas/captura2.png")
time.sleep(2)

btnGuardar = driver.find_element(By.ID, "guardarBtn") 
btnGuardar.click()

html_report += f"""
    <div class="step">
        <p>Formulario guardado.</p>
        <div class="screenshot">
            <img src="capturas/captura2.png" alt="Captura de pantalla formulario guardado">
            <img src="capturas/captura3.png" alt="Captura de pantalla formulario guardado">
        </div>
    </div>
"""

driver.get_screenshot_as_file("capturas/captura3.png")

# Cerrar
time.sleep(5)
driver.quit()

html_report += """
    <h2>Resultado de la prueba:</h2>
    <p class="result">Prueba ejecutada con éxito.</p>
</body>
</html>
"""

# Guardar HTML
with open("reporte_prueba.html", "w") as f:
    f.write(html_report)

logging.info("Prueba ejecutada exitosamente y reporte generado.")
