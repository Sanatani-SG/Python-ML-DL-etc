import json

with open(r"C:\Users\Tabah\OneDrive\PROGRAMMING'\Python ∪ SQL\sample_data.json") as f:
    data=json.load(f)

##for emp in data["employees"]:
##    del emp['full_time']
print(data)

##with open("sample_newdata.json",'w') as w:
##    json.dump(data,w,indent=2)


