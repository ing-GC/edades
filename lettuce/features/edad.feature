Feature: Verificar edad
		Como usuario quiero verificar
		los distintos rangos de edades que hay 

	Scenario: Edad de -1
		Dado que ingreso la edad "-1" 
		cuando realizo la operación
		entonces el resultado que obtengo es "No existes"

	Scenario: Edad de 4
		Dado que ingreso la edad "4" 
		cuando realizo la operación
		entonces el resultado que obtengo es "Eres ninio"

	Scenario: Edad de 17
		Dado que ingreso la edad "17" 
		cuando realizo la operación
		entonces el resultado que obtengo es "Eres joven"

	Scenario: Edad de 30
		Dado que ingreso la edad "30" 
		cuando realizo la operación
		entonces el resultado que obtengo es "Eres adulto"

	Scenario: Edad de 70
		Dado que ingreso la edad "70" 
		cuando realizo la operación
		entonces el resultado que obtengo es "Eres adulto mayor"

	Scenario: Edad de 150
		Dado que ingreso la edad "150" 
		cuando realizo la operación
		entonces el resultado que obtengo es "Eres Mumm-Ra"

	
