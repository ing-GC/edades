
# -*- coding: utf-8 -*-
from lettuce import step, world
from Edades import Edades


@step(u'cuando realizo la operación')
def cuando_realizo_la_operacion(step):
    pass
@step(u'Dado que ingreso la edad "([^"]*)"')
def dado_que_ingreso_la_edad_group1(step, edad):
    world.ed = Edades()
    world.ed.edad(int(edad))
@step(u'entonces el resultado que obtengo es "([^"]*)"')
def entonces_el_resultado_que_obtengo_es_group1(step, group1):
    pass
