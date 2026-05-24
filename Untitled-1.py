# -------------------------------
# Problema 2: Gestión de precios de un menú de restaurante
# -------------------------------

# Matriz con productos: [Nombre, Categoría, Precio Base]
menu = [
    ["Hamburguesa", "Comida Rápida", 25000],
    ["Pizza", "Comida Rápida", 32000],
    ["Ensalada", "Saludable", 18000],
    ["Sopa", "Entrada", 12000],
    ["Filete de Res", "Plato Fuerte", 45000],
    ["Jugo Natural", "Bebida", 8000]
]

# Parámetros de la promoción
CATEGORIA_OBJETIVO = "Comida Rápida"
UMBRAL_PRECIO = 20000
DESCUENTO = 0.15

# -------------------------------
# Módulo para calcular precio final
# -------------------------------
def calcular_precio_final(categoria, precio_base):
    """
    Aplica un 15% de descuento si:
    - El producto pertenece a la categoría objetivo
    - Su precio base es mayor al umbral definido
    """
    if categoria == CATEGORIA_OBJETIVO and precio_base > UMBRAL_PRECIO:
        return precio_base * (1 - DESCUENTO)
    else:
        return precio_base

# -------------------------------
# Mostrar resultados
# -------------------------------
print("Menú con promoción aplicada:\n")
for producto in menu:
    nombre, categoria, precio_base = producto
    precio_final = calcular_precio_final(categoria, precio_base)
    print(f"Producto: {nombre} | Categoría: {categoria} | "
          f"Precio Base: ${precio_base} | Precio Final: ${precio_final:.2f}")
