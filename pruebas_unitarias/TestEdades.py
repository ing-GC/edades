import unittest
from Edades import Edades
class TestEdades(unittest.TestCase):
	def test_edad_menos2(self):
		ed=Edades()
		ed.edad(-2)
		self.assertEquals(ed.obtener_edad(),'No existes')
	def test_edad_6_ninio(self):
		ed=Edades()
		ed.edad(6)
		self.assertEquals(ed.obtener_edad(),'Eres ninio')
	def test_edad_17_joven(self):
		ed=Edades()
		ed.edad(17)
		self.assertEquals(ed.obtener_edad(),'Eres joven')
	def test_edad_40_adulto (self):
		ed=Edades()
		ed.edad(40)
		self.assertEquals(ed.obtener_edad(),'Eres adulto')
	def test_edad_90_mayor(self):
		ed=Edades()
		ed.edad(90)
		self.assertEquals(ed.obtener_edad(),'Eres adulto mayor')
	def test_edad_130 (self):
		ed=Edades()
		ed.edad(130)
		self.assertEquals(ed.obtener_edad(),'Eres Mumm-Ra')

if __name__ == '__main__':
	unittest.main()