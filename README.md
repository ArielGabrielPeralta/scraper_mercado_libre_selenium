# Scraper en Mercado Libre

### Funciones principales

Este scraper permite:

* Introducir un texto en la barra de busqueda.
* Introducir el numero de paginas de las cuales se quisieran extraer datos.
* Recopilar los datos del titular y el precio del producto.
* Incluir los datos recopilados en un archivo externo.

### Futuras funcionalidades

Proximo a implementar:

* Aplicar los filtros deseados.
* Implementar los parametros por consola al ejecutar el programa.
* Agregar una funcionalidad de **BOT** que:
    * Monitoree una publicación dada:
      * Finalización.
      * Baja o suba de precio.
      * Preguntas nuevas.  
    * Busque cada "x" tiempo un producto con ciertas caracteristicas.
      
    * ***En ambos casos se enviará un mail con las actualizaciones***

**Advertencia:** Solo funciona para la pagina de Mercado Libre.

## Para correr el programa

Se requiere:

* Python 3.9.1
* Pip

Ejecutamos la linea de codigo:

* $ pip install -r requirements.txt

Una vez instalado **requirements.txt** y modificado los datos del archivo **selenium_scraper.py** corremos el mismo:

* $ python selenium_scraper.py
 
