from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn
import json
app = FastAPI()

@app.get("/revers/{text}")
def reverse(text:str)->str:
    dict = {}
    dict["original"] = text
    dict["revers_string"] = text[::-1]
    return dict

def reverse_str(s: str) -> str:
    pass

def remove_vowels(s: str) -> str:
    pass

def remove_every_third(s: str) -> tuple[str, list[int], list[str]]:
    pass

def letter_counts_map(s: str) -> dict[str, int]:
    pass
