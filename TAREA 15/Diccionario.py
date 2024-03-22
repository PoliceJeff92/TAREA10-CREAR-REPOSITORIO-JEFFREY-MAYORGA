informacion_personal = {
    "nombre": "Ana García Rojas",
    "edad": 31,
    "ciudad": "Puyo",
}

# Acceder al valor de la ciudad
ciudad_actual = informacion_personal["ciudad"]

# Modificar la ciudad por una nueva
informacion_personal["ciudad"] = "Guayaquil"

# Agregar una nueva clave-valor (profesión)
informacion_personal["profesion"] = "Desarrolladora web"

# Verificar si la clave "telefono" existe
if "telefono" in informacion_personal:
    print("La clave 'telefono' ya existe")
else:
    # Agregar la clave "telefono" con un número ficticio
    informacion_personal["telefono"] = "0987541232"

# Eliminar la clave "edad"
del informacion_personal["edad"]

# Impresión del diccionario final
print(informacion_personal)
