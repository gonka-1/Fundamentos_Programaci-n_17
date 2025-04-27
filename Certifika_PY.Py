
"""Certifika: Esta empresa necesita desarrolladores, solicita realizar un programa que cumpla con las siguientes condiciones:
-alumnos con calificaciones mayor a 6 recibiran un descuento en su matricula del 20%
-alumnos con calificacion mayor a 5 tendran un descuento del 15%
-alumnos con calificacion mayor a 4 tendran un descuanto del 10%
-Los que no cumplen con los requisitos invitamos a seguir esforzandose"""


print ('===Bienvenido a Certifika===')

Nombre_Apellido = input('\nIngrese su Nombre y Apellido: ')
Identificacion = input ('\nIngresa tu identificación: ')

print(('Bienvenid@, '), Nombre_Apellido, ('!!'))

while True:
 
 Nota_1 =float (input('\nIngresa tu primera nota: '))
 Nota_2 =float (input('\nIngresa tu segunda nota: '))
 Nota_3 =float (input('\ningresa tu tercera nota: '))
 
 if any(n < 1 or n > 7 for n in [Nota_1, Nota_2, Nota_3]):
  print('\nUna o más notas son inválidas. Ingresa todas nuevamente.\n')
  continue

 print ('Perfecto!!, en breve calcularemos tu promedio:')
 break

print
Promedio = (Nota_1 + Nota_2 + Nota_3)/ 3
 
print (f'Tu promedio final es de: {Promedio:.1f}')

if Promedio >= 6:
    print ('\nFelicidades, recibiste un descuento en tu matricula del 20%')
elif Promedio >= 5:
     print ('\nFelicidades, recibiste un descuento en tu matricula del 15%')
elif Promedio >= 4: 
     print ('\nFelicidades, recibiste un descuento en tu matricula del 10%')
else:
   print('\nPuedes esforzarte mas la proxima vez, mucho animo', Nombre_Apellido,'!!')





