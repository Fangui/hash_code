# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 16:22:57 2017

@author: prolintos
"""

class DT:

    def _init_(self, path):
        self.rows = None
        self.pools = None
        self.R,self.S,self.U,self.P,self.M = None
        self.load();
        
    def addrow (self, row):
        self.rows.append(row);

    def addpool (self, pool):
        self.pools.append(pool);

    def load(self,path):
        f = open(path)
        self.R,self.S,self.U,self.P,self.M = f.readline().split(" ")
        