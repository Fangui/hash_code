# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 16:22:57 2017

@author: prolintos
"""
import row

class DT:

    def _init_(self, path):
        self.rows = []
        self.pools = []
        self.tmpServ = []
        self.R,self.S,self.U,self.P,self.M = None
        self.load();
        
    def addrow (self, row):
        self.rows.append(row);

    def addpool (self, pool):
        self.pools.append(pool);

    def load(self,path):
        f = open(path)
        self.R,self.S,self.U,self.P,self.M = f.readline().split(" ")
        self.rows = [ row(self.S) for i in range(self.R)]

    def disabledslot (self, row, slot):
        self.rows[row].changeStatus(slot, -2);
