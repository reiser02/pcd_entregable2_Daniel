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
    def __init__(self, sucesor=None):
        self._sucesor = sucesor

    def calcular(self):
        pass

class CalcularEstadisticos(Comprobaciones):
    def __init__(self, estrategias, sucesor):
        super().__init__(sucesor)
        self.estrategias = dict()
        self.estrategias = estrategias

    def calcular(self, datos):
        if self._sucesor is not None:
            resultado_sucesor = self._sucesor.calcular(datos)
        
        resultado_estadisticos = list()

        for e in self.estrategias:
            resultado_estadisticos.append(e.aplicar_estadistico(datos))

        if self._sucesor is not None:
            return resultado_sucesor + resultado_estadisticos
        
        return resultado_estadisticos
        
class ComprobarUmbral(Comprobaciones):
    def __init__(self, sucesor, umbral):
        super().__init__(sucesor)
        self.umbral = umbral

    def calcular(self, datos):
        if self._sucesor is not None:
            return self._sucesor.calcular(datos) + [datos[11] > self.umbral]
        
        return [datos[11] > self.umbral]

class DiferenciaTemperatura(Comprobaciones):
    def calcular(self, datos):
        if self._sucesor is not None:
            return self._sucesor.calcular(datos) + [(datos[11] - datos[5]) > 10]

        return [(datos[11] - datos[5]) > 10]   

class Publicador:
    def __init__(self):
        self.subscriptores = list()

    def alta(self, subscriptor):
        self.subscriptores.append(subscriptor)

    def baja(self, subscriptor):
        try:
            self.subscriptores.remove(subscriptor)
        except Exception as e:
            print(e)
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

        estadisticos = CalcularEstadisticos([Media(), DesviacionTipica(), MinMax()])
        umbral = ComprobarUmbral(estadisticos, 25)
        
        self.comprobaciones = DiferenciaTemperatura(umbral)

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

        print(self.comprobaciones(self.datos))

