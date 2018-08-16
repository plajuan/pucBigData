from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client

db = GraphDatabase("http://localhost:7474", username= "neo4j")
q = 'MATCH (u1:Usuario)-[r:follows]->(u2:Usuario) WHERE u1.name="Alice" RETURN u1, type(r), u2'

result = db.query(q, returns=(client.Node, str, client.Node) )
for r in result:
    print("(%s)-[%s]->(%s)" % (r[0]["name"], r[1], r[2]["name"]) )
