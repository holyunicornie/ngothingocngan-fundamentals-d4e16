person = {
    "name": "Ngân", 
    "yob": 1999,
    "home" : "Bắc Ninh",
    "bmi": {
        "weight": 50,
        "height": 155
        }
    }
 
  #key: valuve (khai báo dictionary (cặp key value)
#nếu key value có 2 (hay nh) key trùng nhau thì lấy cái mới nhất (update)
person["hair"] = "short" #CREATE
person["bmi"]["weight"] = 55 #UPDATE
print(person["name"])    #print(person["name"] [index]) (name list)
name = person["home"]
for key in person:
    print(key, person[key])
weight = person["bmi"] ["weight"]
del person["bmi"] #delete
print(person)
print("relationship" in person)


