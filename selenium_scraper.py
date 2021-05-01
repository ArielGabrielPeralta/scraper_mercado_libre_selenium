from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

# Indicamos el navegador
driver = webdriver.Chrome("./chromedriver.exe")

# En este caso haremos escraper en mercado libre
driver.get("https://www.mercadolibre.com.ar/")

#Ahora a nuestra variable busqueda le damos la cadena de texto que deseamos introducir en la barra de busqueda
busqueda="cartuchos hp"

#Identificamos la barra de busqueda
barra_busqueda = driver.find_element_by_xpath('/html/body/header/div/form/input[@class="nav-search-input"]')

#Tipeamos busqueda en la barra
barra_busqueda.send_keys(busqueda)
#Enter en la barra de busqueda
barra_busqueda.send_keys(Keys.ENTER)

sleep(3)

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

# Como iniciamos en la pagina uno scrapeamos todos los elemenos productos de esa pagina
for producto in productos:
    title = producto.find_element_by_xpath('.//h2[@class="ui-search-item__title"]').text
    print(title)
    price = producto.find_element_by_xpath('.//span[@class="price-tag-fraction"]').text
    print(price)

# Click a la siguiente pagina
path = '//main//div/div[1]/section/div[3]/ul/li/a[@title="Siguiente" and @role="button"]'
pag_siguiente = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, path)))
pag_siguiente.click()

# Ahora nos encontramos en la pagina 2


# Haremos un for para navegar en las paginas que nos quedan
for i in range(num_pages):
    # Actualizamos el valor en la pagina que estamos
    actual_page = int(
        driver.find_element_by_xpath('//li[@class="andes-pagination__button andes-pagination__button--current"]').text)
    # Si la pagina en la que entró el for es menor al numero de paginas a scrapear seguimos la operación
    if i < num_pages and actual_page == i + 1:
        # Obntener los elementos cartuchos
        productos = driver.find_elements_by_xpath('//li[@class="ui-search-layout__item"]')
        # Scrapeamos todos los elemenos cartuchos de esa pagina
        for producto in productos:
            price = producto.find_element_by_xpath('.//span[@class="price-tag-fraction"]').text
            print(price)
            title = producto.find_element_by_xpath('.//h2[@class="ui-search-item__title"]').text
            print(title)
        # Click a la siguiente pagina
        path = '//main//div/div[1]/section/div[3]/ul/li/a[@title="Siguiente" and @role="button"]'
        pag_siguiente = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, path)))
        pag_siguiente.click()

print("Programa finalizado con exito")
