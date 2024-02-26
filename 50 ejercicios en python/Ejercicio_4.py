#4.leer un numero entero de dos digitos y determinar a cuanto es igual la suma de sus digitos

n1 = int(input('Ingrese un número entero de dos digitos '))
d1 = int(n1/10)
d2 = n1%10
sum = d1 + d2
print('La suma de los digitos es: ',sum)