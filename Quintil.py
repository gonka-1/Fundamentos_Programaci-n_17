"""Quintil: La tienda falabella necesita desarrollar un programa para saber cuantos puntos tiene acumulado cada usuario
por cada mil pesos que realice de compra un usuario recibe: (10 puntos) cuando un usuario alcanza los mil puntos es premiun, recibe un descuento del 25%
cuando un usuario alcanza 500 puntos está en el nivel oro por lo tanto recibe un descuento del 10%, para usuarios de 250 puntos es nivel bronce
no recibe descuento pero si varios premios (Audífonos, relojes y mucho más), perfiles de tres tarjetas:
Marcos tiene 1500 puntos a cambiar: que niveles le corresponde?
Jose Luis tiene 2500 puntos: que niveles le corresponde?
Sebastian solo tiene 300 puntos: que nivel le corresponde?
Mostrar en pantalla la información que corresponda al usuario y el descuento que recibe al final, el nivel,
un mensaje motivador para seguir utilizando los puntos"""



print ('\n===Bienvenido a Falabella===')

Nombre = input('\nIngrese su nombre:')

Premio = ['Audifonos','reloj','mochila']

Puntos = int (input('\nIngrese los puntos que tiene: '))

Monto_cancelado= int (input('\nIngrese su monto cancelado:'))

Puntos_agregados = (Monto_cancelado * 10) /1000 + Puntos

print (f'Sus puntos actuales son:{Puntos_agregados}')


if Puntos >= 1000:

    print ('\nEres integrante del del grupo premiun, felicidades!!!')
    print (f'Tienes un descuiento del 25% en tu proxima compra')

elif Puntos >= 500:

    print ('\nEres integrate del grupo oro, felicidades!!!')
    print (f'Tienes un descuento del 10% en tu proxima compra')

elif Puntos >= 250:
  print ('\nEres integrante del grupo bronce, felicidades!!!')
  for i, item in enumerate (Premio):
    print (i+1,'.',item)
  Premio_Canjeado = input('\nSelecciona el premio a canjear:')

  print ('Has seleccionado:', Premio_Canjeado,'!')

else:
   print ('\nNo cumples con los puntos requeridos, intentalo la proxima vez!')

print (f'\nGracias por visitarnos {Nombre}!, espero sigas utilizando tus puntos :) ')



