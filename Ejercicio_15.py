#16. Leer un número entero de tres dígitos y determinar si al menos dos de sus tres dígitos son iguales.
n1 = int(input('Ingrese un número entero de 3 digitos '))
primerDigito = n1 // 100
parteEntera = n1 // 10
segundoDigito = parteEntera % 10
tercerDigito = n1 % 10
