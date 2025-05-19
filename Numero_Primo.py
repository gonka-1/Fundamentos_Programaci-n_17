Numero = [5, 6, 7]

Numero_primo = 0
Numero_no_primo = 0

def es_primo (n):
    if n <= 1:
        return False
    for i in range (2, int(n/2), +1):
        if n% i == 0:
            return False
    return True

for i, numero in enumerate (Numero):
  print (f'{1+i}. numero: {numero}', end='->')
if es_primo(numero):
      print('es primo')
      Numero_primo += 1
else:
      print('No es primo')
      Numero_no_primo += 1
print ('\nResultado: ')
print (f'Se ingresa {Numero_primo} Numero primo')
print (f'Ingresa numero {Numero_no_primo} Numero {'s' if Numero_no_primo > 1 else ''} No primo')


"""Registrar la temperatura en un rango de 50 a -50 C: dado que el ususario pueda ingresar cualquier dato (incluso cadena de texto), se puede usar manejo de excepcion
para evitar que el progama se detenga:
1.Si el dato ingresado no es numero entero el program debe mostar: 
Error: DEBE INGRESAR UN NUMERO ENTERO VALIDO y repetir hasta que sea valido.
2.Si el ususario muestra un numero entero fuera del rango informar al usuario:
ERROR: RANGO INVALIDO DEBE SER UN NUMERO DENTRO DEL RANGO(50, -50 C) 
3. si el ususario ingresa los datos correctamente: temperatur registrada exitosamente.
Debe de haber una opcion para salir del programa y lanzar un mensaje que diga:
CIERRE DEL PROGRAMA, HASTA LUEGO."""
