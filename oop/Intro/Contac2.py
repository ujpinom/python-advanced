

class ContactList(list['Contact']):

    def search(self,nombre:str)->list['Contact']:


        coincidencias: list['Contact'] = []

        for contact in self:

            if nombre in contact.nombre:

                coincidencias.append(contact)

        return coincidencias




class Contact():

    all_contacts = ContactList()

    def __init__(self,nombre:str,email:str)->None:

        self.nombre = nombre
        self.email= email

        Contact.all_contacts.append(self)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"{self.nombre!r}, {self.email!r}" f")"
        )

class AddresHolder():

    def __init__(self, street:str, state: str, code: str)-> None:

        self.street = street
        self.state = state
        self.code = code


class Friend(AddresHolder, Contact):

    def __init__(self,nombre:str,email:str,tel:str,street: str,state: str, code:str):

        Contact.__init__(self,nombre,email)

        AddresHolder.__init__(self,street,state,code)

        self.tel= tel

    def __repr__(self):

        return (f'{super(Friend, self).__repr__()} + Tel:{self.tel}')



c1 = Contact("John A", "johna@example.net")
c2 = Contact("John B", "johnb@sloop.net")
c3 = Contact("Jenna C", "cutty@sark.io")
f = Friend("Dusty", "Dusty@private.com", "555-1212",'perro','gayo','123')

print([nombre for nombre in Contact.all_contacts.search('John')])

print(f)

print(Friend.__mro__)