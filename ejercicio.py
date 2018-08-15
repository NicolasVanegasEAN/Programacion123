#Definir
def obtener_salario_neto(salario, tasa):
    '''
    Calcula salio neto descontando la retencion en la fuente

    >>> obtener_salario_neto(100,2)
    98.0

    >>> obtener_salario_neto(200,10)
    180.0

    >>> obtener_salario_neto(100,0)
    100.0

    :param salario:
    :param tasa:
    :return:
    '''

    salario_neto = salario * (100 - tasa) / 100
    return salario_neto

#Llamar la funcion 3 veces
salario_neto_1 = obtener_salario_neto(float(input("digite su salario"))),
