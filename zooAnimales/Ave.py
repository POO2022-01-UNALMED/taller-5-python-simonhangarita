import Animal
class Ave(Animal):
  _listado=[]
  halcones=0
  aguilas=0
  def __init__(self,nombre,edad,habitat,genero,colorPlumas):
    super().__init__(nombre,edad,habitat,genero)
    self._colorPlumas=colorPlumas
    Ave._listado[self]
    Animal.setTotalAnimales(Animal.getTotalAnimales()+1)
  @classmethod
  def setListado(cls,listado):
    cls._listado=listado
  def setColorPlumas(self,pelaje):
    self._colorPlumas=pelaje
  def getColorPlumas(self):
    return self._colorPlumas
  @classmethod
  def cantidadAves(cls):
    x=0
    for e in cls._listado:
      if (str(type(e).__name__)=="Ave"):
        x+=1
    return x
  @classmethod
  def crearHalcon(self,nombre,edad,genero):
    Ave.halcones+=1
    return Ave(nombre,edad,"montanas",genero,"cafe glorioso")
  @classmethod
  def crearAguila(self,nombre,edad,genero):
    Ave.aguilas+=1
    return Ave(nombre,edad,"montanas",genero,"blanco y amarillo")  
  def Movimiento(self):
    return "volar"