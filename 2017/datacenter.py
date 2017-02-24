# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 17:57:35 2017

@author: Thomas
"""

import video
import endPoint
import cache
import request


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

        self.videos = sorted(self.videos, key = lambda v: v.size/(v.req+1))
        
        for e in self.endPoints:
            e.savingLat()
            
        for e in self.endPoints:
            for c in e.list:
                while (c[0].capacity >= c[0].size + self.videos[0].size):
                    if (self.videos[0].req != 0):
                        c[0].addVideo(self.videos.pop(0))
                    else:
                        self.videos.pop(0)
        
        f.close()
        
        
    def out(self,outp):
        f = open(outp,'w')
        acc=0
        for c in self.caches:
            if(c.size > 0):
                acc+=1
        f.write(str(acc)+'\n')
        for i in range(len(self.caches)):
            if (self.caches[i].size > 0):
                f.write(str(i))
                for v in self.caches[i].list:
                    f.write(' '+str(v.ident))
                f.write('\n')
        f.close()