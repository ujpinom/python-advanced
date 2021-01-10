import numpy as np

'''numeros=np.array(list(range(1,11)))  #El arreglo es del tipo ndarray
num1=list(range(1,11))
num2=list(range(5,15))

numeros_multi= np.array([num1,num2]) #para crear matrices las dilas deben tener las mismas dimensiones
print(numeros)
print(numeros_multi)
print(numeros_multi.shape)  ##Retorna un tupla indicando en la primera posición el numero de filas y la segunda especificando el numero de columnas (2,3)
print(numeros_multi.size)#retorna el númeto total de elementos que estan contenidos en el arreglo
print(numeros_multi.itemsize)

############################## iterando a traves de arreglo-------------------
#---------------------estilo de iteración usado para visualziar los elementos del arreglo sin modificarlos
for fila in numeros_multi:
    for columna in fila:
        print(columna,end=' ')
    print()
#-------------------estilo de iteración para visualizar o modificar los elementos del arreglo
for i in range(numeros_multi.ndim):
    for j in range(len(numeros_multi[i])):
        if(i==j):
            numeros_multi[i][j]=0
        print(numeros_multi[i][j],end=' ')

    print()

#------------------------------llenar arreglos con valores especificados---------------------------------------------------------------------
print(np.zeros(5)) #Crea un arreglo unidimensional con el numero de ceros indicados(5 en este caso)
print(np.ones((5,5),dtype=float)) #Crea un arreglo lleno de unos. el primer argumento indica las dimensiones del arreglo, mientras que el segundo el tipo de dato. por defecto es float
print(np.full((5,5),10)) # crea un arreglo de dimension especificado rellenado con el elemento especificado

#------------------------------------Creating arrays from Ranges-----------------------------------------
num3=np.arange(10) #Similar a range()
print(num3)
print(np.linspace(0.0,1.0)) #la funcion linspace() crea un arreglo de elementos igualmente espaciados entre los limites especificados. Por defecto crea 50 elementos, pero este parametro
#se puede modificar igresando el tercer argumento num=x;'''

num1= np.array([[1,2],[6,3]])
num2=np.array([[4,5],[2,3]])
list1=[1,2,3,4,5]
list2=[23,45,6]
print(num1*num2) #multplica elemento por elemento
print(num1[0,1])
list1+=list2
print(list1)
#existe varias operaciaone que se pueden realizar sobre arreglos de numpy tales como sum,min,max,mean,std,var....
print(num1.sum(),num1.min(),num1.max(),num1.mean(),num1.std(),num1.var())


print(num1[:,0])
grades=np.array([[87, 96, 70], [100, 87, 90],[94, 77, 90]])
grades2=np.array([[87, 96, 70], [100, 87, 90],[947, 77, 90]])
print(grades
      )
print(grades[1:3,1:3])

# El metodo flatten() crea una nueva copia unidimensional de un arreglo multidimensional (deep copy)
flattened= grades.flatten()
print(flattened)

#el metodo ravel() crea una nueva copia unidimensional de un arreglo multidimensional (view_copy)

print(grades.T)#traspuesta de un arreglo
conca= np.hstack((grades,grades2))
fsfs=conca[:,0:4].copy();print(
      fsfs
)
print(conca);print(conca[:,0:4])




