# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 16:22:57 2017

@author: prolintos
"""
import row
import server

class DT:

    def __init__(self):
        self.rows = []
        self.pools = []
        self.tmpServ = []
        self.R,self.S,self.U,self.P,self.M = 0,0,0,0,0
        
    def addrow (self, row):
        self.rows.append(row);

    def addpool (self, pool):
        self.pools.append(pool);

    def disabledslot (self, row, slot):
        self.rows[row].changeStatus(slot, -2);

    def load(self,path):
        f = open(path)
        self.R,self.S,self.U,self.P,self.M = f.readline().split(" ")
        self.R,self.S,self.U,self.P,self.M = int(self.R),int(self.S),int(self.U),int(self.P),int(self.M)
        self.rows = [ row.row(self.S) for i in range(self.R)]
        for i in range(self.U):
            r,s = f.readline().split(" ")
            self.disabledslot(int(r),int(s))
        for i in range(self.M):
            s,c = f.readline().split(" ")
            self.tmpServ.append(server.server(int(s),int(c),i))
    
    def disp (self):
        print (str(self.R) + " rows")
        print (str(self.S) + " slots")
        print (str(self.U) + " unavailables slots")
        print (str(self.P) + " pools")
        print (str(self.M) + " servers to be allocated")