class Cliente:
    
    def __init__(self, nombre, apellido, DNI, email , celular):
        self.nombre = nombre
        self.apellido = apellido
        self.Dni = DNI
        self.email = email
        self.celular = celular
    
    def __str__(self):
        return f'Nombre del cliente: {self.nombre}\n apellido : {self.apellido}\n DNI: {self.Dni}\n celular: {self.celular}'

    def setNombre(self,nombre):
        self.nombre = nombre
