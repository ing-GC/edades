class Edades():
	def __init__(self):
		self.respuesta='Vacio'

	def obtener_edad(self):
		return self.respuesta
		
	def edad(self,edad):
		if(edad<0):
			self.respuesta= 'No existes'
		elif(edad>=0 and edad<13):
			self.respuesta= 'Eres ninio'
		elif(edad<18 and edad >=13):
			self.respuesta= 'Eres joven'
		elif(edad>=18 and edad<65):
			self.respuesta= 'Eres adulto'
		elif(edad>=65 and edad<120):
			self.respuesta= 'Eres adulto mayor'
		elif(edad>=120 and edad>120):
			self.respuesta= 'Eres Mumm-Ra'

