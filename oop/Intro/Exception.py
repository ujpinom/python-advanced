# Exception de prueba
from typing import  Union

class OnlyEven(list[int]):

    def ApendEven(self, number: int)-> None:

        if not isinstance(number,int):

            raise TypeError('Por favor ingrese solamente numeros enteros')

        if number % 2 != 0:

            raise ValueError('Solo numeros impares puedes ser agregados a la lista')


        super().append(number)


def error():

    print('Holaperro voy a lanzar un error')
    raise Exception('This is always raised')

def handler():

    try:

        print('Manejando la excepption')

        error()

    except Exception as ex:

        print(f'El error fue {ex}')

    print(5*8)

def funniest_division(divider: int) -> Union[str, float]:
    try:
        if divider == 13:
            raise ValueError("13 is an unlucky number")
        return 100 / divider
    except ZeroDivisionError:
        return "Enter a number other than zero"
    except TypeError:
        return "Enter a numerical value"
    except ValueError as e:
        print("No, No, not 13!")

    print('golaperro')

for val in (0, "hello", 50.0, 13):
    print(f"Testing {val!r}:", end=" ")
    print(funniest_division(val))