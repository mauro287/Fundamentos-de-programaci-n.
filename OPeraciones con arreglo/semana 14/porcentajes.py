#funcion para calcular el descuento


def calcular_descuento(valor_total,porcentaje_descuento=10):
       descuento=valor_total*porcentaje_descuento/100
       return descuento
descuento1=calcular_descuento(2000)
print(f'el valor del descuento es :',descuento1)

## monto total y porcentaje

monto_total2=3000
porcentaje_descontar=20
descuento2=calcular_descuento(monto_total2,porcentaje_descontar)
print(f"el monto total es :",monto_total2)
print(f'el valor de descuento es del ejemplo 2:',descuento2)
