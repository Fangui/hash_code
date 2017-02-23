# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 17:57:35 2017

@author: Thomas
"""

import video
import endPoint
import cache
import request

def tricaca(l):
    L = [[]]*(l[-1].size)
    for v in l:
        L[v.size - 1].append(v)
    for i in range(len(L)):
        L[i] = sorted(L[i], key = lambda v : v.req)
    R=[]
    for vl in L:
        for v in vl:
            R.append(v)
    return R

class datacenter:
    
    def __init__(self,path):
        f = open(path)
        self.V, self.E, self.R, self.C, self.X = f.readline().split(' ')
        self.V, self.E, self.R, self.C, self.X = int(self.V), int(self.E), int(self.R), int(self.C), int(self.X)
        self.videos = []
        self.vidreq = [(0,0)]*self.V  # (id vid, nbreq)
        self.endPoints = []
        self.requests = []
        
        self.caches = []        
        for i in range(self.C):
            self.caches.append(cache.cache(self.X))            

        vi = f.readline().split(' ')        
        for i in range(len(vi)):
            self.videos.append(video.video(int(vi[i]), i, 0))
            
        for i in range(self.E):
            Ld,K = f.readline().split(' ')
            Ld,K = int(Ld),int(K)            
            e = endPoint.endPoint(Ld)
            
            for j in range(K):
                c,Lc = f.readline().split(' ')
                e.addCacheLat(self.caches[int(c)],int(Lc))
            self.endPoints.append(e)
            
        for i in range(self.R):
            Rv,Re,Rn = f.readline().split(' ')
            self.requests.append( request.request(int(Rv),int(Re),int(Rn)) )
            
        for r in self.requests:
            self.videos[r.idVid].req += r.nbCall

        self.videos = sorted(self.videos, key = lambda v: v.size/v.req)
        #self.videos = tricaca(self.videos)