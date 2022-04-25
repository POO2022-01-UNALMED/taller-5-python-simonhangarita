from zooAnimales.animal import Animal
class Zona:
  def __init__(self,nombre,zoo):
    self._nombre=nombre
    self._zoo=zoo
    self._animales=[]
  def getNombre(self):
    return self._nombre
  def getZoo(self):
    return self._zoo
  def getAnimales(self):
    return self._animales
  def setNombre(self,nombre):
    self._nombre=nombre
  def setZoo(self,nombre):
    self._zoo=nombre
  def setAnimales(self,nombre):
    self._animales=nombre
  def agregarAnimales(self,animal):
    self._animales.append(animal)
  def cantidadAnimales(self):
    x=0
    for i in self._animales:
      if (str(type(i).__name__)=="Animal"):
        x+=1
    return x 