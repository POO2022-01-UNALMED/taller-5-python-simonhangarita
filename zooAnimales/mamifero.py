from zooAnimales.animal import Animal
class Mamifero(Animal):
  _listado=[]
  caballos=0
  leones=0
  def __init__(self,nombre,edad,habitat,genero,pelaje,patas):
    super().__init__(nombre,edad,habitat,genero)
    self._pelaje=pelaje
    self._patas=patas
    Mamifero._listado.append(self)
    Animal.setTotalAnimales(Animal.getTotalAnimales()+1)
  @classmethod
  def setListado(cls,listado):
    cls._listado=listado
  def setPelaje(self,pelaje):
    self._pelaje=pelaje
  def setPatas(self,patas):
    self._patas=patas
  def getPelaje(self):
    return self._pelaje
  def getPatas(self):
    return self._patas
  @classmethod
  def cantidadMamiferos(cls):
    x=0
    for e in cls._listado:
      if (str(type(e).__name__)=="Mamifero"):
        x+=1
    return x
  @classmethod
  def crearCaballo(self,nombre,edad,genero):
    Mamifero.caballos+=1
    return Mamifero(nombre,edad,"pradera",genero,True,4)
  @classmethod
  def crearLeon(self,nombre,edad,genero):
    Mamifero.leones+=1
    return Mamifero(nombre,edad,"selva",genero,True,4)  