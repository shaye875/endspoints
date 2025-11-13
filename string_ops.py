from fastapi import FastAPI
from classitem import *
# import uvicorn
import json
app = FastAPI()

@app.get("/reverse")
def reverse(text:str):
     dict = {}
     dict["original"] = text
     dict["revers_string"] = text[::-1]
     str = json.dumps(dict)
     return str

@app.get("/uppercase/{text}")
def to_upper(text: str):
    return {"original":text,"uppercased":text.upper()}

@app.post("/remove-vowels")
def remove_vowels(item:Item) -> str:
        str1 = ""
        for s in item.text:
            if s not in ["a","e","i","o","u"]:
                str1+=s
        dict = str({ "original":item.text, "without_vowels":str1 })
        return dict

@app.post("/remove-every-third")
def remove_every_third(item:Item) ->dict:
    str1 = ""
    for i in range(len(item.text)):
        if (i+1) % 3 != 0:
            str1+=item.text[i]
    return { "original":item.text,"result": str1}

@app.post("/letter-counts")
def letter_counts_map(item:Item) -> dict:
    dict = {}
    list = []
    for s in item.text:
        if s not in list:
            list.append(s)
            dict[s] = 1
        else:
            dict[s]+=1
    with open('data/letter_counts.json','w') as f:
        dict1 = json.dumps(dict)
        f.write(dict1)
    return {"original":item.text,"counts":dict,"save to":"data/letter_counts.json"}

