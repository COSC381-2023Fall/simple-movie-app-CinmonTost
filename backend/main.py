from typing import Union
from query import searchMovieId
from query import replaceMovie
from query import deleteMovie
from query import addMovie
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class ReqBody(BaseModel):
    movie_name: [str] = None
    movie_cast: [str] = None

@app.get("/movies/{movie_id}")
def read_item(movie_id: int):
    return searchMovieId(movie_id)

@app.put("/movies/{movie_id}")
def read_item(movie_id: int, replaceMovie: ReqBody):
    return replaceMovie(movie_id, replaceMovie.dict(exclude_unset=True))

@app.delete("/movies/{movie_id}")
def read_item(movie_id: int):
    return replaceMovie(movie_id)

@app.post("/movies/{add}")
def read_item(addMovie: ReqBody):
    return addMovie(addMovie.dict(exclude_unset=True))