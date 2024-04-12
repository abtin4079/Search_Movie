from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import redis
import uvicorn 
from elasticsearch import Elasticsearch
import json
from insert_elastic import elasticSearch
from api import api

app = FastAPI(title= "film recommender")

# Connect to Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

# Connect to elasticsearch
elastic_client = Elasticsearch(['https://localhost:9200'])

class SearchRequest(BaseModel):
    query: str

@app.on_event("startup")
async def startup():
    pass


@app.on_event("shutdown")
async def shutdown():
    pass

@app.get('/')
async def up():
    return f"Hey!"


@app.post("/search/")
async def search(search_request: SearchRequest):
    try:

        #insert json to elastic
        


        # Define endpoints    
        API_ENDPOINT = 'https://imdb-top-100-movies.p.rapidapi.com/search'

        #redis_client.set("mame", "memento")

        # Send search query to Redis
        print(search_request.query)
        response_body = redis_client.get(search_request.query)
        print(response_body)
        if response_body is not None:
            print("Response body found in Redis:", response_body)
            return 0

        # search through the elastic
        poster_link = elasticSearch(search_request.query)

        if (poster_link != 0):
            redis_client.set( search_request.query, poster_link)
            print("We successfully set these film name from elastic: ")

        #search through the api
        api_link = api(search_request.query)
        if(api_link != "invalid"):
            redis_client.set( search_request.query, api_link)
            print("We successfully set these film name from api: ")
        else:
            print("there is no matching film in this API! ")

    except Exception as e:
        # Log the exception or handle it as needed
        return {"error": str(e)}


if __name__ == '__main__':
    uvicorn.run("main:app", host='localhost', port=8000, reload=True)