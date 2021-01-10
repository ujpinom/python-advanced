import pandas as pd
import numpy as np
import re

############ Cleaning your data #############################################

codigos_postales=pd.Series({'Bostos':'02215','Miami':'1234'})
print(codigos_postales)
print(codigos_postales.str.match(r'\d{5}'))  # revisar si cada uno de los codigos ingresados tiene el numero de digitos apropiado, 5 para este caso
#Method match applies the regular expression \d{5} to each Series element,The method returns a new Series containing True for each valid element.
#Sometimes, rather than matching an entire value to a pattern, you’ll want to know whether a value contains a substring that matches the pattern. In this case, use method
#contains instead of match.

cities= pd.Series(['Boston, MA 02215', 'Miami, FL 33101'])
print(cities.str.contains('[A-Z]{2}'))

contacts= [['Mike Green', 'demo1@deitel.com', '5555555555'],['Sue Brown', 'demo2@deitel.com', '5555551234']]
contactsdf=pd.DataFrame(contacts,columns=['Nombre','Email','Cel'],index=['Persona1','Persona2'])
print(contactsdf)

def formato_numero_cel(numeros):
    resultado=re.fullmatch(r'(\d{3})(\d{3})(\d{4})',numeros)
    return '-'.join(resultado.groups()) if resultado else numeros

formato= contactsdf['Cel'].map(formato_numero_cel)
contactsdf['Cel']=formato
print(contactsdf)

