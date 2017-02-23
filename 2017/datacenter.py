# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 17:57:35 2017

@author: Thomas
"""

import video

class datacenter:
    
    def __init__(self,path):
        f = open(path)
        self.V, self.E, self.R, self.C, self.X = f.readline().split(' ')
        self.V, self.E, self.R, self.C, self.X = int(self.V), int(self.E), int(self.R), int(self.C), int(self.X)
        vids = f.readline().split(' ')
        
        