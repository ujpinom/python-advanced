from typing import List


class Contact():

    all_contacts: List["Contact"] = []

    def __init__(self,nombre: str,email: str):

        self.nombre = nombre
        self.email = email

        Contact.all_contacts.append(self)

    def __repr__(self)->str:
             return (f"ClassName: {self.__class__.__name__}  Nombre:{self.nombre}  Email:{self.email}")



class Supplier(Contact):

    def ventas(self, venta:"Order")->None:

        print(f'La venta fue pendida al contacto supplier {self.nombre}')



c_1 = Contact("Dusty", "dusty@example.com")
c_2 = Contact("Steve", "steve@itmaybeahack.com")
c = Contact("Some Body", "somebody@example.net")
s = Supplier("Sup Plier", "supplier@example.net")
print(Contact.all_contacts)

print(s.ventas('Holaperro'))