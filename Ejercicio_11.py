#Leer dos números enteros de dos dígitos y determinar si tienen dígitos comunes.
n1 = int(input('Ingrese un número de dos digitos: '))
n2 = int(input('Ingrese otro número de dos digitos: '))
d1 = n1//10
d2 = n1%10
sd1 = n2//10
sd2 = n2%10
if n1 > 9 and n1 < 100 and n2 > 9 and n2 < 100:
    if d1 == sd1 or d2 == sd2 or d1 == sd2 or d2 == sd1:
        print('Tienen digitos comunes')
    else: print('No tienen digitos comunes')