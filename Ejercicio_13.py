#14. Leer dos números enteros de dos dígitos y determinar a cuánto es igual la suma de todos los dígitos.

n1 = int(input('Ingrese un número de dos digitos '))
n2 = int(input('Ingrese otro número de dos digitos '))
d1 = n1//10
d2 = n1%10
s1 = n2//10
s2 = n2%10
if n1 > 9 and n1 < 100 and n2 > 9 and n2 < 100:
    sum = d1 + d2 + s1 + s2
    print('La suma de todos los dígitos es:',sum)