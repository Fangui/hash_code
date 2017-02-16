# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 14:37:55 2017

@author: Thomas
"""

import os

def load(self,path):
    f = open(path)
    self.R,self.S,self.U,self.P,self.M = f.readline().split(" ")   