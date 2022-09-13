import tensorflow as tf
from tensorflow.keras import models

#Define el nombre del modelo, luego se encargar de cargar el modelo y retornarlo

def model():
    model_cnn = tf.keras.models.load_model('WilhemNet_86.h5')
    return model_cnn