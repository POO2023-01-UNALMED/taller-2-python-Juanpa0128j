class Motor():
    def __init__(self, numeroCilindros, registro, tipo):
        self.numeroCilindros = numeroCilindros
        self.registro = registro
        self.tipo = tipo

    def cambiarRegistro(self, registro):
        self.registro = registro
    
    def asignarTipo(self, tipo):
        self.tipo = tipo

class Asiento():
    def __init__(self, precio, registro, color):
        self.precio = precio
        self.registro = registro
        self.color = color

    def cambiarColor(self, color):
        if color == "rojo" or color == "verde" or color == "amarillo" or color == "negro" or color == "blanco":
            self.color = color

class Auto():
    cantidadCreados = 0
    asientos = []
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.marca = marca
        self.precio = precio
        self.registro = registro
        self.motor = motor
        self.cantidadCreados += 1
        self.asientos = asientos
    
    @classmethod
    def cantidadAsientos(cls):
        return len(cls.asientos)

    def verificarIntegridad(self):
        P = "Auto original"
        for n in self.asientos:
            if self.registro !=  n.registro or self.registro != self.motor.registro or self.motor.registro != n.registro:
                P = "Las  piezas no son originales"

        return P