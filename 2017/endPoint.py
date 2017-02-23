def getKey(item):
  return item[1]

class endPoint:
  def __init__(self, lat1):
    self.lat1 = lat1
    self.list = []

  def addCacheLat(self, lat, cache):
     self.list.append((cache,lat))

  def savingLat(self):
    savings = [0] * len(self.list)
    for i in range(len(self.list)):
      latSaved = self.lat1 - self.list[i][1]
      savings[i] = (self.list[i][0], latSaved)

    sorted(savings, key = getKey)
    return savings

 
