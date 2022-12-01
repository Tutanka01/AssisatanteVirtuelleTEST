import spotipy
import json
import webbrowser

username = 'secret'
clientID = 'secret'
clientSecret = 'secret'
redirectURI = 'http://google.fr/'

oauth_object = spotipy.SpotifyOAuth(clientID,clientSecret,redirectURI)
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotifyObject = spotipy.Spotify(auth=token)

user = spotifyObject.current_user()
print(json.dumps(user,sort_keys=True, indent=4))

