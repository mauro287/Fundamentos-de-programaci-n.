# Programación Tradicional

def obtener_precios_productos():
    """
    Solicita al usuario que ingrese los precios de varios productos.
    Retorna una lista con los precios.
    """
    precios = []
    for i in range(1, 6):
        while True:
            try:
                precio = float(input(f"Ingrese el precio del producto {i}: "))
                precios.append(precio)
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
    return precios

def calcular_precio_total(precios):
    """
    Calcula el precio total de una lista de precios.
    """
    return sum(precios)

def main_tradicional():
    """
    Función principal para la implementación tradicional.
    """
    print("\nProgramación Tradicional:")
    precios = obtener_precios_productos()
    total = calcular_precio_total(precios)
    print(f"El precio total de los productos es: {total:.2f} USD")

# Ejecutar la versión tradicional
main_tradicional()

# Programación Orientada a Objetos (POO)

class CarritoDeCompras:
    """
    Clase para manejar un carrito de compras.
    """
    def __init__(self):
        self.precios = []

    def agregar_precio(self, precio):
        """
        Agrega un precio a la lista de precios.
        """
        self.precios.append(precio)

    def calcular_precio_total(self):
        """
        Calcula el precio total de los productos en el carrito.
        """
        if not self.precios:
            return 0.0
        return sum(self.precios)

    def ingresar_precios(self):
        """
        Solicita al usuario que ingrese los precios de varios productos.
        """
        for i in range(1, 6):
            while True:
                try:
                    precio = float(input(f"Ingrese el precio del producto {i}: "))
                    self.agregar_precio(precio)
                    break
                except ValueError:
                    print("Por favor, ingrese un número válido.")

def main_poo():
    """
    Función principal para la implementación orientada a objetos.
    """
    print("\nProgramación Orientada a Objetos (POO):")
    carrito = CarritoDeCompras()
    carrito.ingresar_precios()
    total = carrito.calcular_precio_total()
    print(f"El precio total de los productos es: {total:.2f} USD")

# Ejecutar la versión POO
main_poo()

# Comparación entre Programación Tradicional y POO

"""
1. Organización del Código:
En la Programación Tradicional, el código está estructurado en funciones separadas, lo que facilita su lectura y mantenimiento para tareas simples.
En la POO, la lógica y los datos están encapsulados en una clase, lo que favorece la modularidad y la reutilización en proyectos más complejos.

2. Escalabilidad:
La POO permite extender el programa con nuevas funcionalidades (por ejemplo, agregar descuentos o aplicar impuestos) sin afectar directamente el resto del código.
 La versión tradicional puede requerir reestructuración significativa al agregar funcionalidades más complejas.

3. Simplicidad:
La Programación Tradicional es más directa y adecuada para problemas sencillos.
 La POO introduce cierta complejidad inicial, pero ofrece mayor flexibilidad y claridad a largo plazo en proyectos 
 
"""
