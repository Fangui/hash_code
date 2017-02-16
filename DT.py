# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 16:22:57 2017

@author: prolintos
"""

class DT:
     
     def _init_(self, rows, pools):
         self.rows = rows;
         self.pools = pools;
    
     def addrow (self, row):
        self.rows.append(row);
        
     def addpool (self, pool):
        self.pools.append(pool);
        
    