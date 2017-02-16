# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 16:22:57 2017

@author: prolintos
"""
import row
import server
import pool
import operator

class DT:

    def __init__(self,_path):
        self.path = _path
        self.rows = []
        self.pools = []
        self.tmpServ = []
        self.R,self.S,self.U,self.P,self.M = 0,0,0,0,0
        #R = Rows
        #S = Slots per Rows
        #U = number of disabeled slots
        #P = number of pools
        #M = number of servers
        self.load() #load the file

    def disabledslot (self, row, slot):
        self.rows[row].changeStatus(slot, -2);

    def load(self):
        f = open(self.path) #read file
        self.R,self.S,self.U,self.P,self.M = f.readline().split(" ") #get start data
        self.R,self.S,self.U,self.P,self.M = int(self.R),int(self.S),int(self.U),int(self.P),int(self.M) #make them int
        self.rows = [ row.row(self.S) for i in range(self.R)] #create rows
        self.pools = [ pool.pool(i) for i in range(self.P)] #create pools
        for i in range(self.U): #disable slots
            r,s = f.readline().split(" ")
            self.disabledslot(int(r),int(s))
        for i in range(self.M): #add servers to tmp list
            s,c = f.readline().split(" ")
            self.tmpServ.append(server.server(int(s),int(c),i))
        #sort the temp servers so that we can decide how to spead them
        #order first by size then by capacity
        self.tmpServ = sorted(self.tmpServ, key=operator.attrgetter('size'))
        self.tmpServ = sorted(self.tmpServ, key=operator.attrgetter('capacity'))
        f.close()

    def dispTmpSrv(self):
        for s in self.tmpServ:
            print("Size: {0} Cap: {1}".format(s.size, s.capacity))
    
    def disp (self):
        print (str(self.R) + " rows")
        for r in self.rows:
            r.disp()
        print (str(self.P) + " pools")
        for p in self.pools:
            p.disp()
        print (str(self.S) + " slots per rows")
        print (str(self.U) + " unavailables slots")
        print (str(self.M) + " accessible servers")