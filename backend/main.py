from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/movies/{movie_id}")
def read_item(movie_id: int, q: Union[str, None] = None):
    return {"item_id": movie_id, "q": q} 

