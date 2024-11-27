print("sofia larios rodriguez y sandra oddet garcia tapia")
# Programa con ciclo de vida básico para gestionar tabla de skincare

# Verificación de contraseña
contraseña_correcta = "lars88"
intentos = 3

while intentos > 0:
    contraseña = input("Introduce la contraseña: ")
    if contraseña == contraseña_correcta:
        print("Contraseña correcta. Bienvenido al sistema.")
        break
    else:
        intentos -= 1
        print(f"Contraseña incorrecta. Te quedan {intentos} intentos.")
else:
    print("Acceso denegado. Fin del programa.")
    exit()

# Tabla inicial de skincare (10x10)
skincare = {
    "Limpieza": ["Gel limpiador", "Espuma facial", "Agua micelar", "Aceite limpiador", "Bálsamo limpiador",
                 "Jabón facial", "Exfoliante enzimático", "Tónico exfoliante", "Limpiador bifásico", "Toallitas desmaquillantes"],
    "Hidratación": ["Crema ligera", "Gel hidratante", "Crema rica", "Hidratante en spray", "Mascarilla nocturna",
                    "Aceite facial", "Hidratante con SPF", "Suero hidratante", "Loción hidratante", "Bálsamo hidratante"],
    "Protección solar": ["SPF mineral", "SPF químico", "Protector en spray", "Protector en stick", "Base con SPF",
                         "BB cream SPF", "Polvo con SPF", "Labial SPF", "Protector niños SPF", "Protector para deporte"],
    "Exfoliación": ["Exfoliante químico", "Exfoliante físico", "Mascarilla exfoliante", "Tónico con AHA", "Gel con BHA",
                    "Limpiador exfoliante", "Exfoliante de labios", "Scrub corporal", "Exfoliante natural", "Exfoliante en pads"],
    "Antiedad": ["Retinol", "Péptidos", "Suero antioxidante", "Crema con ácido hialurónico", "Mascarilla antiedad",
                 "Aceite con retinol", "Crema reafirmante", "Contorno de ojos", "Tónico antiedad", "Sérum con niacinamida"],
    "Tratamientos": ["Suero antiacné", "Gel para manchas", "Crema antimanchas", "Ampollas revitalizantes", "Suero calmante",
                     "Mascarilla detox", "Parches antiacné", "Corrector de rojeces", "Tratamiento antibrillos", "Loción para cicatrices"],
    "Tónicos": ["Tónico hidratante", "Tónico purificante", "Tónico con ácido glicólico", "Tónico calmante", "Tónico antioxidante",
                "Agua de rosas", "Tónico matificante", "Tónico para poros", "Bruma facial", "Tónico iluminador"],
    "Mascarillas": ["Mascarilla en hoja", "Mascarilla peel-off", "Mascarilla de arcilla", "Mascarilla iluminadora", "Mascarilla calmante",
                    "Mascarilla purificante", "Mascarilla antiacné", "Mascarilla antioxidante", "Mascarilla de colágeno", "Mascarilla hidratante"],
    "Labios": ["Bálsamo labial", "Exfoliante labial", "Aceite labial", "Mascarilla nocturna labial", "Gloss hidratante",
               "Protector solar labial", "Bálsamo con color", "Suero labial", "Hidratante intensivo", "Parches labiales"],
    "Ojos": ["Contorno de ojos hidratante", "Contorno de ojos antiedad", "Parches de gel para ojos", "Suero iluminador", "Crema para ojeras",
             "Roll-on descongestionante", "Mascarilla para ojos", "Suero calmante", "Corrector iluminador", "Gel refrescante"]
}

# Menú interactivo
while True:
    print("\n--- Menú ---")
    print("1. Agregar producto")
    print("2. Consultar productos")
    print("3. Modificar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("Selecciona una opción (1-5): ")

    if opcion == "1":  # Agregar producto
        print("\nCategorías disponibles:")
        for categoria in skincare:
            print(f"- {categoria}")
        categoria = input("Introduce la categoría donde deseas agregar el producto: ")

        if categoria in skincare:
            nuevo_producto = input("Introduce el nombre del nuevo producto: ")
            skincare[categoria].append(nuevo_producto)
            print(f"Producto '{nuevo_producto}' agregado en la categoría '{categoria}'.")
        else:
            print("Categoría no encontrada. Intenta de nuevo.")

    elif opcion == "2":  # Consultar productos
        print("\n--- Productos por categoría ---")
        for categoria, productos in skincare.items():
            print(f"{categoria}:")
            for i, producto in enumerate(productos, start=1):
                print(f"  {i}. {producto}")

    elif opcion == "3":  # Modificar producto
        print("\nCategorías disponibles:")
        for categoria in skincare:
            print(f"- {categoria}")
        categoria = input("Introduce la categoría del producto a modificar: ")

        if categoria in skincare:
            print(f"Productos en '{categoria}':")
            for i, producto in enumerate(skincare[categoria], start=1):
                print(f"{i}. {producto}")
            index = int(input("Selecciona el número del producto a modificar: ")) - 1

            if 0 <= index < len(skincare[categoria]):
                nuevo_nombre = input("Introduce el nuevo nombre del producto: ")
                skincare[categoria][index] = nuevo_nombre
                print("Producto modificado con éxito.")
            else:
                print("Número inválido.")
        else:
            print("Categoría no encontrada.")

    elif opcion == "4":  # Eliminar producto
        print("\nCategorías disponibles:")
        for categoria in skincare:
            print(f"- {categoria}")
        categoria = input("Introduce la categoría del producto a eliminar: ")

        if categoria in skincare:
            print(f"Productos en '{categoria}':")
            for i, producto in enumerate(skincare[categoria], start=1):
                print(f"{i}. {producto}")
            index = int(input("Selecciona el número del producto a eliminar: ")) - 1

            if 0 <= index < len(skincare[categoria]):
                eliminado = skincare[categoria].pop(index)
                print(f"Producto '{eliminado}' eliminado con éxito.")
            else:
                print("Número inválido.")
        else:
            print("Categoría no encontrada.")

    elif opcion == "5":  # Salir
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intenta de nuevo.")
