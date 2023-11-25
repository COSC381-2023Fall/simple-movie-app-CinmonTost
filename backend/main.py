from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/movies/{movie_id}")
def read_item(movie_id: int, q: Union[str, None] = None):
    return {"movie_id": movie_id, "q": q}


@app.put("/movies/{movie_id}")
def read_item(movie_id: int, q: Union[str, None] = None):
    return {"movie_id": movie_id, "q": q}