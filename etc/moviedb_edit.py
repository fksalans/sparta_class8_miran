from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta 

movie = db.movies.find_one({'title':'매트릭스'})
print(movie['star'])

#same_star = list(db.movies.find({'star':'9.39'}))
#for movie in same_star:
#    print (movie['title'])

db.movies.update_many({'star':'9.39'},{'$set':{'star':'0'}})


