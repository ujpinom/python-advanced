print(23.4)
print(5 * 4)
print(4+5)

print('She said "Hello" to everyone')
z='perro'
k='4'
m=print(len(z)) #imprime la longitud de un string, es decir su dimensión.
print(k+z) #el simbolo + concatena las variables k y z
print(z[1])  # sirve para buscar cual es el elemento que ocupa la posición 1 dentro  de la varible z. se empieza desde cero
my_strin='hola mundo'
print(my_strin[1:]) # muestra los elementos desde la posición 2 hasta el final del string
print(my_strin[2:7])
print(len(my_strin))
print('Hi'*10)
title='el perro, la vaca, el caballo'
print('los animales son: ',title)
print(title.split(',')) # separa el contenido de la variable por comas
print(title.split(' ')) # separa el contenido de la variable por espacios
print(title.count('a')) # el metodo count() sirve para determinar cuantos strings hay dentro de otro. En este caso cuentas "a" hay en el string
print(title.replace("el perro","panochon")) # reemplaza un string dentro de un string por otro string. Se reemplaza el string "el perro" por "panochon"
print(my_strin.replace("hola","adios"))
ff='Edward Alun Rawlings'
print(ff.find('Alun')) # la función find() revisa si hay un string se encuentra dentro de otro. Si lo esta arroja la posición de su primer elemento de
# de lo contrario arroja -1 inicando que dicho elemento no forma parte del string
print('Edward John Rawlings'.find('Alun'))
print('perro'=='pegr') # "==" pregunta si es igual. "!=" pregunta si es diferente
print('perro'!='pegr')
#some_string.lower().startswith('h') # convierte el string en minuscula y luego ejecuta la operación startswith('h'). Esto es para eliminar la
#sensibilidad a las letras mayusculas y minuscula del programa.
format_string='hello {}'
print(format_string.format('uriel'))
nombre='uriel'
edad= 20
profesion='ing_electrisista'
print('Su nombre es {}, tiene {} de edad y es {}'.format(nombre,edad,profesion)) #el metodo format() llena los contenedores con la información especificada den el método.
entrance='buenos días {0}, usted tiene un {2} % de descuento. Valido hasta el dia {1} de {3}'
print(entrance.format('perra',25,20,'junio'))


print('|{:<25}|'.format('left aligned')) # The default
print('|{:>25}|'.format('right aligned'))
print('|{:^25}|'.format('centered'))
print('{:^95}'.format('Información del consumidor'))
profesion2='su nombre es {nombre},uste tiene un {descuento}% de descuento.Valido hasta el día {dia} de {mes}'
print(profesion2.format(nombre='ana',descuento=25,dia=2,mes='julio'))
import string
# Initialise the template with ¢variables that
# will be substitute with actual values
template = string.Template('$artist sang $song in $year')
print(template.substitute(artist='Freddie Mercury', song='The Great Pretender', year=1987))
edadd=input('cual es su edad:')
print('su edad es de:',edadd,'años')