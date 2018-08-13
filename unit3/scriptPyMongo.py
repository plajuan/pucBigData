import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client.aula

albuns = db.albuns.find()

file = open("c:\\data\\albuns.txt", "a")

for item in albuns:
    try:
        nome = item["nome"]
        file.write(nome + '\n')
    except:
        print("atributo sem nome")

file.close()
