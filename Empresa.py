# archivo main

""" Importacion de las clases en el archivo "paraimpor". """
from paraimpor import Proyecto, Acciones

"""Array para guardar las instancias de los proyectos"""
archivero = []

""""Aquí están las 3 instancias con datos establecidos de los proyectos"""
"""Cree las instancias de la clase proyecto y uso los datos como argumento al constructor init"""
proyecto1 = Proyecto(
    id_proyecto=1,
    nombre_proyecto="App Gestión Inventario para 'Mercado Local'",
    estado_proyecto="Desarrollo",
    fecha_inicio= "2024-01-10",  # 1 de octubre de 2024
    fecha_entrega= "2025-15-03",  # 15 de marzo de 2025
    cliente="Mercado Local S.A.",
    equipo_asignado="Frontend, Backend, QA",
    presupuesto= 45000
)

proyecto2 = Proyecto(
    id_proyecto=2,
    nombre_proyecto="Rediseño Web Corporativo 'InmoFuturo'",
    estado_proyecto="Planificación",
    fecha_inicio= "2025-20-01",  # 20 de enero de 2025
    fecha_entrega="2025-30-05",  # 30 de mayo de 2025
    cliente="InmoFuturo Bienes Raíces",
    equipo_asignado="Diseño UX, Frontend",
    presupuesto= 22000
)

proyecto3 = Proyecto(
    id_proyecto=3,
    nombre_proyecto="Sistema de Tickets 'HelpDesk Solutions'",
    estado_proyecto="Pruebas",
    fecha_inicio="2024-10-07",  # 10 de julio de 2024
    fecha_entrega="2025-28-02",  # 28 de febrero de 2025
    cliente="Soporte Express Ltda.",
    equipo_asignado="Backend, QA",
    presupuesto=38000
)

"""Guardo las instancias dentro del arreglo archivero"""
archivero.append(proyecto1)
archivero.append(proyecto2)
archivero.append(proyecto3)

"""Cree una variable para usar las funciones de Acciones del menu y dentro uso archivero como una dependencia objeto, para que el menu se ejecute correctamente"""
acciones = Acciones(archivero)

""" Bucle para seleccionar una de las opciones del menu"""
while True:
    print("\nSeleccione una opción para continuar: ")
    print("1. Agregar proyecto")
    print("2. Ver proyectos")
    print("3. Buscar proyecto por ID")
    print("4. Actualizar proyecto")
    print("5. Eliminar proyecto")
    print("6. Salir")

    """"Creo una variable de opción tipo input para seleccionar una opción"""
    opcion = input("Opción a elegir: ")

    """Condicional IF con opciones para el menú"""
    if opcion == "1":
        acciones.agregar_proyecto()
    elif opcion == "2":
        acciones.ver_proyectos()
    elif opcion == "3":
        acciones.buscar_proyecto_id()
    elif opcion == "4":
        acciones.actualizar_proyecto()
    elif opcion == "5":
        acciones.eliminar_proyecto()
    elif opcion == "6":
        break
    else:
        print("Opción inválida.")


