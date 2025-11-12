from fastapi import FastAPI
# from pydantic import BaseModel
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


def reverse_str(s: str) -> str:
    pass

def remove_vowels(s: str) -> str:
    pass

def remove_every_third(s: str) -> tuple[str, list[int], list[str]]:
    pass

def letter_counts_map(s: str) -> dict[str, int]:
    pass
