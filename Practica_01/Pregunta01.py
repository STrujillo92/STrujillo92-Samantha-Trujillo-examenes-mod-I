nombre="Samantha"
salario=2000
edad="32"
compania="Corporación ABC"
"""
Identificando tipos de variables
"""
print("La variable nombre de valor {} es de tipo {}".format(nombre,type(nombre)))
print("La variable salario de valor {} es de tipo {}".format(salario,type(salario)))
print("La variable edad de valor {} es de tipo {}".format(edad,type(edad)))
print("La variable compania de valor {} es de tipo {}".format(compania,type(compania)))
"""
Convirtiendo edad a int
"""
edad=int(edad)
print("La variable edad de valor {} es de tipo {}".format(edad,type(edad)))
"""
Clasificando la edad para el bono
"""
if edad>30:
    bono=0.1*salario
    print("Usted tiene un bono de 10% en el mes de diciembre.")
else:
    bono=0.05*salario
    print("Usted tiene un bono del 5% en el mes de diciembre.")
"""
Calculando bono final
"""
bonof=pow(salario,2)+bono
print("La bonificación final será de S/.{} soles.".format(bonof))