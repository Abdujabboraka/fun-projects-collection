d ,success,fail = {
    "users":[
        {"name":"Olim","score":10},
        {"name":"Sobir","score":80},
        {"name":"Xamdam","score":20},
        {"name":"Sherzod","score":60},
        {"name":"Sardor","score":30},
    ]
     }, [], []
def final():
    for i in d["users"]:
        if i["score"] > 50:
            success.append(i)
        else:
            fail.append(i)
    print(f"succes\n{success}\nfail\n{fail}")
print(final())