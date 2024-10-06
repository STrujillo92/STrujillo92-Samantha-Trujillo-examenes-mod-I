dinero=[]
class Persona:
    nacionalidad='peruana'
    def __init__(self,sueldo,saldo):
        self.sueldo=sueldo
        self._saldo=saldo

    def pedir_datos(self):
        self.nombre = input('Ingrese el nombre de la persona: ')
        self.edad = int(input('Ingrese la edad de la persona: '))
        print('Los datos básicos de {} has sido guardados correctamente.'.format(self.nombre))

    def mostrar_saldo(self):
        print('{}, tu saldo en cuenta es de {} soles.'.format(self.nombre,self._saldo))

    def transferir(self,monto):
        if self._saldo<monto:
            print('Lo sentimos {}, saldo insuficiente. Solo quedan {} soles en cuenta.'.format(self.nombre,self._saldo))
        else:
            self._saldo=self._saldo-monto
            dinero.append(monto)
            print('Felicidades {}, operación exitosa. Estás transfiriendo {} soles.'.format(self.nombre,monto))
            print('{}, el saldo en tu cuenta es de {} soles.'.format(self.nombre,self._saldo))


class Persona2(Persona):
    def __init__(self,sueldo,saldo):
        super().__init__(sueldo, saldo)
        self.saldo=saldo

    def mostrar_saldo(self):
        self.saldo=self.saldo+dinero[0]
        dinero.clear()
        print('Receptor: Tu saldo en cuenta es de {} soles.'.format(self.saldo))

per1=Persona(5000,1000)
per2=Persona2(5000,0)
per1.pedir_datos()
per1.mostrar_saldo()
per1.transferir(500)
per2.mostrar_saldo()
per1.transferir(300)
per2.mostrar_saldo()
per1.transferir(500)
