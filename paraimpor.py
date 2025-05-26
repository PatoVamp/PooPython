class Proyecto :
    def __init__(self, id_proyecto, nombre_proyecto, estado_proyecto, fecha_inicio, fecha_entrega, cliente, equipo_asignado, presupuesto):
        self.id_proyecto = id_proyecto
        self.nombre_proyecto = nombre_proyecto
        self.estado_proyecto = estado_proyecto
        self.fecha_inicio = fecha_inicio
        self.fecha_entrega = fecha_entrega
        self.cliente = cliente
        self.equipo_asignado = equipo_asignado
        self.presupuesto = presupuesto

    def ver_proyectos(self):
        print(f"\nID Proyecto     : {self.id_proyecto}")
        print(f"Nombre Proyecto : {self.nombre_proyecto}")
        print(f"Estado Proyecto : {self.estado_proyecto}")
        print(f"Fecha Inicio    : {self.fecha_inicio}")
        print(f"Fecha Entrega   : {self.fecha_entrega}")
        print(f"Cliente         : {self.cliente}")
        print(f"Equipo Asignado : {self.equipo_asignado}")
        print(f"Presupuesto     : {self.presupuesto}")
        print("-" * 40)
    def actualizar_proyecto(self):
        self.nombre_proyecto = input("Nombre_Proyecto: ")
        self.estado_proyecto = input("Estado_Proyecto: ")
        self.fecha_inicio = input("Fecha_Inicio: ")
        self.fecha_entrega = input("Fecha_Entrega: ")
        self.cliente = input("Cliente: ")
        self.equipo_asignado = input("Equipo_Asignado: ")
        self.presupuesto = input("Presupuesto: ")
        print("Datos actualizados correctamente.\n")

class Acciones:
    def __init__(self, archivero):
        self.archivero = archivero
    def agregar_proyecto(self):
        while True:
            try:
                id_proyecto = int(input("ID_Proyecto: "))
                repetido = False
                for proyecto in self.archivero:
                    if proyecto.id_proyecto == id_proyecto:
                        print("El proyecto ya existe")
                        repetido = True
                        break
                if not repetido:
                    break
            except ValueError:
                print("Error: El ID debe ser un número entero.")

        nombre_proyecto = input("Nombre_Proyecto: ")
        estado_proyecto = input("Estado_Proyecto: ")
        fecha_inicio = input("Fecha_Inicio: ")
        fecha_entrega = input("Fecha_Entrega: ")
        cliente = input("Cliente: ")
        equipo_asignado = input("Equipo_Asignado: ")
        presupuesto = input("Presupuesto: ")
        nuevo_proyecto = Proyecto(id_proyecto, nombre_proyecto, estado_proyecto, fecha_inicio, fecha_entrega, cliente, equipo_asignado, presupuesto)
        self.archivero.append(nuevo_proyecto)
        print("proyecto agregado correctamente.\n")

    def ver_proyectos(self):
        if not self.archivero:
            print("No hay proyectos.")
            return
        for proyecto in self.archivero:
            proyecto.ver_proyectos()

    def buscar_proyecto_id(self):
        while True:
            try:
                id_proyecto = int(input("ID_Proyecto: "))
                for proyecto in self.archivero:
                    if proyecto.id_proyecto == id_proyecto:
                        proyecto.ver_proyectos()
                        break
                    else:
                        print("Proyecto no encontrado")
            except ValueError:
                print("Escriba un ID válido de proyecto.")


    def eliminar_proyecto(self):
        while True:
            try:
                id_proyecto = int(input("ID_Proyecto: "))
                for proyecto in self.archivero:
                    if proyecto.id_proyecto== id_proyecto:
                        self.archivero.remove(proyecto)
                        print("Proyecto eliminado correctamente.")
                        break
            except ValueError:
                print("Escriba un ID válido de proyecto.")


