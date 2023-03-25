#Pregunta 1
#Maria Cristina Orihuela Flores

#Se importa la funcion random
import random

#Definimos una funcion
def cadenaADN (long):
    base=['A', 'C', 'G', 'T']
    lista_cadena=[]
    for i in range(0, long):
        base_random=random.choice(base)
        lista_cadena.append(base_random)
    lista_cadena_final= " ".join(lista_cadena)
    return lista_cadena_final

#Solicitamos el dato de entrada
long=int(input("Enter the string length [20, 1000]: "))
#Validamos la longitud
if long>=20 and long<=1000:
    cadena_finalADN=cadenaADN(long)
    print("The DNA string is: ", cadena_finalADN)
else:
    print("¡ERROR!, the size must be between 20 and 1000")
