# ejemplo de apertura de archivos del deber de la semana 16 en Python
#definicion del nombre del archivo
file_names="my_notes.txt"

#modo de apertura: "r" para lectura(read)
#Abrimos el archivo que acabamos de crear
archivo=open(file_names,"w")

archivo.write('Nabon\n')
archivo.write('El Pan\n')
archivo.write('Paute\n')
#cerramos el archivo
archivo.close()
 #lectura de archivo de texto
 # abrimos el archivo'my_notes.txt' en modo de lectura('r')
with open('my_notes.txt','r') as file:
     #Leemos el archivo linea por linea
     line=file.readline()
     while line:
         # mostramos en consola cada linea leida.
         print(line.strip()) # elimina saltos de lineas
         line=file.readline()