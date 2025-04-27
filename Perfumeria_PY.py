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


# Lista de productos
productos_dama = ["Perfume Organza para dama", "Katy Perry", "Mañana fresca para dama", "La mejor noche para dama", "Sueño exclusivo para dama"] 
productos_caballero = ["Ahora sí voy para caballero", "Antonio Bandera", "Lacoste", "A que te quito el sueño para caballero"]

# Precios
precios_50ml = 10000
precios_100ml = 18000

# Captura de datos del cliente
print("===== Bienvenido a Perfumería Glory =====")
boleta = input("Ingrese el número de boleta: ")
identificacion = input("Ingrese el número de identificación: ")
nombre = input("Ingrese el nombre del cliente: ")

pedido = []
subtotal = 0

while True:
    genero = input("\n¿Desea perfume de dama o caballero? (escriba 'fin' para terminar): ").lower()
    
    if genero == 'fin':
        break

    if genero == 'dama':
        productos = productos_dama
    elif genero == 'caballero':
        productos = productos_caballero
    else:
        print("Opción inválida. Escriba 'dama', 'caballero' o 'fin'.")
        continue

    print("\nEstos son los perfumes disponibles:")
    for i, producto in enumerate(productos):
        print(f"{i+1}. {producto}")

    while True:
        seleccion = input("Seleccione el número del perfume o escriba 'fin' para cambiar de categoría: ")
        if seleccion.lower() == 'fin':
            break

        try:
            indice = int(seleccion) - 1
            if indice < 0 or indice >= len(productos):
                print("Número inválido. Intente de nuevo.")
                continue

            producto_seleccionado = productos[indice]

            tamaño = input("¿Qué formato desea llevar? (50ml/100ml): ")
            if tamaño == "50ml":
                precio = precios_50ml
            elif tamaño == "100ml":
                precio = precios_100ml
            else:
                print("Tamaño inválido. Intente de nuevo.")
                continue

            cantidad = int(input("¿Cuántas unidades desea llevar?: "))
            total = precio * cantidad
            subtotal += total

            pedido.append((producto_seleccionado, tamaño, cantidad, total))
            print(f"Producto añadido: {producto_seleccionado} ({tamaño}) x{cantidad} - ${total:,}")

        except ValueError:
            print("Entrada inválida. Ingrese un número.")

 # Calcular IVA y mostrar factura
iva = subtotal * 0.19
total_final = subtotal + iva

print("\n===== Factura =====")
print(f"Número de boleta: {boleta}")
print(f"Identificación: {identificacion}")
print(f"Nombre del cliente: {nombre}\n")
print("Detalle del pedido:")

for item in pedido:
    print(f"- {item[0]} ({item[1]}) x{item[2]} = ${item[3]:,}")

print(f"\nSubtotal: ${subtotal:,}")
print(f"IVA (19%): ${iva:,.2f}")
print(f"Total a pagar: ${total_final:,.2f}")

