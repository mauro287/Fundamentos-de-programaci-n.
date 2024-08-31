#matriz de 3*3
from types import new_class

matriz=[
     [8,4,5],
     [3,6,10],
     [7,8,9]
]

print(matriz)
print(len(matriz))
#funcion buscar_ valor especifico
def buscar_valor (matriz,valor_buscado):
     for i in range(len(matriz)):
         for j in range(len(matriz)):
            if matriz[i][j]==valor_buscado:
             return i,j
valor_buscado= 6
print(buscar_valor(matriz,valor_buscado))
if valor_buscado==valor_buscado:
    print("valor encontrado en la posicion",buscar_valor(matriz,valor_buscado))
else:
    print("valor incorrecto")