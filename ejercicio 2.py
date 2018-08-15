def de_kelvin_a_centigrados(kelvin):
    '''

    :param kelvin:
    :return:
    '''
    return kelvin - 273

def convertir_dolares_a_pesos(dolar, trm):
    '''
    >>> convertir_dolares_a_pesos(20,3000)
    60000

    >>> convertir_dolares_a_pesos(50,3000)
    150000

    :param dolar: (num) el valor de los dolare a convertir
    :return trm: (num) el total en pesos de los dolares convertidos
    '''
    return dolar * trm
