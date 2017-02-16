# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

class Pool:
    """
    servers : liste des serveurs appartenant a cette pool
    capacity : capacite totale des serveurs
    """
    def __init__(self, name, servers = [], capacity = 0):
        self.name = name
        self.servers = servers
        self.max_capacity = capacity

def add_server(pool, server):
    pool.servers.append(server)
    pool.max_capacity += server.capacity

def remove_server(pool, server):
    pool.servers.remove(server)
    pool.max_capacity -= server.capacity
