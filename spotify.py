import spotipy
import json
import webbrowser

username = 'elmejor-95-95'
clientID = 'ad8a04c76b2f429b9da4cc2a7a3d3f95'
clientSecret = 'ecc4c22c36294ff3b90a116da19d920b'
redirectURI = 'http://google.fr/'

oauth_object = spotipy.SpotifyOAuth(clientID,clientSecret,redirectURI)
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotifyObject = spotipy.Spotify(auth=token)

user = spotifyObject.current_user()
print(json.dumps(user,sort_keys=True, indent=4))

