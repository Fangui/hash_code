class row:
  def __init__(self, capacity):
    self.capacity = capacity
    self.data = [0] * capacity
    self.servers = []

def Print(self):
  for i in range(capacity):
    print(self.data[i])

def addServer(self,server):
  self.servers.append(server)

def changeStatus(self, index, server):
  self.data[index] = server

def listEnable(self):
  cpt = 0
  add = True
  arr = []
  for i in range(capacity):
    if self.data[i] == 0:
      cpt += 1
    elif self.data[i] == -2:
      if add:
        arr.append( (cpt,i) )
        add = False
        cpt = 0
    elif self.data[i] == -1:
      add = True
    else:
      print("WTF VALUE")

  return arr

