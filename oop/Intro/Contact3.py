

class ContactList(list['Contact']):

    def search(self,nombre:str)->list['Contact']:


        coincidencias: list['Contact'] = []

        for contact in self:

            if nombre in contact.nombre:

                coincidencias.append(contact)

        return coincidencias




class Contact():

    all_contacts = ContactList()

    def __init__(self,nombre:str='',email:str='', **kwargs)->None:

        self.nombre = nombre
        self.email= email

        super().__init__(**kwargs)

        Contact.all_contacts.append(self)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"{self.nombre!r}, {self.email!r}" f")"
        )

class AddresHolder():

    def __init__(self,street:str='', state: str='', code: str='',**kwargs)-> None:

        super().__init__(**kwargs)
        self.street = street
        self.state = state
        self.code = code


class Friend(AddresHolder, Contact):

    def __init__(self,tel:str='',**kwargs):

        '''
         Recibe todos los argumentos  necesarios para la construccion del objecto tipo Friend

        :param tel: Telefono de nustro amigo
        :param kwargs: Adicional argumentos para la super clase los parametros deben ser los siguientes
        

        '''

        super().__init__(**kwargs)

        self.tel= tel

    def __repr__(self):

        return (f'{super(Friend, self).__repr__()} + Tel:{self.tel}')



c1 = Contact("John A", "johna@example.net")
c2 = Contact("John B", "johnb@sloop.net")
c3 = Contact("Jenna C", "cutty@sark.io")

f = Friend(tel='134234324',street='sdfsd',state='asdasd',code='asasdasd',nombre='Uriel',email='holaperro@unal.edu.co')

print([nombre for nombre in Contact.all_contacts.search('John')])

print(f)

print(Friend.__mro__)
print(f.code)