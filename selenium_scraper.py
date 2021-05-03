from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd

# Indicamos el navegador y la pagina a scrapear
driver = webdriver.Chrome("./chromedriver.exe")
driver.get("https://www.mercadolibre.com.ar/")

# Ingresar en esta variable lo que se quisiera buscar
busqueda = "cartuchos hp"

# Buscamos segun los parametros dados
barra_busqueda = driver.find_element_by_xpath('/html/body/header/div/form/input[@class="nav-search-input"]')
barra_busqueda.send_keys(busqueda)
barra_busqueda.send_keys(Keys.ENTER)
sleep(1)

# Obtenemos todos los elementos productos
productos = driver.find_elements_by_xpath('//li[@class="ui-search-layout__item"]')

# Obtenemos la pagina en la que nos encontramos y la cambiamos a entero para poder operar con ella
actual_page = int(
    driver.find_element_by_xpath('//li[@class="andes-pagination__button andes-pagination__button--current"]').text)

# Indicamos al programa cuantas paginas debemos que scrapear
num_pages = 3

# Aceptamos las cookies
cookies = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="cookieDisclaimerButton"]')))
cookies.click()

# En esta lista se almacenarán los productos
todos_productos = []

# Iteramos en los productos y los guardamos
for producto in productos:
    title = producto.find_element_by_xpath('.//h2[@class="ui-search-item__title"]').text
    price = producto.find_element_by_xpath('.//span[@class="price-tag-fraction"]').text
    todos_productos.append([title, price])

# Avanzamos a la siguiente pagina
path = '//main//div/div[1]/section/div[3]/ul/li/a[@title="Siguiente" and @role="button"]'
pag_siguiente = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, path)))
pag_siguiente.click()

# Iteramos en las paginas que queremos scrapear
for i in range(num_pages):
    # Actualizamos el valor en la pagina que estamos
    actual_page = int(
        driver.find_element_by_xpath('//li[@class="andes-pagination__button andes-pagination__button--current"]').text)
    # Si la pagina en la que entró el for es menor al numero de paginas a scrapear seguimos la operación
    if i < num_pages and actual_page == i + 1:
        # Obntener los productos
        productos = driver.find_elements_by_xpath('//li[@class="ui-search-layout__item"]')
        # Obtenemos todos los productos de esa pagina y los guardamos en la lista
        for producto in productos:
            price = producto.find_element_by_xpath('.//span[@class="price-tag-fraction"]').text
            title = producto.find_element_by_xpath('.//h2[@class="ui-search-item__title"]').text
            todos_productos.append([title, price])
        # Avanzamos de pagina
        path = '//main//div/div[1]/section/div[3]/ul/li/a[@title="Siguiente" and @role="button"]'
        pag_siguiente = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, path)))
        pag_siguiente.click()

# Generamos un archivo de excel y guardamos la información en ese archivo
df1 = pd.DataFrame(todos_productos, columns=["Titulo", "Precio"])
writer = pd.ExcelWriter('productos.xlsx')
df1.to_excel(writer)
writer.save()
