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

def nbUnable(self):
  (cpt, nb) = (0, 0)
  index = 0

  for i in range(capacity):
    if self.data[i] == 0:
      cpt += 1
    else:
      if cpt > nb:
        index = i
        nb = cpt
  return (nb, index)

