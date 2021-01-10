from decimal import Decimal
from comissionEmployeee import EmpleadoPorComision

class Empleado_Asalariado(EmpleadoPorComision):

    def __init__(self,primer_nombre,primer_apellido,seguro,ventas_totales,tasa_comision,salario_base):
        super().__init__(primer_nombre,primer_apellido,seguro,ventas_totales,tasa_comision)
        self.salario_base=salario_base

    @property
    def salario_base (self):
        return self._salario_base

    @salario_base.setter
    def salario_base(self,salario_base):
        if(salario_base<Decimal('0.0')):
            raise ValueError('El salario base debe ser mayor que cero')
        self._salario_base=salario_base

    def ganancias(self):
        return super().ganancias()+self.salario_base

    def __repr__(self):
        return (super().__repr__()+f'\nSalario Base: {self.salario_base:,.2f}')

