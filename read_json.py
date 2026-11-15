import json

with open('day1.json','r') as file:
    data = json.load(file)
print("Name =",data["name"])
print("Age =",data["age"])
print("city =",data["city"])
print("skills =",data["skills"])