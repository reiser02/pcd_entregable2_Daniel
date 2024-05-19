import pytest
from Entregable import Publicador, Sistema, Media, DesviacionTipica, MinMax, CalcularEstadisticos


def test_alta():
    p = Publicador()
    s = Sistema.obtener_instancia()
    p.alta(s)
    assert len(p.subscriptores) == 1

def test_baja():
    p = Publicador()
    s = Sistema.obtener_instancia()
    p.alta(s)
    p.baja(s)
    assert len(p.subscriptores) == 0

def test_media():
    datos = [1, 6, 3, 5, 6, 2]
    m = Media()
    assert m.aplicar_estadistico(datos) == sum(datos) / len(datos)

def test_desviacion_tipica():
    datos = [1, 6, 3, 5, 6, 2]
    d = DesviacionTipica()
    media = sum(datos) / len(datos)
    assert d.aplicar_estadistico(datos) == (sum(map(lambda x: (x + media) ** 2, datos)) / (len(datos) - 1)) ** (1 / 2)

def test_min():
    datos = [1, 6, 3, 5, 6, 2]
    m = MinMax()
    minimo, _ = m.aplicar_estadistico(datos)
    assert minimo == min(datos) 

def test_max():
    datos = [1, 6, 3, 5, 6, 2]
    m = MinMax()
    _, maximo = m.aplicar_estadistico(datos)
    assert maximo == max(datos)

def test_calcular_estadisticos():
    datos = [1, 6, 3, 5, 6, 2]
    m = Media()
    calculadoraEstadisticos = CalcularEstadisticos(m)
    assert calculadoraEstadisticos(datos, "Media") == m.aplicar_estadistico(datos)
