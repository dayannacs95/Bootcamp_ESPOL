#EJERCICIO 1: NUMERO POSITIVO, NEGATIVO O CERO
x = int(input("Ingrese un numero: "))
z = "El valor ingresado es"
if x > 0:
    y = "POSITIVO"
elif x == 0:
    y = "CERO"
else:
    y = "NEGATIVO"
print(z,y)

#EJERCICIO 2: NUMERO PAR O IMPAR
x = int(input("Ingrese un numero entero: "))
if x%2 == 0:
    y = "PAR"
else:
    y = "IMPAR"
print(z, y)

#EJERCICIO 3: CALIFICACION DE EXAMEN
x = int(input("Ingrese su calificacion (escala de 0 a 100): "))
resultado = "Su calificación es: "
if x <= 100 and x >= 90:
    y = "A"
elif x <= 89 and x >= 80:
    y = "B"
elif x <= 79 and x >= 70:
    y = "C"
elif x <= 69 and x >= 60:
    y = "D"
else: 
    y = "F"
print(resultado,y)

#EJERCICIO 4: EL MAYOR DE TRES NUMEROS
valor1 = int(input("Ingrese primer valor: "))
valor2 = int(input("Ingrese segundo valor: "))
valor3 = int(input("Ingrese tercer valor: "))
if valor1 > valor2 and valor1 > valor3:
    y = "EL VALOR 1 ES EL NUMERO MAYOR"
elif valor2 > valor1 and valor2 > valor3:
    y = "EL VALOR 2 ES EL NUMERO MAYOR"
else: 
    y = "EL VALOR 3 ES EL NUMERO MAYOR"
print(y)