class Empleado:
    def __init__(self, nombre, cedula, salario):
        self.nombre = nombre
        self.cedula = cedula
        self.salario = salario

class Empleados:
    def __init__(self):
        self.empleados = []
        # Seeders
        self.nuevoEmpleado(nombre="Jose Lima", cedula="1234567", salario=1500)
        self.nuevoEmpleado(nombre="Pedro Perex", cedula="3456789", salario=1600)
        self.nuevoEmpleado(nombre="Jose Serrano", cedula="123400123", salario=1400)
        self.nuevoEmpleado(nombre="Henry Morales", cedula="123321123", salario=1000)

    def nuevoEmpleado(self, **params):
        self.empleados.append(Empleado(**params))

    def listarEmpleados(self):
        return self.empleados

    def listarEmpleadosJSON(self):
        lista = []
        for empleado in self.empleados:
            lista.append({
                "nombre": empleado.nombre,
                "cedula": empleado.cedula,
                "salario": empleado.salario
            })
        return lista

    def mostrarEmpleado(self, index):
        return self.empleados[index]

    def editarEmpleado(self, index, **params):
        self.empleados[index] = Empleado(**params)

    def eliminarEmpleado(self, index):
        del self.empleados[index]

    def sumarSalario(self):
        salarios = 0
        for empleado in self.empleados:
            salarios += empleado.salario
        return salarios
