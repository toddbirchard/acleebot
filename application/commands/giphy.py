import requests
from random import randint
from config import Config


def random_giphy_image(searchTerm):
    """Get a random image from Giphy."""
    rand = randint(0, 20)
    params = {'api_key': Config.giphy_api_key,
              'q': searchTerm,
              'limit': 1,
              'offset': rand,
              'rating': 'R',
              'lang': 'en'}
    res = requests.get('https://api.giphy.com/v1/gifs/search', params=params)
    if len(res.json()['data']):
        image = res.json()['data'][0]['images']['original']['url']
        return image
    else:
        # logger.warn(f"Giphy search term {searchTerm} returned no results.")
        return 'image not found :('