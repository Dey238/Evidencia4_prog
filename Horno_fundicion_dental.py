class Horno_Fundicion:
    def __init__(self, Numero_serie, Marca, Modelo, Capacidad, Peso, Potencia, Temperatura, Estado):
        self.__Numero_serie = Numero_serie
        self.__Marca = Marca
        self.__Modelo = Modelo
        self.__Capacidad = Capacidad
        self.__Peso = Peso
        self.__Potencia = Potencia
        self.__Temperatura = Temperatura
        self.__Estado = Estado

    def get_Numero_serie(self):
        return self.__Numero_serie
    def set_Numero_serie(self, Numero_serie):
        self.__Numero_serie = Numero_serie

    def get_Marca(self):
        return self.__Marca
    def set_Marca(self, Marca):
        self.__Marca = Marca

    def get_Modelo(self):
        return self.__Modelo
    def set_Modelo(self, Modelo):
        self.__Modelo = Modelo

    def get_Capacidad(self):
        return self.__Capacidad
    def set_Capacidad(self, Capacidad):
        self.__Capacidad = Capacidad

    def get_Peso(self):
        return self.__Peso
    def set_Peso(self, Peso):
        self.__Peso = Peso

    def get_Potencia(self):
        return self.__Potencia
    def set_Potencia(self, Potencia):
        self.__Potencia = Potencia

    def get_Temperatura(self):
        return self.__Temperatura
    def set_Temperatura(self, Temperatura):
        self.__Temperatura = Temperatura

    def get_Estado(self):
        return self.__Estado
    def set_Estado(self, Estado):
        self.__Estado = Estado

    def encender(self): 
        if self.__Estado == "Apagado": 
            self.__Estado = "Encendido"
            return (f"Estado: {self.__Estado}")
        else: 
            return (f"Estado: {self.__Estado}")

    def apagar(self): 
        if self.__Estado != "Apagado":
            self.__Estado = "Apagado"
            return (f"Estado: {self.__Estado}")
        else:
            return (f"El horno está apagado")

    def __add__(self, incremento):
        if self.__Estado == "Encendido":
            self.__Temperatura += incremento         
        else:
            return (f"Horno apagado. No se puede aumentar temperatura.")
    
    def __sub__(self, decremento):
        if self.__Estado == "Encendido":
            nueva_temperatura = self.__Temperatura - decremento
            if nueva_temperatura >= 0:
                self.__Temperatura = nueva_temperatura
                return (f"Temperatura ajustada en: {self.__Temperatura}")
            else:
                return (f"La temperatura no puede ser inferior a 0°C.")
        else:
            return "Horno apagado"
