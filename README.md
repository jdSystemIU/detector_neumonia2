## Hola! Bienvenido a la herramienta para la detección rápida de neumonía

## Autores: Daniela Restrepo y Joseph David
Deep Learning aplicado en el procesamiento de imágenes radiográficas de tórax en formato JPG con el fin de clasificarlas en 3 categorías diferentes:

1. Neumonía Bacteriana

2. Neumonía Viral

3. Sin Neumonía

Aplicación de una técnica de explicación llamada Grad-CAM para resaltar con un mapa de calor las regiones relevantes de la imagen de entrada.

---
## Uso de la herramienta:

A continuación le explicaremos cómo empezar a utilizarla.

Requerimientos necesarios para el funcionamiento:

1. Instale VcXsrv Windows X Server.
2. Configure el display de Xlaunch; Seleccione la ventana "Multiple Windows" y en "Display number" digite -1. Finalmente, guarde el archivo de configuración antes de finalizar.
3. Ejecute el Xlaunch configurado en el menú de inicio.
4. Instale Docker en su escritorio. 
5. Ejecute e inicialice el servicio de Docker.
6. Diríjase al CMD y siga las siguientes instrucciones:
    - git clone https://github.com/jdSystemIU/detector_neumonia2.git
    - cd detector_neumonia_demo
    - docker build -t python:latest .
    - Linux o Mac:
    - docker run -it –rm -v /tmp/.X11-unix:/tmp/.X11-unix –net host -e DISPLAY=$DISPLAY python
    - Windows:
    - docker run -it --rm -e DISPLAY=host.docker.internal:0 --net host python 

Nota: Aplique los pasos 1, 2 y 3, en el caso de que su sistema operativo sea Windows. De lo contrario, omita los mismos. 
----------------------------------------------------------------------------------

## Testing:

Asegúrese de que este en funcionamiento Docker y Xlaunch.
Ejecute los siguientes pasos desde el directorio donde ha realizado el gitclone:

- cd detector_neumonia_demo
- docker run -it --rm -e DISPLAY=host.docker.internal:0 --net host python bash
- python -m unittest test1.py
- python -m unittest test2.py
----------------------------------------------------------------------------------
Uso de la Interfaz Gráfica:

- Ingrese la cédula del paciente en la caja de texto
- Presione el botón 'Cargar Imagen', seleccione la imagen del explorador de archivos del computador
- Presione el botón 'Predecir' y espere unos segundos hasta que observe los resultados
- Presione el botón 'Guardar' para almacenar la información del paciente en un archivo excel con extensión .csv
- Presione el botón 'PDF' para descargar un archivo PDF con la información desplegada en la interfaz
- Presión el botón 'Borrar' si desea cargar una nueva imagen

---

## Explicación de los scripts

## BACKEND

### integrator.py

Es un módulo que integra los demás scripts y retorna solamente lo necesario para ser visualizado en la interfaz gráfica.

Retorna la clase, la probabilidad y una imagen el mapa de calor generado por Grad-CAM.

### messages.py

Es un modulo perteneciente al backend donde se retornan los mensajes de confirmacion, que se van a visualizar en la UI

### read_img.py

Script que lee la imagen en formato JPG - JPEG para visualizarla en la interfaz gráfica. Además, la convierte a arreglo para su preprocesamiento.

## INFERENCE

### grad_cam.py

Script que recibe la imagen y la procesa, carga el modelo, obtiene la predicción y la capa convolucional de interés para obtener las características relevantes de la imagen.

### load_model.py

Script que lee el archivo binario del modelo de red neuronal convolucional previamente entrenado llamado 'WilhemNet86.h5'.

### preprocess_img.py

Script que recibe el arreglo proveniento de read_img.py, realiza las siguientes modificaciones:
- resize a 512x512
- conversión a escala de grises
- ecualización del histograma con CLAHE
- normalización de la imagen entre 0 y 1
- conversión del arreglo de imagen a formato de batch (tensor)

## UI

### detector_neumonia.py

Contiene el diseño de la interfaz gráfica utilizando Tkinter.

Los botones llaman métodos contenidos en otros scripts.

---
## Modelo de Aprendizaje Automático

La red neuronal convolucional implementada (CNN) es basada en el modelo implementado por F. Pasa, V.Golkov, F. Pfeifer, D. Cremers & D. Pfeifer
en su artículo Efcient Deep Network Architectures for Fast Chest X-Ray Tuberculosis Screening and Visualization.

Está compuesta por 5 bloques convolucionales, cada uno contiene 3 convoluciones; dos secuenciales y una conexión 'skip' que evita el desvanecimiento del gradiente a medida que se avanza en profundidad.
Con 16, 32, 48, 64 y 80 filtros de 3x3 para cada bloque respectivamente.

Después de cada bloque convolucional se encuentra una capa de max pooling y después de la última una capa de Average Pooling seguida por tres capas fully-connected (Dense) de 1024, 1024 y 3 neuronas respectivamente.

Para regularizar el modelo utilizamos 3 capas de Dropout al 20%; dos en los bloques 4 y 5 conv y otra después de la 1ra capa Dense.

## Técnica Grad-CAM

Es utilizada para resaltar las regiones de una imagen que son importantes para la clasificación. Un mapeo de activaciones de clase para una categoría en particular indica las regiones de imagen relevantes utilizadas por la CNN para identificar esa categoría.

Grad-CAM realiza el cálculo del gradiente de la salida correspondiente a la clase a visualizar con respecto a las neuronas de una cierta capa de la CNN. Esto permite tener información de la importancia de cada neurona en el proceso de decisión de esa clase en particular. Una vez obtenidos estos pesos, se realiza una combinación lineal entre el mapa de activaciones de la capa y los pesos, de esta manera, se captura la importancia del mapa de activaciones para la clase en particular y se ve reflejado en la imagen de entrada como un mapa de calor con intensidades más altas en aquellas regiones relevantes para la red con las que clasificó la imagen en cierta categoría.

