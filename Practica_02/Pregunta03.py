class Billetera:
    cta_mn=0
    cta_usd=0
    def __init__(self,cta_mn,cta_usd):
        self.cta_mn=cta_mn
        self.cta_usd=cta_usd
        self.nombre=input('Ingrese el nombre del titular: ')
        self.apellido=input('Ingrese el apellido del titular: ')

    def transferir(self,monto):
        ope=int(input('Ingrese la operación que desea realizar (1: de soles a dólares, 2: de dólares a soles): '))
        if ope==1:
            if self.cta_mn>=monto:
                self.cta_mn=self.cta_mn-monto
                self.cta_usd=self.cta_usd+(monto*0.27)
                print('Felicidades {} {}, transferencia exitosa.'.format(self.nombre,self.apellido))
                print('Saldo en cuenta en soles: {}.'.format(self.cta_mn))
                print('Saldo en cuenta en dólares: {}.'.format(self.cta_usd))
            else:
                print('Lo sentimos, saldo insufiente en cuenta en soles.')
                print('Solo tiene {} soles.'.format(self.cta_mn))
        elif ope==2:
            if self.cta_usd>=monto:
                self.cta_usd=self.cta_usd-monto
                self.cta_mn=self.cta_mn+(monto*3.77)
                print('Felicidades {} {}, transferencia exitosa.'.format(self.nombre,self.apellido))
                print('Saldo en cuenta en soles: {}.'.format(self.cta_mn))
                print('Saldo en cuenta en dólares: {}.'.format(self.cta_usd))
            else:
                print('Lo sentimos {} {}, saldo insufiente en cuenta en dólares.'.format(self.nombre,self.apellido))
                print('Solo tiene {} dólares.'.format(self.cta_usd))
        else:
            print('La operación ingresada es inválida.')

    def retirar(self,monto):
        cuenta=int(input('Ingrese la cuenta de la que desea retirar (1 para soles, 2 para dólares): '))
        if cuenta==1:
            if self.cta_mn>=monto:
                self.cta_mn=self.cta_mn-monto
                print('Felicidades {} {}, operación exitosa.'.format(self.nombre,self.apellido))
                print('Saldo en cuenta en soles: {}.'.format(self.cta_mn))
                print('Saldo en cuenta en dólares: {}.'.format(self.cta_usd))
            else:
                print('Lo sentimos {} {}, saldo insufiente en cuenta en soles.'.format(self.nombre,self.apellido))
                print('Solo tiene {} soles.'.format(self.cta_mn))
        elif cuenta==2:
            if self.cta_usd>=monto:
                self.cta_usd=self.cta_usd-monto
                print('Felicidades {} {}, operación exitosa.'.format(self.nombre,self.apellido))
                print('Saldo en cuenta en soles: {}.'.format(self.cta_mn))
                print('Saldo en cuenta en dólares: {}.'.format(self.cta_usd))
            else:
                print('Lo sentimos {} {}, saldo insufiente en cuenta en dólares.'. format(self.nombre,self.apellido))
                print('Solo tiene {} dólares.'.format(self.cta_usd))
        else:
            print('La operación ingresada es inválida.')

cliente1=Billetera(4000,1200)
cliente1.transferir(500)
cliente1.retirar(1000)
cliente1.transferir(800)
cliente1.retirar(300)
cliente1.transferir(100)
cliente1.retirar(300)