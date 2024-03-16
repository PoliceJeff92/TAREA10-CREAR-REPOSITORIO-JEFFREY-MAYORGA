def calcular_descuento(monto_total, porcentaje_descuento=10):
  """
  Calcula el descuento aplicado a un monto total de compra.

  Args:
      monto_total (float): Monto total de la compra.
      porcentaje_descuento (float, optional): Porcentaje de descuento a aplicar. Defaults to 10.

  Returns:
      float: Monto del descuento calculado.
  """
  descuento = monto_total * (porcentaje_descuento / 100)
  return descuento

# Llamadas a la función
monto_compra_1 = 1000
descuento_1 = calcular_descuento(monto_compra_1)

monto_compra_2 = 2000
porcentaje_descuento_2 = 20
descuento_2 = calcular_descuento(monto_compra_2, porcentaje_descuento_2)

# Salida de resultados
print(f"Monto compra 1: {monto_compra_1}")
print(f"Descuento 1 ({porcentaje_descuento}%): {descuento_1}")
print(f"Monto final a pagar 1: {monto_compra_1 - descuento_1}")

print(f"\nMonto compra 2: {monto_compra_2}")
print(f"Descuento 2 ({porcentaje_descuento_2}%): {descuento_2}")
print(f"Monto final a pagar 2: {monto_compra_2 - descuento_2}")
