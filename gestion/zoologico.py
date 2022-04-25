from gestion.zona import Zona
class Zoologico:
  def __init__(self,nombre=None,ubicacion=None):
    self._nombre=nombre
    self._ubicacion=ubicacion
    self._zonas=[]
  def setNombre(self,nombre):
    self._nombre=nombre
  def setUbicacion(self,ubicacion):
    self._ubicacion=ubicacion
  def setZonas(self,zonas):
    self._zonas=zonas
  def getNombre(self):
    return self._nombre
  def getUbicacion(self):
    return self._ubicacion
  def getZona(self):
    return self._zonas
  def agregarZonas(self,zona):
    self._zonas.append(zona)
  def cantidadTotalAnimales(self):
    x=0
    for i in self._zonas:
      x+=i.cantidadAnimales()
    return x