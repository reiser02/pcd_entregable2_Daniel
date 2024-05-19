class Publicador:
    def __init__(self):
        self.subscriptores = list()

    def alta(self, subscriptor):
        self.subscriptores.append(subscriptor)

    def baja(self, subscriptor):
        self.subscriptores.remove(subscriptor)

    def notificar_subscriptores(self):
        for s in self.subscriptores:
            s.actualizar()

class Subscriptor:
    def actualizar(self):
        pass

class Sistema(Subscriptor):
    _unicaInstancia = None
    
    def __init__(self):
        self.datos = list()

    @classmethod
    def obtener_instancia(cls):
        if cls._unicaInstancia is None:
            cls._unicaInstancia = cls()
        return cls._unicaInstancia
    
    def actualizar(self, valor):
        if len(self.datos) == 12:
            self.datos.pop(0)
            self.datos.append(valor)
        else:
            self.datos.append(valor)

class EstrategiaEstadisticos:
    def aplicar_estadistico(self):
        pass

class Media(EstrategiaEstadisticos):
    def aplicar_estadistico(self, datos):
        return sum(datos) / len(datos)
    
class DesviacionTipica(EstrategiaEstadisticos):
    def aplicar_estadistico(self, datos):
        media = sum(datos) / len(datos)
        return (sum(map(lambda x: (x + media) ** 2, datos)) / (len(datos) - 1)) ** (1 / 2)
    
class MinMax(EstrategiaEstadisticos):
    def aplicar_estadistico(self, datos):
        return min(datos), max(datos)
    
class Comprobaciones:
    def __init__(self, sucesor):
        self._sucesor = sucesor

    def calcular(self):
        pass

class CalcularEstadisticos(Comprobaciones):
    def __init__(self, estrategia, sucesor):
        super().__init__(sucesor)
        self.estrategias = dict()

        for e in estrategia:
            self.estrategias[e.__class__.__name__] = e

    def calcular(self, datos, estrategia):
        return self.estrategias[estrategia].aplicar_estadistico(datos)
        

