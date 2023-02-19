# Spotify Integration

## Overview

The Spotify integration allows you to query the Spotify API for information about artists, albums, tracks, and playlists.
For now the integration is supported by an app in developer mode which involves quota limit.

For all use please ensure you have the following secrets in your environment:

* CLIENT_ID = <>
* CLIENT_SECRET= <>

### Spotify Recommender

* Provide `playlist_recommendation()` genre list specifcied in the format of `genre1,genre2,genre3` to get a list of recommended tracks based on the genres. 
Additionally `limit`controls the number of tracks returned.
* The function returns a dataframe with the name, external url and preview url of the track.
