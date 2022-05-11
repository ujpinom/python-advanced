class OutStock(Exception):
    pass

class InvalidItem(Exception):
    pass


class ItemType():

    def __init__(self,name:str,cantidad:int)->None:

        self.name= name
        self.cantidad = cantidad



class Inventory():

    def __init__(self, items:list[ItemType]):

        pass

    def purchase(self,item_type:ItemType)->int:

        if item_type.name == 'Widget'.lower():

            raise OutStock(item_type)

        elif item_type.name == 'Carro'.lower():

            return 234
        else:

            raise InvalidItem(item_type)



it1 = ItemType('Carro'.lower(),2)
it2 = ItemType('perro'.lower(),4)

inve = Inventory([it1,it2])

item_compra = it2
try:

    cantidad=inve.purchase(item_compra)

except OutStock as ex:

    print(f'No hay inventario para el item: {item_compra.name}')

except InvalidItem as ex:

    print(f'El item {item_compra.name} no existe en el inventario')

else:

    print(f'La cantidad de elementos restantes para el item {item_compra.name} es {cantidad}')


perro=(1,4)
