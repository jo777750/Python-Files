import pymongo


myclient = pymongo.MongoClient("mongodb+srv://m220student:m220password@mflix.4ul9r.mongodb.net/admin?retryWrites=true&w=majority")
db = myclient.test


'''
mongodump --uri "mongodb+srv://<your username>:<your password>@<your cluster>.mongodb.net/sample_supplies"

myclient = pymongo.MongoClient("mongodb+srv://m220student:m220password@mflix.4ul9r.mongodb.net/mflix?retryWrites=true&w=majority")

m220=myclient.m220


{"start station name" : "Howard St & Centre St", "birth year" : 1961}
{"start station name" : "Howard St & Centre St", "birth year" : 1961}
movies=m220.movies
movies.find_one()
'''