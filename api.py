import requests


def api(movie_name):
    url = f"https://imdb-search2.p.rapidapi.com/{movie_name}"

    headers = {
        "X-RapidAPI-Key": "0e566a50abmshcbb2f7203fd11b5p14de52jsn691d435af501",
        "X-RapidAPI-Host": "imdb-search2.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if (response.status_code == 404):
        print("there is no valid film with your request!")
        return "invalid"

    if (response.status_code == 200):  
        api_url = response.json()['description'][0]['#IMG_POSTER']
        print(api_url)
        return api_url

    
