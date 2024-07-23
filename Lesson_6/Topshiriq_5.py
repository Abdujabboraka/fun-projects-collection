d = {
    "users":[
        {"name":"Olim","score":10},
        {"name":"Sobir","score":80},
        {"name":"Xamdam","score":20},
        {"name":"Sherzod","score":60},
        {"name":"Sardor","score":30},
    ]
     }

def default():
    for i in d["users"]:
        i["score"] = 0
        print(i)
default()