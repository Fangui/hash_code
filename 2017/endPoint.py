class endPoint:
  def __init__(self, lat1):
    self.lat1 = lat1
    self.list = []

  def addCacheLat(self, lat, cache):
     self.list.append((cache,lat))

      
