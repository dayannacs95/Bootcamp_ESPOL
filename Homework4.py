harry_potter = open("datos_HarryPotter.txt", "r", encoding="utf8")
for line in harry_potter:
    cap1 = harry_potter.readline().strip()
    print(cap1)

harry_potter.close()

harry_potter = open("datos_HarryPotter.txt", "r", encoding="utf8")
words = 0 #inicializar variable para contar palabras
l_palabras = 0 
for line in harry_potter:
    l_palabras = harry_potter.readline().strip().split(" ") #crea lista con las palabras de cada linea del archivo
    words += len(l_palabras) #cuenta cada elemento de la lista y los suma en cada iteración
print("El total de palabras contenidas en este fragmento es {}".format(words))

countries = open("paises_tarea.txt", "r", encoding="utf8")
lineas = countries.readlines() #lee todas las lineas del archivo, muestra una lista donde cada elemento es una cadena de texto
print(">>>")
dict_paises = dict()
for line in lineas:
    datos = line.split(',') # crea variable que divide cada elemento de la linea segun el delimitador ","
    ciudad = datos[0].strip().split(": ") #indexa la posicion para separar el pais de la ciudad
    l_ciudad = ciudad[1] #crea lista de ciudades
    dict_paises[ciudad[0]] = l_ciudad #guarda en el diccionario
print("Algunos paises del mundo, con sus respecivas capitales son: {}".format(dict_paises))

ventas = open("ventas.txt", "r", encoding="utf8")

lineas = ventas.readlines()
dict_ventas = dict()
for line in lineas:
    datos = line.split(',')
    registros = datos[0].strip().split(": ")
    ventas = registros[1]
    dict_ventas[registros[0]] = (ventas)
print("En el trimestre se han registrado las siguientes ventas: {}".format(dict_ventas))

suma_ventas = 0
total_ventas = list(dict_ventas.values())
meses = list(dict_ventas.keys())

for i in total_ventas:
    suma_ventas += int(i)
print("Las ventas totales son: $", suma_ventas)

indice_mes = total_ventas.index(max(total_ventas))
ventas_mas_altas = meses[indice_mes]
print("El mes con las ventas más altas fue {}".format(ventas_mas_altas))

promedio = round((suma_ventas/len(meses)),2)
print("El promedio de ventas mensual es de: ${}".format(promedio))