#Ejercicio 1: SUMA DE DOS NUMEROS
x = int(input("Ingrese primer valor: "))
y = int(input("Ingrese segundo valor: "))
resultado = x + y
print(resultado)

#Ejercicio 2: CALCULADORA DE EDAD
import datetime as dt
year_current = dt.datetime.now().year
birth_year = int(input("Ingrese su año de nacimiento: "))
age = year_current - birth_year
print("Su edad actual es", age, "años")

#Ejercicio 3: SALUDO PERSONALIZADO
x = str(input("Ingrese su nombre: "))
print("Hola! Bienvenido(a)", x, ", espero tengas lindo dia")

#Ejercicio 4: CALCULADORA
operacion = input("Que operacion desea realizar?: ")
x = int(input("Ingrese valor 1: "))
y = int(input("Ingrese valor 2: "))
if operacion == "suma":
    print(x+y)
elif operacion == "resta":
    print(x - y)
elif operacion == "multiplicacion":
    print(x*y)
else: 
    print(x//y)
