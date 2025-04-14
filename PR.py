Nombre= input ('Hola, dime tu nombre')

Edad = int (input('Cuantos años tienes '))

print ('Hola', Nombre, 'Tienes:', Edad)




print('Hola, mundo')


""""se utuliza para dejar comentarios
de varias lineas"""


"""variable01 = 12
variable02 = 12,3
variabletext= 'hola mundo'
variablelogic = True
variablelogic = False"""


#input se ultiliza para ingresar informacion 

#Nombre = input ("Diime tu nombre: ")
#Apellido = input ("Dime tu apellido: ")

#Suma

N1 = int(input('Dame un numero entero:'))
N2 = float(input('Dame un numero decimal:'))

#operacion_1

R1 = N1 + N2

print (f'El resultado final es:', {R1})

#Resta 

N3 = int(input('Dame un numero entero:'))
N4 = int(input('Dame un segundo numero entero:'))

#Operacion_2

R2 = N3 - N4

print (f'El resultado de la resta es:', {R2})

# Multiplicacion

N5 = int(input('Dame un numero entero:'))
N6 = int(input('dame un segundo numero entero:'))

#Operacion_3

R3 = N5*N6

print('El resultado de la multiplicacion es:', {R3})

#Division

N7 = float(input('Dame un numero dececimal:'))
N8 = float(input('Dame un segundo numero decimal:'))

#Operacion_4

R4 = N7 / N8 

print(f'El resultado de la division es:', {R4})

print('Felicidades completaste todas las operaciones!!!')


'''
Necesito ir a hacer la compra y se me ocurre hacer una lista en python
1. Como primer mensaje, deseo mostrarle al usuario un mensaje de bienvenida
2. Agregar los productos
3. Mostrar un mensaje al usuario de añade tus productos
4. Mostrar un mensaje al usuario si desea eliminar alguno de los productos
5. Al final, imprimir la lista
'''
print("Bienvenido a la lista de compras")

productos = []

print ("\nPor favor, añade tus productos. Escribe 'fin' cuando termines.")

while True:
    agregar = input("\nProducto: ")
    if agregar.lower() == "fin":
        break
    productos.append(agregar)

respuesta = input("Desea eliminar algun producto? (Si/No): ")

if respuesta.lower() == "si":
    print("Que producto desea eliminar? Escribe 'fin' para finalizar: ")
    while True:
        eliminar = input("Eliminar: ")
        if eliminar.lower() == "fin":
            break
        if eliminar in productos:
            productos.remove(eliminar)
            print(f'{eliminar} ha sido eliminado.')
        else:
            print(f'{eliminar} no está en la lista')

print("Tu lista final de productos:")
print(productos)


Actividad programación:

"""Una tienda de perfume llamda Glory el representante de venta de la tienda de perfume necesita organizar
el formulario de venta y el piensa que representando el siguiente formulario podria mejorar sus ventas:
ya que el formulario que tiene actualmente tiene 10 items, campos que desea implementar: Número de boleta,
Número de identificación, Nombre del cliente y productos del pedido.
Productos del inventario: 
-Perfume organza para dama 
-Katy Perry
-Mañana fresca para dama
-La mejor noche para dama
-Sueño exclusivo para dama
-Ahora si voy para caballero
-Antonio Bandera
-Lacoste 
-A que te quito el sueño para caballero 
colocarle precio: 
50ml 10mil 
100ml 18mil 
Añadir todo el pedido, todo el subtotal mas el iva(19%)."""
