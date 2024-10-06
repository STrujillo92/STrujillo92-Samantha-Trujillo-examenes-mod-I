from datetime import datetime

tiempo=datetime.now()

def funcionADecoradora(funcionB):

    def funcionC(**kwargs):
        print('La cantidad de argumentos que tiene la función es')
        resultado=funcionB(**kwargs)
        print('La función decoradora terminó de ejecutarse correctamente.')
        return resultado
    return funcionC


@funcionADecoradora
def datos(**kwargs):
    cont=0
    for key in kwargs:
        cont+=1
    if cont>1:
        print(cont)
    else:
        print('Número de elementos ingresados incorrecto.')

datos(edad=input('Ingrese la edad: '),nombre=input('Ingrese el nombre: '),
      hora=tiempo.hour,minutos=tiempo.minute)

def funcionADecoradora2(funcionB):

    def funcionC(**kwargs):
        print('Hayando el promedio:')
        resultado=funcionB(**kwargs)
        print('La función decoradora terminó de ejecutarse correctamente.')
        return resultado
    return funcionC

@funcionADecoradora2
def media(**kwargs):
    cont=0
    suma=0
    for value in kwargs.values():
        suma=suma+value
        cont=cont+1
    prom=suma/cont
    print('La media de las {} notas es {}.'.format(cont,prom))

media(nota1=20,nota2=18,nota3=17,nota4=15)