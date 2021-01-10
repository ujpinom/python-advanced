from decimal import Decimal

class Account:
    """Información bancaria de una persona"""
    def __init__(self,nombre,saldo):
        if saldo < Decimal('0.0'):
            raise ValueError('El saldo debe ser positivo')
        self.nombre=nombre
        self.saldo=saldo

    def deposito(self,cantidad):
        """Deposita una cantidad de dinero a la cuenta"""
        if cantidad<Decimal('0.00'):
            raise ValueError('El deposito debe ser  una cantidad positiva')
        self.saldo+=cantidad
        return self.saldo