#Programa para calcular el descuento aplicado al monto total de la compra

def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicando un porcentaje al monto total de la compra.

    Args:
        monto_total (float): El monto total de la compra
        porcentaje_descuento (float): El porcentaje de descuento (por defecto 10%)

    Returns:
        float: El monto del descuento calculado
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento


# Programa principal
def main():
    print("=== CALCULADORA DE DESCUENTOS ===\n")

    # Primera llamada: solo con el monto total (usa descuento por defecto del 10%)
    monto1 = 1000.0
    descuento1 = calcular_descuento(monto1)
    print(f"Compra 1:")
    print(f"Monto total: ${monto1:.2f}")
    print(f"Descuento aplicado: {10}%")
    print(f"Monto del descuento: ${descuento1:.2f}")
    print(f"Monto final a pagar: ${monto1 - descuento1:.2f}")
    print("-" * 40)

    # Segunda llamada: con monto total y porcentaje de descuento personalizado
    monto2 = 750.0
    porcentaje2 = 15
    descuento2 = calcular_descuento(monto2, porcentaje2)
    print(f"Compra 2:")
    print(f"Monto total: ${monto2:.2f}")
    print(f"Descuento aplicado: {porcentaje2}%")
    print(f"Monto del descuento: ${descuento2:.2f}")
    print(f"Monto final a pagar: ${monto2 - descuento2:.2f}")
    print("-" * 40)

    # Ejemplo adicional con entrada del usuario
    print("\n=== CÁLCULO PERSONALIZADO ===")
    try:
        monto_usuario = float(input("Ingrese el monto total de su compra: $"))

        # Preguntamos si quiere usar descuento personalizado
        usar_personalizado = input("¿Desea aplicar un descuento personalizado? (s/n): ").lower()

        if usar_personalizado == 's':
            porcentaje_usuario = float(input("Ingrese el porcentaje de descuento: "))
            descuento_usuario = calcular_descuento(monto_usuario, porcentaje_usuario)
            porcentaje_mostrar = porcentaje_usuario
        else:
            descuento_usuario = calcular_descuento(monto_usuario)
            porcentaje_mostrar = 10

        print(f"\nResumen de su compra:")
        print(f"Monto total: ${monto_usuario:.2f}")
        print(f"Descuento aplicado: {porcentaje_mostrar}%")
        print(f"Monto del descuento: ${descuento_usuario:.2f}")
        print(f"Monto final a pagar: ${monto_usuario - descuento_usuario:.2f}")

    except ValueError:
        print("Error: Por favor ingrese valores numéricos válidos.")


if __name__ == "__main__":
    main()