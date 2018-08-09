'''
Created on 9 de ago de 2018

@author: juanpla
'''
from cassandra.cluster import Cluster

cluster = Cluster()
session = cluster.connect('aula')
result = session.execute('select * from playlist_versionada')
for mod in result:
    print(mod.modificacao)