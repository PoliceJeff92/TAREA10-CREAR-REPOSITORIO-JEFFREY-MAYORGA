# Abrir el archivo en modo escritura ("w")
with open("my_notes.txt", "w") as archivo:
    # Escribir las líneas de notas personales
    archivo.write("Mi nombre es Jeffrey Mayorga Angos, soy policía nacional con el grado de cabo primero.\n")
    archivo.write("Actualmente me encuentro trabajando en la penitenciaria de Guayaquil.\n")
    archivo.write("Tengo 31 años y estudio la carrera de ingeniería en Tics en la Universidad Estatal Amazónica.\n")
# Abrir el archivo en modo lectura ("r")
with open("my_notes.txt", "r") as archivo:
    # Leer el contenido línea por línea
    linea = archivo.readline()
    while linea:
        # Mostrar cada línea leída en la consola
        print(linea)
        # Leer la siguiente línea
        linea = archivo.readline()
