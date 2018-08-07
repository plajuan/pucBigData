import redis
from random import randint

C1 = "candidato1"
C2 = "candidato2"

r = redis.StrictRedis(host = 'localhost', port=6379, charset="utf-8", decode_responses=True)
r.flushdb()

r.set(C1, 0)
r.set(C2, 0)

for i in range(100):
	cand = "candidato" + str(randint(1,2))
	r.incr(cand)
	
res1 = r.get(C1)
res2 = r.get(C2)

if res1 > res2:
	print(C1 + " venceu com " + str(res1) + " votos.")
elif res1 < res2:
	print(C2 + " venceu com " + str(res2) + " votos.")
else:
	print("votação empatada!")
