""""lista de supermercado:
El dia de hoy necesito hacer compras y necesito hacer una lista, primer mensaje un mensaje de bienvenida, agregar 2 productos,
mostrar un mensaje a tu usuario de añade tu producto, solicitar al usuario modificar uno de los productos. al final hacer una lista de la compra resumida"""


Nombre = input('Hola, como te llamas:')

print('Bienvenido,', Nombre, ('!, Que deseas llevar?'))

list = []
list.append('Mandarina')
list.append('Naranja')

print('Hola!!, quiero llevar:', list)
 
print('Hoy no tenemos: mandarina')

list.remove('Mandarina')

print('Hmm que mal, entonces llevaré otra cosa')

Nuevo_Producto = (input('Que desea llevar?:'))

list.append(Nuevo_Producto)

print ('Quiero llevar entonces', list)

print ('Entonces tu resumen es:', list,('Gracias por su compra!!'))

