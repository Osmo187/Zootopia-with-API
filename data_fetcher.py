import requests

API_KEY = "xH5LWyd1QPVUqSbu45PmXhAawnj5UJPsHPNz7S8S"
API_URL = "https://api.api-ninjas.com/v1/animals"


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
      'name': ...,
      'taxonomy': { ... },
      'locations': [ ... ],
      'characteristics': { ... }
    }
    """
    response = requests.get(
        API_URL,
        params={"name": animal_name},
        headers={"X-Api-Key": API_KEY}
    )
    return response.json()