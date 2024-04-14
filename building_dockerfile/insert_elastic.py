from elasticsearch import Elasticsearch
from api import api

def elasticSearch(movie_name):
    # Create an Elasticsearch client instance
    es = Elasticsearch(['http://0.0.0.0:9200'])  # Replace 'localhost:9200' with your Elasticsearch server address

    # Define the search query
    search_query = {
        "query": {
            "match": {
                "Series_Title": movie_name  # Example search term
            }
        }
    }

    # Perform the search
    search_results = es.search(index="movies", body=search_query)

    # Check if there are any search results
    if search_results['hits']['total']['value'] > 0:
        # Save the Poster_Link of the first document
        poster_link = search_results['hits']['hits'][0]['_source']['Released_Year']
        print("Poster Link:", poster_link)
        return poster_link
    else:
        print("No documents found matching the search criteria.")
        return "invalid"

