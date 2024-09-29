# ejemplo del diccionario

animales={
    "domesticos":"Gato",
    "salvajes":"tigre",
    "acuaticos":"Tiburon",
     "aves":"Paloma",
    "reptiles":"Serpiente",
}
# obtenemos valores
print("domesticos:",animales["domesticos"])
print("salvajes:",animales["salvajes"])
print("acuaticos:",animales["acuaticos"])
print("aves:",animales["aves"])
print("reptiles:",animales["reptiles"])
#Agregar un nuevo par clave
animales["salvajes"]="Tiburon,tigre,serpiente"
print("todo:",animales)
# eliminar un par clave
del animales["aves"]
print("todo:",animales)
#imprime valores
valores=animales.values()
print("imprime los valores",valores)
#imprime claves
claves=animales.keys()
print("imprime las claves",claves)
#recorremos con un for
for claves,valores in animales.items():
    print(claves,valores)