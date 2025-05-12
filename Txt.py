"""with open ("datos.txt", "w") as archivo:
    archivo.write('Nombre: Mario')
    archivo.write('\nEdad: 25')
    archivo.write('\ncarrera: ing.' )   """

try:
    archivo = open('datos.txt', 'r')
    contenido = archivo.read()
except FileExistsError as error:
    print('Te equivocaste :c')
else: 
    print('Correcto')
finally:
    print ('Lo lograste')
