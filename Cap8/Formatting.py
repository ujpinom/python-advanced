import numpy as np

print(f'{12.34545:.2f}');print(f'{10}{12:>20d}');
print(f'{"Hola perro":^34}')##Centrar el mensaje
#Sometimes it’s desirable to force the sign on a positive number:
print(f'{10:+15d}')
#You can format numbers with thousands separators by using a comma (,), as follows:
print(f'{123455678:,}')#divide los miles con comas

#+++++++++++++++++++++++++++++++++++++++++Concatenating and Repeating Strings+++++++++++++++++++++++++++++++
s1='Hola perro';s2=' Que honda gonorrea'
s1+=' '+ s2;print(s1)
print(s1+s2)
sentence = '\t\t\t \n This is a test string. \t\t\n';print(sentence);print('hola')
saf=list(('vaca','Agua'));print(saf)
sfdsfs=np.array(saf);
sfdsfs.sort();print(sfdsfs)

print('Orange'=='orange')
##########################################################333Searching for Substrings
'''Counting Occurrences
String method count returns the number of times its argument occurs in the string on
which the method is called:'''
horacion='Hola perro gonorrea Que las coas sean mejor de lo que habiamos dicho';print(horacion.lower().count('que'))