'''
Created on 9 de ago de 2018

@author: juanpla
'''
from cassandra.cluster import Cluster

cluster = Cluster()
session = cluster.connect('aula')
session.execute("""
    INSERT INTO users(
    id,
    lastname,
    age,
    city,
    email,
    firstname
    ) VALUES (uuid(), 'Jones', '35', 'Austin', 'jones@test.com', 'Bob');
"""
)
result = session.execute("select * from users where lastname ='Jones' ALLOW FILTERING")[0]

print(result.age, result.lastname)
