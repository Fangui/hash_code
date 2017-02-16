# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 16:22:57 2017

@author: prolintos
"""
import row
import server

class DT:

    def __init__(self, _path):
        self.rows = []
        self.pools = []
        self.tmpServ = []
        
    def addrow (self, row):
        self.rows.append(row);

    def addpool (self, pool):
        self.pools.append(pool);

    def disabledslot (self, row, slot):
        self.rows[row].changeStatus(slot, -2);

    def load(self,path):
        f = open(path)
        self.R,self.S,self.U,self.P,self.M = f.readline().split(" ")
        self.rows = [ row(self.S) for i in range(self.R)]
        for i in range(self.U):
            r,s = f.readline().split(" ")
            self.disabledslot(r,s)
        for i in range(self.M):
            s,c = f.readline().split(" ")
            self.tmpServ.append(server(s,c,i))