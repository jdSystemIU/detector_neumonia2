
import unittest

from BACKEND import messages

#Se encarga de que los mensajes que visualiza el usuario sean los correctos

class test1(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(messages.save_(),"Los datos se guardaron con éxito.")
        self.assertAlmostEqual(messages.pdf_successful_(),"El PDF fue generado con éxito.")
        self.assertAlmostEqual(messages.confirmation_(),"Se borrarán todos los datos.")
        self.assertAlmostEqual(messages.confirmation_delete_(),"Se borrarán todos los datos.")
        self.assertAlmostEqual(messages.delete_successful_(), "Los datos se borraron con éxito")