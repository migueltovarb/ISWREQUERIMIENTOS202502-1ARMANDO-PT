import csv
import os

# Nombre del archivo donde se guardarán los contactos
ARCHIVO = "contactos.csv"


# ----------------------------
# Función para cargar contactos
# ----------------------------
def cargar_contactos():
    contactos = []
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, newline="", encoding="utf-8") as f:
            lector = csv.reader(f)
            for fila in lector:
                if len(fila) == 4:  # [nombre, teléfono, correo, cargo]
                    contactos.append(fila)
    return contactos


# ----------------------------
# Función para guardar contactos
# ----------------------------
def guardar_contactos(contactos):
    with open(ARCHIVO, "w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerows(contactos)


# ----------------------------
# Registrar nuevo contacto
# ----------------------------
def registrar_contacto(contactos):
    nombre = input("Nombre: ").strip()
    telefono = input("Teléfono: ").strip()
    correo = input("Correo: ").strip().lower()
    cargo = input("Cargo: ").strip()

    # Validar que el correo no esté repetido
    for c in contactos:
        if c[2] == correo:
            print("❌ Ese correo ya está registrado.")
            return

    contactos.append([nombre, telefono, correo, cargo])
    guardar_contactos(contactos)
    print(" Contacto guardado con éxito.")


# ----------------------------
# Buscar contacto
# ----------------------------
def buscar_contacto(contactos):
    termino = input("Escribe el nombre o correo a buscar: ").strip().lower()
    encontrados = []

    for c in contactos:
        if termino in c[0].lower() or termino in c[2].lower():
            encontrados.append(c)

    if encontrados:
        print("\nContactos encontrados:")
        for c in encontrados:
            print(f" {c[0]} | {c[1]} |  {c[2]} |  {c[3]}")
    else:
        print(" No se encontró ningún contacto.")


# ----------------------------
# Listar todos los contactos
# ----------------------------
def listar_contactos(contactos):
    if not contactos:
        print("No hay contactos registrados.")
        return
    print("\nLista de contactos:")
    for c in contactos:
        print(f" {c[0]} |  {c[1]} |  {c[2]} |  {c[3]}")


# ----------------------------
# Eliminar contacto
# ----------------------------
def eliminar_contacto(contactos):
    correo = (
        input("Escribe el correo del contacto que deseas eliminar: ").strip().lower()
    )
    for c in contactos:
        if c[2] == correo:
            contactos.remove(c)
            guardar_contactos(contactos)
            print(" Contacto eliminado correctamente.")
            return
    print(" No se encontró un contacto con ese correo.")


# ----------------------------
# Menú principal
# ----------------------------
def menu():
    contactos = cargar_contactos()

    while True:
        print("\n--- ConnectMe - Directorio de Contactos ---")
        print("1. Registrar contacto")
        print("2. Buscar contacto")
        print("3. Listar contactos")
        print("4. Eliminar contacto")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            registrar_contacto(contactos)
        elif opcion == "2":
            buscar_contacto(contactos)
        elif opcion == "3":
            listar_contactos(contactos)
        elif opcion == "4":
            eliminar_contacto(contactos)
        elif opcion == "5":
            print(" Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta otra vez.")


# ----------------------------
# Ejecución del programa
# ----------------------------
if __name__ == "__main__":
    menu()
