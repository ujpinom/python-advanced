from decimal import Decimal

class EmpleadoPorComision:

    def __init__(self,primer_nombre,primer_apellido,seguro,ventas_totales,tasa_comision):
        self._primer_nombre=primer_nombre
        self._primer_apellido=primer_apellido
        self._seguro=seguro
        self.ventas_totales=ventas_totales
        self.tasa_comision=tasa_comision

    @property
    def primer_nombre(self):
        return  self._primer_nombre

    @property
    def primer_apellido(self):
        return self._primer_apellido
    @property
    def seguro(self):
        return self._seguro
    @property
    def ventas_totales(self):
        return self._ventas_totales

    @ventas_totales.setter
    def ventas_totales(self,ventas):
        if(ventas<Decimal('0.0')):
            raise ValueError('Las ventas deben ser positivas')
        self._ventas_totales=ventas

    @property
    def tasa_comision(self):
        return self._tasa_comision

    @tasa_comision.setter
    def tasa_comision(self,tasa):
        if not (Decimal('0.0')<tasa<Decimal('1.0')):
            raise ValueError('La tasa debe ser mayor que 0 y menor que 1.')
        self._tasa_comision=tasa

    def ganancias(self):
        return self._ventas_totales*self._tasa_comision

    def __repr__(self):
        return (f'EmpleadoPorComision({self._primer_nombre}{self._primer_apellido}\nSeguro: {self._seguro}\nVentas Totales: {self._ventas_totales:,.2f}\nTasa: {self._tasa_comision})')

