
import unittest

from UI import detector_neumonia

#Se encarga de comprobar la correcta carga de imagenes

class test2(unittest.TestCase):
    def test2(self):
        detector_neumonia.App.load_img_file(self)