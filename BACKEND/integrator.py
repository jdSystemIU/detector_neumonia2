# Librerias
import numpy as np
import tensorflow as tf
from tensorflow.keras import models

# Paquetes propios
from INFERENCE import grad_cam
from INFERENCE import preprocess_img
from INFERENCE import load_model

# Función para preprocesar la imagén y cargar el modelo, a fin de realizar la predicción respecitva. 
# En este sentido, la predicción es la clasificación de la imagen en alguna de las clases 0, 1, 2. 

def predict(array): 
    # Funcion de call para preprocesar la imagén. Devuelve la imagen en formato por lotes. 
    batch_array_img = preprocess_img.preprocess(array)
    # Llamado a la función para cargar el modelo y predecir: devuelve la clase y la probabilidad predichas.
    model = load_model.model()
    prediction = np.argmax(model.predict(batch_array_img))
    proba = np.max(model.predict(batch_array_img))*100
    label = ''
    if prediction == 0:
        label = 'bacteriana'
    if prediction == 1:
        label = 'normal'
    if prediction == 2:
        label = 'viral'
    # Función de call para generar "Grad-CAM": devuelve una imagen con un mapa de calor superpuesto.
    heatmap = grad_cam.grad_cam(array)
    return(label, proba, heatmap)



    
    
