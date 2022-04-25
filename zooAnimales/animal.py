
class Animal:
  _totalAnimales=0
  def __init__(self,nombre,edad,habitat,genero):
    self._nombre=nombre
    self._edad=edad
    self._habitat=habitat
    self._genero=genero
    self._zona=None
    Animal._totalAnimales+=1
  @classmethod
  def getTotalAnimales(cls):
    return cls._totalAnimales
  def getNombre(self):
    return self._nombre
  def getEdad(self):
    return self._edad
  def getHabitat(self):
    return self._habitat
  def getGenero(self):
    return self._genero
  def getZona(self):
    return self._zona
  @classmethod
  def setTotalAnimales(cls,total):
    cls._totalAnimales=total
  def setNombre(self,nombre):
    self._nombre=nombre
  def setEdad(self,nombre):
    self._edad=nombre
  def setHabitat(self,nombre):
    self._habitat=nombre
  def setGenero(self,nombre):
    self._genero=nombre
  def setZona(self,nombre):
    self._zona=nombre
  def movimiento(self):
    return "desplazarse"
  def __str__(self):
    if self._zona is None:
      return "Mi nombre es "+str(self._nombre)+", tengo una edad de "+str(self._edad)+", habito en"+str(self._habitat)+" y mi genero es "+str(self._genero)
    else:
      return "Mi nombre es "+str(self._nombre)+", tengo una edad de "+str(self._edad)+", habito en"+str(self._habitat)+" y mi genero es "+str(self._genero)+", la zona en la que me ubico es"+str(self._zona)+", en el zoo"+str(self._zona.getZoo())
  @classmethod
  def totalPorTipo(cls):
    return "Mamiferos: "+str(Mamifero.cantidadMamiferos())+"\nAves: "+str(Ave.cantidadAves())+"\nReptiles: "+str(Reptil.cantidadReptiles())+"\nPeces: "+str(Pez.cantidadPeces())+"\nAnfibios: "+ str(Anfibio.cantidadAnfibios())
    
      
    