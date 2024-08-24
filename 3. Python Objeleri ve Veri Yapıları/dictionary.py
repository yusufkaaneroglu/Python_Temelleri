# sehirler=["kocaeli", "istanbul"]
# plakalar=[41, 34] 

# print(plakalar[sehirler.index("istanbul")])

# #print(plakalar["kocaeli"]) => 41
# #print(plakalar["istanbul"]) => 34

# plakalar = { "kocaeli" : 41, "istanbul" : 34 }

# print(plakalar["kocaeli"])
# print(plakalar["istanbul"])

# plakalar["ankara"] = 6
# plakalar["kocaeli"] ="new value"
users = {
    "Sadikturan": {  
        "age": 36, 
        "email": "sadik@gmail.com",
        "adress": "kocaeli",
        "phone": "1231321"      
    },
        "cinarturan": {  
        "age": 2, 
        "roles": ["admin","user"],
        'email': "cinar@gmail.com",
        "adress": "kocaeli",
        "phone": "1231321"      
    }
}

# print(users["cinarturan"]["age"])
# print(users["cinarturan"]["email"])
# print(users["cinarturan"]["adress"])
print(users["cinarturan"]["roles"])

