"""numeros= [19,3,5,7,15]
print(f'Index{"Value":>8}   Bar')
for index,value in enumerate(numeros):
    print(f'{index} {value:>8}       {"*"*value}')"""

lista=[2, 3, 5, 7, 11, 13, 17, 19]
list1= lista[::-1] #Crea una nueva lista recorriendo la original al revés
list2=lista[-1:(-1)*len(lista)-1:-1]
list3=['perro','gato','marrano']
list3.pop()
lista[0:0]=list3   #Asigna los elementos de list3 a los tres primeros elementos de la list1 dejando el resto de elementos sin modificar
print(lista,list1,list2,sep='  ')
numeros= list(range(0,10))
numeros.sort(reverse=True)
del numeros[3] #Borra el elemento ubicado en el index 3 de numeros
#La función del tambien sirve para borrar variables, asi como borrar todos los elementos de una lista(no solo un elemento)
x=numeros.index(3) # retorna el index donde se encuntra ubicado el argumento. devuelve error si dicho numero no se encuentra
print(x)
print()
if(6 in numeros): #Verifica si 6 es contenido por numeros
    print('Claro que si gonorre')
else:
    print('no gonorrea')

print(numeros)

#El metodo insert(index,elemento) inserta el elemento indicado en la posición indicada
#El metodo extend inserta los elementos de una secuencia al final de la lista especificada
numeros.insert(0,1200) ;print(numeros);print()
numeros.extend(('perro','gonorrea'));print(numeros) #este método es equivalente a lista+=secuencia
numeros+=('perro','gonorrea');print(numeros)
#El metodo removes remueve la primera ocurrencia del elementos especificado. Un error ocurre si el elemento no se encuntra contenido en la lista
#El mmetodo clear también borra todos los elementos de una lista
#El metodo count busca por el argumento en la lista y devuelve el numero de veces que este se repite dentro de la lista

respuestas=[1, 2, 5, 4, 3, 5, 2, 1, 3, 3,1, 4, 3, 3, 3, 2, 3, 3, 2, 2]
minimo=min(respuestas);maximo=max(respuestas)

for i in range(minimo,maximo+1):
    print(f'{i} se repite {respuestas.count(i)} veces')



list4=[i for i in range(1,11) if i%2==0]
print(list4)

lista2= ['perro','vaca','marrano']

lista5=[item.upper() for item in lista2]
print(lista5)

#------------------------------------Filter,map and reduce------------------------------------------

num=[i for i in range(1,11)] #equivalente a list(range(1,11))
numm2= list(range(1,11))
def main():


    numeros_impares=list(filter(find_odd,numm2))
    numeros_impares3=list(filter(lambda x:x%2!=0,num))
    numeros_impares2=[i for i in num if find_odd(i)]
    print('Lista obtenida haciendo uso del metodo filter y funcion comun',numeros_impares)
    print('lista obtenidad por list comprehension',numeros_impares2)
    print('lista obtenidad usando funciones lambda', numeros_impares3)



def find_odd(x):
    return x%2!=0

main()

a = [[77, 68, 86, 73], [96, 87, 89, 81], [70, 90, 86, 81]]

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end=' ')
    print()

