class Proyecto :
    """Clase para representar el proyecto."""
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
        """"Imprime los datos de un proyecto"""
        print(f"\nID Proyecto   : {self.id_proyecto}")
        print(f"Nombre Proyecto : {self.nombre_proyecto}")
        print(f"Estado Proyecto : {self.estado_proyecto}")
        print(f"Fecha Inicio    : {self.fecha_inicio}")
        print(f"Fecha Entrega   : {self.fecha_entrega}")
        print(f"Cliente         : {self.cliente}")
        print(f"Equipo Asignado : {self.equipo_asignado}")
        print(f"Presupuesto     : {self.presupuesto}")
        print()

    def actualizar_proyecto(self):
        """"Actualiza los datos de un proyecto"""
        self.nombre_proyecto = input("Nombre_Proyecto: ")
        self.estado_proyecto = input("Estado_Proyecto: ")
        self.fecha_inicio = input("Fecha_Inicio: ")
        self.fecha_entrega = input("Fecha_Entrega: ")
        self.cliente = input("Cliente: ")
        self.equipo_asignado = input("Equipo_Asignado: ")
        self.presupuesto = input("Presupuesto: ")
        print("Datos actualizados correctamente.\n")

class Acciones:
    """Clase para representar las acciones del menú."""
    def __init__(self, archivero):
        """"Inicializa la lista de proyectos."""
        self.archivero = archivero
    def agregar_proyecto(self):
        """"Agrega un nuevo proyecto a la lista."""
        while True:
            """"Crea un bucle para verificar si el ID ya existe."""
            try:
                id_proyecto = int(input("ID_Proyecto: "))
                repetido = False
                for proyecto in self.archivero:
                    """"Comprueba si el ID ya existe."""
                    if proyecto.id_proyecto == id_proyecto:
                        """"verifica si el ID ya existe y lo imprime."""
                        print("El proyecto ya existe")
                        repetido = True
                        break
                if not repetido:
                    break
            except ValueError:
                """"Verifica si hay otro tipo de dato y lo marca como error."""
                print("Error: El ID debe ser un número entero.")

        """Datos ingresados por el usuario"""
        nombre_proyecto = input("Nombre_Proyecto: ")
        estado_proyecto = input("Estado_Proyecto: ")
        fecha_inicio = input("Fecha_Inicio: ")
        fecha_entrega = input("Fecha_Entrega: ")
        cliente = input("Cliente: ")
        equipo_asignado = input("Equipo_Asignado: ")
        presupuesto = input("Presupuesto: ")

        """"Crea un nuevo proyecto y lo agrega a la lista en base a los datos ingresados."""
        nuevo_proyecto = Proyecto(id_proyecto, nombre_proyecto, estado_proyecto, fecha_inicio, fecha_entrega, cliente, equipo_asignado, presupuesto)

        """"Guarda los datos en la lista archivero"""
        self.archivero.append(nuevo_proyecto)
        print("proyecto agregado correctamente.\n")

    def ver_proyectos(self):
        """"verifica si no hay proyectos y lo imprime"""
        if not self.archivero:
            print("No hay proyectos.")
            return
        for proyecto in self.archivero:
            """"Imprime los datos de cada proyecto"""
            proyecto.ver_proyectos()

    def buscar_proyecto_id(self):
        """"Busca un proyecto por su ID y lo imprime"""
        id_proyecto = int(input("ID_Proyecto: "))
        encontrado = False
        for proyecto in self.archivero:
            """"Comprueba si el ID existe en la lista de proyectos"""
            if proyecto.id_proyecto == id_proyecto:
                proyecto.ver_proyectos()
                """"si encontrado es verdadero, imprime el proyecto"""
                encontrado = True
                break
        if not encontrado:
            print("Proyecto no encontrado.")

    def actualizar_proyecto(self):
        """"Actualiza los datos de un proyecto"""
        id_proyecto = int(input("ID_Proyecto: "))
        for proyecto in self.archivero:
            if proyecto.id_proyecto == id_proyecto:
                """""llamo la funcion actualizar_proyecto y se ejecuta en proyecto"""
                proyecto.actualizar_proyecto()
                break
        else:
            print("Escriba un ID válido de proyecto.")

    def eliminar_proyecto(self):
        """"Elimina un proyecto de la lista"""
        id_proyecto = int(input("ID_Proyecto: "))
        for proyecto in self.archivero:
            if proyecto.id_proyecto == id_proyecto:
                """""Elimina el proyecto de la lista del archivero"""
                self.archivero.remove(proyecto)
                print("Proyecto eliminado correctamente.")
                break
        else:
            print("Escriba un ID válido de proyecto.")


