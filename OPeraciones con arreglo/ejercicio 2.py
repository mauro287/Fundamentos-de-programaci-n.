# ejercicio 2 matriz de 3*3
matriz=[
    [8,4,5],
    [3,6,10],
    [7,8,9]
]

print(matriz)
#blucle de ordenamiento blucle_sort
def bubble_sort(fila):
    # algoritmo de blucle sort ejemplo
   n=len(fila)
   for i in range(n):
       for j in range (n-1,i,-1):
           if fila[j]>fila[j-1]:
               fila[j], fila[j-1]=fila[j-1], fila[j]
               print(fila)

print("matriz original")
print(matriz)
bubble_sort(matriz[1])
print(matriz)