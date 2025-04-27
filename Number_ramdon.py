

"""programa que solicite 2 numeros a un usuario a: limite inferior, b: limite superior, adivinar un numero aleatorio (azar) al mismo numero realizar un porcentaje, 
pregumtandole al usuario que le saque el porcentaje deseado(agregar o quitar) al resultado y luego finalizar con resultado_final."""

nombre = input ('Dame tu nombre: ')

print ('\n===Bienvenido,', nombre,'===')
    
A = int (input('\nDame tu limite inferior: '))
B = int (input('\nDame tu limite superior:'))

import random 

resultado = random.randint(A,B)

print (f'\nTu Numero es: {resultado}')

Porcentaje = float(input('\nDame el porcentaje que deseas aplicar:'))

while True:
 accion = input('\nDeseas agregar o quitar el porcentaje agregado?:')

 if accion == 'agregar':
    Resultado_final = resultado + (resultado * Porcentaje)
    break
 elif accion == 'quitar':
    Resultado_final = resultado + (resultado * Porcentaje)
    break
 else: 
    print ('opción invalida, vuelva a intentar')  
    continue
 
print (f'Resutaldo Final es: {Resultado_final}')