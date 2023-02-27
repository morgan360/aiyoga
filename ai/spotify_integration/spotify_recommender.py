import requests
from django.conf import settings
import pandas as pd

CLIENT_ID = getattr(settings, "CLIENT_ID", None)
CLIENT_SECRET = getattr(settings, "CLIENT_SECRET", None)

BASE_URL = "https://api.spotify.com/v1/"


def authentication():
    AUTH_URL = "https://accounts.spotify.com/api/token"

    # POST
    auth_response = requests.post(
        AUTH_URL,
        {
            "grant_type": "client_credentials",
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
        },
    )

    # convert the response to JSON
    auth_response_data = auth_response.json()

    # return the headers with access token
    return {
        "Authorization": "Bearer {token}".format(
            token=auth_response_data["access_token"]
        )
    }


def playlist_recommendation(genre: str, limit: int = 20) -> pd.DataFrame:
    """
    Returns recommended tracks (number specified with limit) based on a genre.
    Returns a dataframe with the name, external url and preview url of the track.
    """
    headers = authentication()
    r = requests.get(
        BASE_URL + "recommendations/",
        headers=headers,
        params={"seed_genres": genre, "max_energy": 0.1, "limit": limit},
    )
    spotify_response = pd.DataFrame(r.json()["tracks"])
    return spotify_response[["name", "external_urls", "preview_url"]]
