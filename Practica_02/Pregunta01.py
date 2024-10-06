class Persona:
    nacionalidad='peruana'
    def __init__(self,sueldo):
        self.sueldo=sueldo

    def pedir_datos(self):
        self.nombre = input('Ingrese el nombre de la persona: ')
        self.edad = int(input('Ingrese la edad de la persona: '))
        self.edadb=self.edad
        print('Los datos básicos de {} has sido guardados correctamente.'.format(self.nombre))

    def cumpleanos(self):
        self.edad=self.edad+1
        print('{} ahora tiene {} años.'.format(self.nombre,self.edad))

    def aumento_sueldo(self):
        self.sueldo=self.sueldo*1.3
        print('{} ha recibido un aumento de sueldo, ahora gana {} soles mensuales.'.format(self.nombre,self.sueldo))

    def mensaje(self,anno):
        if anno<2024:
            print('Año ingresado es inválido.')
        else:
            self.edadb=self.edadb+(anno-2024)
            print('En el año {}, {} tendrá {} años.'.format(anno,self.nombre,self.edadb))

#primera persona
per1=Persona(3000)
per1.pedir_datos()
per1.cumpleanos()
per1.cumpleanos()
per1.aumento_sueldo()
per1.mensaje(2040)
#segunda persona
per2=Persona(1800)
per2.pedir_datos()
per2.cumpleanos()
per2.cumpleanos()
per2.cumpleanos()
per2.aumento_sueldo()
per2.mensaje(2026)