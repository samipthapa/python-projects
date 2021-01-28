import requests
import base64
import webbrowser
import json

client_id = 'dc7aa202a6f24a48a4ddafeb2d043811'
client_secret = '5a925e617ac3478ea8da486a61ce9258'

# Authorize

auth_url = "https://accounts.spotify.com/authorize"

auth_parameters = {
    'client_id': client_id,
    'response_type': 'code',
    "redirect_uri": "https://www.spotify.com/us/",
    "scope": "user-top-read"
}

auth_response = requests.get(auth_url, params=auth_parameters)

auth_code_url = None
if auth_code_url is None:
    webbrowser.open_new(auth_response.url)

# Access Code

else:
    i = auth_code_url.find('code') + 5
    auth_code = auth_code_url[i:]

    access_token_url = "https://accounts.spotify.com/api/token"
    
    client_creds = f'{client_id}:{client_secret}'
    client_creds_bytes = client_creds.encode()
    b64 = base64.b64encode(client_creds_bytes)

    access_token_data = {
        "grant_type": "authorization_code",
        "code": auth_code,
        "redirect_uri": "https://www.spotify.com/us/"
    }

    access_token_headers = {
        "Authorization": f"Basic {b64.decode()}"
    }

    try:
        with open('token.json', 'r') as f:
            read_data = json.load(f)
        refresh_token = read_data.get('refresh_token')
        exchange_url = 'https://accounts.spotify.com/api/token'
        exchange_payload = {
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token
        }
        exchange_header = {
            "Authorization": f"Basic {b64.decode()}"
        }
        exchange_response = requests.post(exchange_url, data=exchange_payload, headers=exchange_header)
        access_token = exchange_response.json().get('access_token')
            
    except FileNotFoundError:
        response = requests.post(access_token_url, data=access_token_data, headers=access_token_headers)
        write_data = response.json()
        access_token = write_data.get('access_token')
        with open('token.json', 'w') as f:
            json.dump(write_data, f, indent=2)

    # Top Tracks

    top_tracks = "https://api.spotify.com/v1/me/top/tracks"
    track_payload = {
        "limit": 10,
        'time_range': 'long_term'
    }
    track_headers = {
        "Authorization": f"Bearer {access_token}"
    }
    tracks_response = requests.get(top_tracks, params=track_payload, headers=track_headers)
    data = tracks_response.json()

    print("----USER'S TOP TRACKS----\n")
    for i in range(len(data['items'])):
        name = data['items'][i].get('name')
        artist = data['items'][i]['artists'][0].get('name')
        print(f'{i+1}. {name} - {artist}')

    #Top artists

    artist_url = "https://api.spotify.com/v1/me/top/artists"
    artist_payload = {
        "limit": 10,
        "time_range": "long_term"
    }
    artist_headers = {
        "Authorization": f'Bearer {access_token}'
    }
    artist_response = requests.get(artist_url, params=artist_payload, headers=artist_headers)
    artist_data = artist_response.json()

    print("\n----USER'S TOP ARTISTS----\n")
    for i in range(len(artist_data['items'])):
        artist_name = artist_data['items'][i].get('name')
        print(f'{i+1}. {artist_name}')
