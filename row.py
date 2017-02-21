import server

class row:
  def __init__(self, capacity):
    self.capacity = capacity
    self.data = [0] * capacity
    self.servers = []

  def dispServer(self):
    for i in range(len(self.servers)):
      print(self.servers[i].size)

  def disp(self):
    print("row->")
    print(self.data)
    print("serv")
    self.dispServer()
      
  def addServer(self,server):
    i = 0
    Len = len(self.servers)
    while i < Len and server.size < self.servers[i].size:
      i += 1
    self.servers.insert(i, server)

  def changeStatus(self, index, server):
    self.data[index] = server

  def listEnable(self):
    cpt = 0
    add = True
    arr = []
    for i in range(self.capacity):
      if self.data[i] == 0:
        cpt += 1
        if i == self.capacity - 1:
          arr.append( (cpt, i - cpt + 1) )
      elif self.data[i] == -2:
        add = True
        if add and cpt > 0:
          arr.append( (cpt,i - cpt) )
          add = False
          cpt = 0
      elif self.data[i] == -1:
        add = True
        print("This algo shouldn't enter this case")
      else:
        print("WTF VALUE")

    return arr

  def insertServer(self, l):
    Length = len(l)
    LenS = len(self.servers)
    i = 0

    while i < LenS:
      B = True
      j = 0
      ins = False
      while j < Length and B:
        if l[j][0] == self.servers[i].size:
          B = False
          self.servers.pop(i)
          LenS -= 1
          i -= 1
          for k in range(l[j][1], l[j][0] + l[j][1]):
            self.data[k] = -1
        elif l[j][0] > self.servers[i].size:
          pos = j
          ins = True
        j += 1
        
        if j == Length and ins:
          for k in range(l[pos][1], l[pos][1] + self.servers[i].size):
            self.data[k] = -1
          l[pos] = list(l[pos])
          l[pos][0] -= l[pos][1]
          l[pos][1] += l[pos][1]
          l[pos] = tuple(l[pos])
          self.servers.pop(i)
          LenS -= 1
          i -= 1
        
      i += 1
"""
serv = server.server(3, 62, 0, 0)
serv2 = server.server(8, 15, 0, 0)
serv3 = server.server(4, 51, 0, 0)

l = row(20)

l.changeStatus(4, -2)
l.changeStatus(8, -2)

l.addServer(serv)
l.addServer(serv2)
l.addServer(serv3)
l.disp()
L = l.listEnable()
print(L)

l.insertServer(L)

l.disp()
"""
