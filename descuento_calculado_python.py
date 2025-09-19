def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento
# Programa principal
monto_1 = 150.0
monto_2 = 200.0
# Llamada con porcentaje por defecto (10%)
descuento_1 = calcular_descuento(monto_1)
total_a_pagar_1 = monto_1 - descuento_1