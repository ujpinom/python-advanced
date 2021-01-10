from decimal import Decimal
from Account import Account
from timewithproperties import Time
from deck import  DeckOfCards
from comissionEmployeee import EmpleadoPorComision
from empleadoAsalariado import Empleado_Asalariado

empleando1= EmpleadoPorComision('Uriel','Pino','12345567',123456.45,0.8)
print(empleando1.ganancias())
empleando1.tasa_comision=0.2
print(empleando1.primer_nombre);print(empleando1.ganancias())
print(
    empleando1
)

empleando1.ventas_totales=2000000;print(f'{empleando1.ganancias():,.2f}')

empleado2=Empleado_Asalariado('Uriel','Pino','12345567',123456.45,0.8,20000);print(empleado2)
print(f'{empleado2.ganancias():,.2f}')
empleado2.ventas_totales=Decimal('10000.0');empleado2.tasa_comision=Decimal('0.05');empleado2.salario_base=Decimal('1000')
print(f'{empleado2.ganancias():,.2f}')