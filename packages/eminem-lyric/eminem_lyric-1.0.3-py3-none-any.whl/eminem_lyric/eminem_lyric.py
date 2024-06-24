import requests
from requests.exceptions import HTTPError, RequestException


class EminemLyric:
    """
    A class for fetching and retrieving lyrics of Eminem songs from an external API.

    This class provides a convenient interface for users to fetch and access lyrics of Eminem songs
    using an external lyrics API. It offers methods to retrieve both processed lyrics and raw lyrics
    data, allowing users flexibility in accessing the lyrics.

    Methods:
    - __init__(song_title: str): Initializes an EminemLyric object with the specified song title.
    - lyric (property): Property to fetch and return the processed lyric of the specified song.
    - lyric_raw (property): Property to fetch and return the raw lyric data from the API.

    Raises:
    - TypeError: If the song title is not a string.
    - ValueError: If the song title is empty.
    - Exception: If the song is not found in the API response or if there is an error fetching the lyric.

    Examples of Use:
    >>> lyric_object = EminemLyric("Lose Yourself")
    >>> print(lyric_object.lyric)
    "Look, if you had one shot, or one opportunity..."

    >>> print(lyric_object.lyric_raw)
    {"lyrics": "Look, if you had one shot, or one opportunity..."}
    """
    _source = "https://api.lyrics.ovh/v1/eminem/"  # API source URL

    def __init__(self, song_title: str) -> None:
        """
        Initializes an EminemLyric object with the specified song title.

        Parameters:
        - song_title (str): The title of the Eminem song.
        """
        self.song = song_title  # Calls the setter method

    def __str__(self) -> str:
        """
        Returns a string representation of the EminemLyric object.

        Returns:
        - str: A string representation of the EminemLyric object.
        """
        return f"{self.__class__.__name__}(song='{self.song}')"

    @property
    def song(self) -> str:
        """
        Getter for the song title.

        Returns:
        - str: The title of the Eminem song.
        """
        return self._song

    @song.setter
    def song(self, value: str) -> None:
        """
        Setter for the song title.

        Parameters:
        - value (str): The title of the Eminem song.

        Raises:
        - TypeError: If the song title is not a string.
        - ValueError: If the song title is empty.
        """
        if not isinstance(value, str):
            raise TypeError("Invalid Song Title.")
        elif value.strip() == "":
            raise ValueError("Empty Song Title.")
        else:
            self._song = value.lower()  # Convert to lowercase for consistency

    @property
    def lyric(self) -> str:
        """
        Property to fetch and return the lyric of the specified song.

        Returns:
        - str: The lyric of the specified Eminem song.
        """
        return self._fetch_lyric()

    @property
    def lyric_raw(self) -> str:
        """
        Property to fetch and return the raw lyric data from the API.

        Returns:
        - str: The raw lyric data from the API.
        """
        return self._fetch_lyric_raw()

    def _fetch_lyric(self) -> str:
        """
        Fetches and returns the lyric of the specified song.

        Returns:
        - str: The lyric of the specified Eminem song.
        """
        data = self._fetch_lyric_raw()
        return data['lyrics']

    def _fetch_lyric_raw(self) -> dict:
        """
        Fetches and returns the lyric data from the API.

        Returns:
        - dict: The lyric data from the API.

        Raises:
        - Exception: If the song is not found in the API response or if there is an error fetching the lyric.
        """
        try:
            with requests.get(self._source + self._song) as response:
                response.raise_for_status()
                data = response.json()
                return data
        except HTTPError as http_error:
            if http_error.response.status_code == 404:
                raise Exception("No lyrics found for the requested song.")
            else:
                raise Exception(f"HTTP Error: {http_error}")
        except RequestException as request_exception:
            raise Exception(f"Request Error: {request_exception}")
        except Exception as e:
            raise Exception(f"Unexpected Error: {e}")
