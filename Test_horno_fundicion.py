import unittest
from Horno_fundicion_dental import Horno_Fundicion

class TestHorno_Fundicion(unittest.TestCase):

    def setUp(self):
        self.horno = Horno_Fundicion(24560, "Indef", "134D", "1,5L", "18Kg", "1,7Kw", 0, "Apagado")

    def test_creacion_horno(self):
        self.assertEqual(self.horno.get_Numero_serie(), 24560)
        self.assertEqual(self.horno.get_Marca(), "Indef")
        self.assertEqual(self.horno.get_Modelo(), "134D")
        self.assertEqual(self.horno.get_Capacidad(), "1,5L")
        self.assertEqual(self.horno.get_Peso(), "18Kg")
        self.assertEqual(self.horno.get_Potencia(), "1,7Kw")
        self.assertEqual(self.horno.get_Temperatura(), 0)
        self.assertEqual(self.horno.get_Estado(), "Apagado")

    def test_encender_horno(self):
        resultado = self.horno.encender()
        self.assertEqual(self.horno.get_Estado(), "Encendido")
        self.assertEqual(resultado, "Estado: Encendido")

    def test_apagar_horno(self):
        self.horno.encender() 
        resultado = self.horno.apagar()
        self.assertEqual(self.horno.get_Estado(), "Apagado")
        self.assertEqual(resultado, "Estado: Apagado")

    def test_incrementar_temperatura(self):
        self.horno.encender()  
        self.horno.__add__(50)  
        self.assertEqual(self.horno.get_Temperatura(), 50)

    def test_decrementar_temperatura(self):
        self.horno.encender() 
        self.horno.__add__(100)  
        resultado = self.horno.__sub__(30)  
        self.assertEqual(self.horno.get_Temperatura(), 70)
        self.assertEqual(resultado, "Temperatura ajustada en: 70")

    def test_decrementar_temperatura_inferior_a_cero(self):
        self.horno.encender()
        resultado = self.horno.__sub__(10)  
        self.assertEqual(self.horno.get_Temperatura(), 0)
        self.assertEqual(resultado, "La temperatura no puede ser inferior a 0°C.")

