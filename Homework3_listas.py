#imprimir nombres de frutas y alterar lista
frutas = ["papaya", "mango", "banana", "pera", "uva"]
print(frutas[0]+", "+frutas[-1])
nueva = input("Ingrese nueva fruta: ")
frutas[2] = nueva
print(frutas)

#Añadir y eliminar elementos
lst = []
lst.append(1)
lst.append(25)
lst.append(17)
lst.pop(1)
print(lst)

#operaciones
lst2 = [1,2,3,4,5]
valores = []
for numero in lst2:
    resultado = numero*2
    valores.append(resultado)
print(sum(valores))

#opcional
#crear lista de 10 numeros
import random as rd #importando modulo con funciones para numeros aleatorios
iteraciones = 10 #numeros aleatorios solicitados
lst_numeros = [] #lista vacia para almacenar los numeros generados
for i in range(iteraciones): #generando los 10 numeros aleatorios solicitados
    aleatorio = rd.randint(1,1000) 
    lst_numeros.append(aleatorio) #almacenando en la nueva lista
print(max(lst_numeros))
print(min(lst_numeros))
promedio = sum(lst_numeros)//iteraciones #calculando promedio de los valores de la lista
print(promedio)

pares =[] #lista vacia para almacenar pares
for i in lst_numeros: #iterando sobre cada elemento de la lista original
    num_par = 0 #se define variable para almacenar pares
    if i%2 == 0: #si el residuo es cero, es par
        num_par = i #se almacena en la variable si es par
        pares.append(num_par) #se agrega a la lista
print(pares) #imprime los pares
print(sorted(pares,reverse=True)) #ordena la lista de pares de mayor a menor

lista2 = [1, 34, 5567, 1, 34, 457, 75, 89, 46, 89]
valores_unicos = set(lista2) #convirtiendo a set para eliminar repetidos
print(list(valores_unicos)) #convirtiendo el conjunto a lista de nuevo