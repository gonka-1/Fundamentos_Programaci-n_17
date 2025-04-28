"""que permita generar un numero aleatorio dentro de un rango definido por el ususario y ajustarlo dividiendo entre 4, luego el ususario tiene que dar un numero para poder 
dividirlo nuevamente 
en un maximo de tres intentos
condiciones:
-ingreso de datos
Letra a: el usuario ingresa 2 numeros enteros que representan el rango numerico
b: el primer numero tiene que ser menor al segundo
-generacion del numero aleatorio
a: si elige un numero aleatorio dentro del rango ingresado
b: el numero se ajusta dividiendo entre 4 y redondeandolo al multiplo de 4 mas cercano
-Del usuario:
a: primer intento: si el usuario acierta se muestra el mensaje de felicidades adivinaste al primer intento 
b: segundo intento: si el usuario no acierta se indicara si el numero es mayor o menor 
c: tercer intento: sino acierta se le devuelve a dar una pista 
d: resultado final
sino acierta en los 3 intentos el programa da un mensaje de 'game over' el numero es incorrecto"""


print ('===Bienvenido a adivina el numero===')

import random as rd

rango_inferior = int(input('\ndame tu limite inferior: '))
rango_superior = int(input('\ndame tu rango superior:' ))

resultado_adivinar = rd.randint(rango_inferior,rango_superior)
intentos = 2


while intentos >=0:
    intento = int(input('\ningresa un numero: '))
    intentos -= 1 
    if intento == resultado_adivinar:
      print ('Felicidades, adivinste!!!')
      break
    if intento < resultado_adivinar:
     print('muy bajo')
    elif intento > resultado_adivinar:
     print('muy alto')
else:
 print ('\nTenias solo 3 intentos, suerte la proxima vez')
 
if intento == resultado_adivinar:
  print('\nSe ajustara su numero adivinado dividiendo en 4: ')
  Resultado_final = round(intento / resultado_adivinar, 4)
  print (f'\nEste es tu resultado final:{Resultado_final}')

 



