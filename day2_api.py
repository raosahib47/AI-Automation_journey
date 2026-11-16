import urllib.request
import json

print("Loading Data.............")

url = "https://jsonplaceholder.typicode.com/users/1"

try:
    response = urllib.request.urlopen(url)

    raw_data = response.read().decode("utf-8")

    data = json.loads(raw_data)

    print("\n =====Data Available=====")
    print("User_name =",data["name"])
    print("User_email =",data["email"])
    print("User_city =",data["address"]["city"])

except Exception as e:
    print("error :",e)