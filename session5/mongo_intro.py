from pymongo import MongoClient

client = MongoClient()

database = client.get_database('D4E16')

quiz_collection = database.get_collection('quizzes')
from bson import ObjectId  

data = quizzes = [ # collection 
    {
        'question': 'con chó có mấy chân?',
        'choices': [
            '1 chân', 
            '2 chân', 
            '9 chân', 
            '4 chân',
        ],
        'rightChoice': 3
    },
    {
        'question': 'con thỏ có mấy chân?',
        'choices': [
            '1 chân',
            '2 chân',
            '9 chân',
            '4 chân',
        ],
        'rightChoice': 1
    },
    {
        'question': 'con vịt có mấy chân?',
        'choices': [
            '1 chân',
            '3 chân',
            '9 chân',
            '2 chân',
        ],
    }
]

#CREATE
#quiz_collection.insert_one(data) # (data=dict)
quiz_collection.insert_many(data) #phải chuyển dữ liệu thành 1 list (data=list)

#READ
quizzes = list(quiz_collection.find()) #find.all
print(quizzes)
for quiz in quizzes:
    print(quiz)

query = {'_id': ObjectId("5f845baa6200975db3f7e8ad")}
update = {
    '$set': {
        'updated': 999999999
    }
}
#quiz = list(quiz_collection.find(query))
#print(quiz)
#quiz = quiz_collection.find({'updated': 999999999})
#quiz_collection.find_one_and_update(query, update)
#print(quiz)
#quiz_collection.find_one_and_update(query, update)

quiz_collection.delete_one(query)