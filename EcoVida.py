 
Nombre = input('\nIngrese su nombre: ').capitalize()
Tipo_cliente = input('\nIngrese su tipo de cliente (Normal / Premiun / Frecuente / Empresarial / Adulto Mayor):').capitalize()
monto_compra =int(input('\nIngrese su monto de compra sin puntos:$'))
metodo_pago = input('\ningrese su metodo de pago(Efectivo / Débito / Crédito):').capitalize()

descuento = 0
recargo = 0

if Tipo_cliente == 'Normal' and monto_compra > 100000:
    descuento += 0.05
elif Tipo_cliente == 'Frecuente' and monto_compra > 80000:
    descuento += 0.10
elif Tipo_cliente == 'Premiun' and monto_compra > 50000:
    descuento += 0.15
elif Tipo_cliente == 'Empresarial' and monto_compra > 200000:
    descuento += 0.20
elif Tipo_cliente == 'Adulto Mayor' and monto_compra > 30000:
    descuento += 0.08
elif metodo_pago == 'Efectivo' and monto_compra > 50000:
    descuento += 0.03
elif metodo_pago == 'Credito' and monto_compra < 20000:
    recargo += 0.05


if Nombre.find('a') != -1 or Nombre.find('e') != -1 or Nombre.find('o') != -1:
    descuento += 0.02
    print ('\nFelicidades, obtuviste un descuento por tu nombre!!!')

import random

Numero_suerte = random.randint (1 , 10)

print ('\nTu número de la suerte es:', Numero_suerte)

if Numero_suerte in [7 , 9]:
    descuento += 0.05
elif Numero_suerte in [1 , 2]:
    recargo += 0.03
elif Numero_suerte == 5:
    print ('Felicidades, has ganando un cupón!!!')

Total_pago = monto_compra * (1 - descuento + recargo)

#Resumen de compra:

print ('\n===SU RESUMEN ES===')

print('Nombre:', Nombre)
print ('Tipo de cliente:', Tipo_cliente)
print ('Monto a pagar:', monto_compra)
print ('Metodo de pago:', metodo_pago)
print (f'Descuento: {round(int(descuento*100))}%')
print (f'recargo: {round(int(recargo*100))}%')
print (f'Total final: $ {int(round(Total_pago))}')








