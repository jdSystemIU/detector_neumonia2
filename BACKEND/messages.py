
from email import message
from tkinter import *
from tkinter import ttk, font, filedialog, Entry
from tkinter.messagebox import askokcancel, showinfo, WARNING
import getpass
import csv
from PIL import ImageTk, Image
import pyautogui
import tkcap
import img2pdf
import numpy as np
import time
#Paquetes propios
from BACKEND import read_img
from UI import detector_neumonia

#Mensajes que visualiza el usuario
#Se encarga de retornar los mensajes a detector_neumonia.py

save = "Los datos se guardaron con éxito."
pdf_successful = "El PDF fue generado con éxito."
confirmation_delete = "Se borrarán todos los datos."
delete_successful = "Los datos se borraron con éxito"

def save_():
        return save
        
def pdf_successful_():
        return pdf_successful

def confirmation_delete_():
        return confirmation_delete

def delete_successful_():
        return delete_successful 
        


  

