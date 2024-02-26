#1.Leer un numero entero y determinar si es un numero terminado en 4

n1 = int(input('Ingrese un número entero: '))
if n1 % 10 == 4 :
    print('El número termina en 4')
else :
    print('El número no termina en 4')
