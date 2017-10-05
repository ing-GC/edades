
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

