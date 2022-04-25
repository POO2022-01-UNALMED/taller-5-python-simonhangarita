from zooAnimales.animal import Animal
class Reptil(Animal):
  _listado=[]
  iguanas=0
  serpientes=0
  def __init__(self,nombre,edad,habitat,genero,pelaje,patas):
    super().__init__(nombre,edad,habitat,genero)
    self._colorEscamas=pelaje
    self._largoCola=patas
    Reptil._listado[self]
    Animal.setTotalAnimales(Animal.getTotalAnimales()+1)
  @classmethod
  def setListado(cls,listado):
    cls._listado=listado
  def setColorEscamas(self,pelaje):
    self._colorEscamas=pelaje
  def setLargoCola(self,patas):
    self._largoCola=patas
  def getColorEscamas(self):
    return self._colorEscamas
  def getLargoCola(self):
    return self._largoCola
  @classmethod
  def cantidadReptiles(cls):
    x=0
    for e in cls._listado:
      if (str(type(e).__name__)=="Reptil"):
        x+=1
    return x
  @classmethod
  def crearIguana(self,nombre,edad,genero):
    Reptil.iguanas+=1
    return Reptil(nombre,edad,"humedal",genero,"verde",3)
  @classmethod
  def crearSerpiente(self,nombre,edad,genero):
    Reptil.serpientes+=1
    return Reptil(nombre,edad,"jungla",genero,"blanco",1)  
  def Movimiento(self):
    return "reptar"