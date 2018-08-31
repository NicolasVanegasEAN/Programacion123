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

a = 10
b = 2
c = a / b


#Hacer una funcion que calcule la divison de dos numeros (VALIDANDO QUE EL DENOMINADOR NO SEA 0)

def division(numerador, divisor):
    '''

    (num//num) -> float

    >>> division(10,2)
    5

    >>> division(10,0)
    'No puedo dividir entre 0'




    :param num: Numerador
    :param num: Denominador !=0
    :return: num
    '''

    if divisor == 0:
        return 'No puedo dividir entre 0'
    return numerador / divisor


def dividir(numerador,divisor):
    """"(num, num) -> float...."""""
    try:
        return numerador / divisor
    except ZeroDivisionError:
        return 'No puedo divir entre 0'



#Hacer un programa que lea por teclado dos numeros y diga cual es el mayor (VALIDE LA ENTRADA DE DATOS USANDO TRY)

#Leer los dos numeros

num_1 = input('Ingrese su primer numero')
num_2 = input('Ingrese su segundo numero')

#Intentar convertirlos
try:
    num_1 = float(num_1)
    num_2 = float(num_2)

#compararlos y decir cual es mayor
    if num_1 > num_2:
        print (num1,'es mayor',num2)
    elif num_2 == num_1:
        print(num_2, 'es igual que', num_1)
    else:
        print (num_2,'es mayor',num_1)

# Manejamos nuestros errores
except ValueError:
    print(num_1,'y', num_2, 'No son numeros validos')
