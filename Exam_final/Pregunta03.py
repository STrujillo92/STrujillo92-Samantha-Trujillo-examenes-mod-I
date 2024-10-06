lista=[]

def funcionADecoradora(funcionB):

    def funcionC(*args, **kwargs):
        print('Está por ejecutarse la función.')
        suma = 0
        for arg in args:
            suma = suma + arg
        for value in kwargs.values():
            suma = suma + value
        print('La suma de los parámetros es: {}'.format(suma))
        resultado=funcionB(*args, **kwargs)
        print('La función ha sido ejecutada correctamente.')
        return resultado
    return funcionC


@funcionADecoradora
def mayor(*args,**kwargs):
    for arg in args:
        lista.append(arg)
    for value in kwargs.values():
        lista.append(value)
    lista.sort()
    print('El mayor valor ingresado fue: {}'.format(lista[-1]))
    lista.clear()


mayor(5,8,2,num=20,num1=1,num2=4)
mayor(n1=10,n2=5,n3=8)
mayor(5,7,9,25,140)