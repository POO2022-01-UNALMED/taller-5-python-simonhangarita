from zooAnimales.animal import Animal
class Pez(Animal):
  _listado=[]
  salmones=0
  bacalaos=0
  def __init__(self,nombre,edad,habitat,genero,pelaje,patas):
    super().__init__(nombre,edad,habitat,genero)
    self._colorEscamas=pelaje
    self._cantidadAletas=patas
    Pez._listado[self]
    Animal.setTotalAnimales(Animal.getTotalAnimales()+1)
  @classmethod
  def setListado(cls,listado):
    cls._listado=listado
  def setColorEscamas(self,pelaje):
    self._colorEscamas=pelaje
  def setCantidadAletas(self,patas):
    self._cantidadAletas=patas
  def getColorEscamas(self):
    return self._colorEscamas
  def getCantidadAletas(self):
    return self._cantidadAletas
  @classmethod
  def cantidadPeces(cls):
    x=0
    for e in cls._listado:
      if (str(type(e).__name__)=="Pez"):
        x+=1
    return x
  @classmethod
  def crearSalmon(self,nombre,edad,genero):
    Pez.salmones+=1
    return Pez(nombre,edad,"oceano",genero,"rojo",6)
  @classmethod
  def crearBacalao(self,nombre,edad,genero):
    Pez.bacalaos+=1
    return Pez(nombre,edad,"oceano",genero,"gris",6)  
  def Movimiento(self):
    return "nadar"