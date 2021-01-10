import re
#####################################33Function fullmatch####################################
#fullmatch() revisa si la expresión en el primer argumento esta contenida en la expresión del segundo argumento;

pattern='02215'
if re.fullmatch(pattern,'0221545,-34'):
    print('MATCH')
else:
    print('NO MATCH')

#metacharacters [] {} () \ * + ^ $ ? . |

print('MATCH') if re.fullmatch(r'\d{5}','34567') else print( 'Invalid')
#Custom Character Classes
print('matches') if re.fullmatch('[A-Z][a-z]*','Uriel') else print('Invalido') #Sirve para validar si el string ingresado es un nombre. Valida si el primer caracter es mayuscula.
# El operador * matches cero o mas ocurrencias de la sub-expresión  a su izquierda. Es decir un numero indefinido de letras minusculas, ya que los nombres no tienen una longitud definida.


print('MAtch') if re.fullmatch('[*+%$]*','*****') else print('no peroo');
print('MAtch') if re.fullmatch('[*+%$]*','?') else print('no peroo')
#########################33 * vs. + Quantifier#############################
#Si requiere que despues de la primera letra mayuscula del nombre exista almenos alguna otra ocurrencia entonces se debe reemplazar el operador * por el operador +

print('Nombre valido') if re.fullmatch('[A-Z][a-z]+','E') else print('El nombre no es valido.')
print('Nombre valido') if re.fullmatch('[A-Z][a-z]+','Elena') else print('El nombre no es valido.')
##33####You can match at least n occurrences of a subexpression with the {n,} quantifier.
print('YEAH!') if re.fullmatch(r'\d{3,}','123456') else print('NO!') #Busca al menos la ocurrencia de tres digitos
print('YEAH!') if re.fullmatch(r'\d{3,}','12') else print('NO!') #A las expresiones anteriores se les puede también fijar un limite superior
print('OH YEAH') if re.fullmatch(r'\d{3,8}','12345678') else print('NEl perro') #numeros mínimo con 3 hasta 8 digitos máximo
print('OH YEAH') if re.fullmatch(r'\d{3,8}','1234567889') else print('NEl perro') #numeros mínimo con 3 hasta 8 digitos máximo

#################################################################Function sub—Replacing Patterns#####################################
#Let’s convert a tab-delimited string to comma-delimited:
print(re.sub(r'\t',',','1\t2\t3\t4'))
################ Function split####################################################
saludo='Hola gonorrea! Espero que este bien en este fin de semana. Espero que todas las cosas buenas que deseas se       hagan una hermosa realidad!'
print(re.split(r'!\s*',saludo))

#####################3Function search—Finding the First Match Anywhere in a String#######################
###Function search looks in a string for the first occurrence of a substring that matches a regular expression and returns a match object (of type SRE_Match) that contains the matching
#substring. The match object’s group method returns that substring:
##Ignoring Case with the Optional flags Keyword Argument Many re module functions receive an optional flags keyword argument that changes how regular expressions are matched. For example, matches are case sensitive by default, but by
#using the re module’s IGNORECASE constant, you can perform a case-insensitive search:
resultado= re.search('hola','Perro HOLA',flags=re.IGNORECASE)
print(resultado.group()) if resultado else print('Nel perro')

################################### Capturing Substrings in a Match#################################################
#You can use parentheses metacharacters—( and )—to capture substrings in a match. For example, let’s capture as separate substrings the name and e-mail address in the string text:

text = 'Charlie Cyan, e-mail: demo1@deitel.com'

pattern2=r'([A-Z][a-z]+ [A-Z][a-z]+), e-mail: (\w+@\w+\.\w{2,})'
result= re.search(pattern2,text)
print(result.groups())