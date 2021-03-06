import requests as web
from requests.auth import HTTPBasicAuth
import base64, datetime

class Spotify():

    def __init__(
        self, 
        client_id: str,
        client_secret: str,
        api_url : str = 'https://api.spotify.com/v1',
        token_url : str = 'https://accounts.spotify.com/api/token'

    ) -> None:

        # Public properties
        self.client_id = client_id
        self.client_secret = client_secret
        self.api_url = api_url
        self.token_url = token_url

        # Private properties
        self._token = None
        self._token_expires_in = None
        self._token_type = None
        self._token_access_time = None

        # Run authentication when class is init
        self.__authenticate()

    def __create_client_cred(self) -> dict:
        
        client_creds = f'{self.client_id}:{self.client_secret}'
        client_creds_b64 = base64.b64encode(client_creds.encode())

        data = {'grant_type': 'client_credentials'}
        headers = {'Authorization': f'Basic {client_creds_b64.decode()}'}

        return {'data': data, 'headers': headers}

    def __authenticate(self) -> None:

        cred = self.__create_client_cred()   

        res = web.post(self.token_url, data = cred['data'], headers = cred['headers'])
        if not self.__is_valid_data(res):
            raise Exception('Spotify Authentication Failed!')

        json_data = res.json()

        self._token = json_data['access_token']
        self._token_expires_in = json_data['expires_in']
        self._token_type = json_data['token_type']
        self._token_access_time = datetime.datetime.now()


    def __form_endpoint_from_params(self,base: str, params: list) -> str:
    
        query = ''
        for param in params:
            query = query + '/' + param

        return f'{base}{query}'

    def __create_request_headers(self):

        return {'Authorization': f'Bearer {self._token}'}

    def __is_valid_data(self,response):
        
        if response.status_code == 200:
            return True

        return False
    
    def get_genres_by_artist(self, artist: str) -> list:

        endpoint = self.__form_endpoint_from_params(self.api_url, ['search'])

        # Form query parameters by artist
        payload = {'q': artist, 'type': 'artist', 'limit': '50'}

        res = web.get(endpoint, headers = self.__create_request_headers(), params = payload)

        if self.__is_valid_data(res):
            data = res.json()
            artist_data = data['artists']['items']
            for data in artist_data:
                try:
                    found_artist_name = data['name']
                    if found_artist_name == artist:
                        genres = data['genres']
                        if not genres:
                            print(f'Artist {found_artist_name} was found on spotify, but no record of genres for {found_artist_name}')
                            return None

                        return genres
                except:
                    return None

        return None


    def get_genres_by_album(self, album: str) -> list:

        endpoint = self.__form_endpoint_from_params(self.api_url, ['search'])

        # Form query parameters by artist
        payload = {'q': album, 'type': 'album', 'limit': '50'}

        res = web.get(endpoint, headers = self.__create_request_headers(), params = payload)

        if self.__is_valid_data(res):
            data = res.json()
            album_data = data['albums']['items']
            for data in album_data:
                try:
                    found_album_name = data['name']
                    if found_album_name == album:
                        id = data['id']
                        genres = self.get_genres_from_album_id(id)

                        if not genres:
                            print(f'Album {found_album_name} was found on spotify, but no record of genres for {found_album_name}')
                            # Back up, find albums artist and see if they have genres
                            return self.get_genres_by_artist_2(data['artists'][0]['name'])
                            
                        return genres
                except:
                    return None

        return None

    def get_genres_from_album_id(self,id: str):

        endpoint = self.__form_endpoint_from_params(self.api_url, ['albums', id])

        res = web.get(endpoint, headers = self.__create_request_headers())

        if self.__is_valid_data(res):

            # Albums don't return genres, need to do another request to get them
            data = res.json()
            return data['genres']

        return None

    def get_genres_from_keywords(self,keywords):

        genres = self.get_genres_by_artist(keywords)

        if not genres:
            genres = self.get_genres_by_album(keywords)

        return genres

