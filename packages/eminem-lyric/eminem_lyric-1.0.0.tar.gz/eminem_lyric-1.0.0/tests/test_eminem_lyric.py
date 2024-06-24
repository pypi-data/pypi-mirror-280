import unittest
from eminem_lyric import EminemLyric
from requests.exceptions import RequestException


class TestEminemLyric(unittest.TestCase):
    def test_song_title_lowercase(self):
        # Test whether the song title is converted to lowercase
        lyric_object = EminemLyric(song_title='LOSE YOURSELF')
        self.assertEqual(lyric_object.song, 'lose yourself')

    def test_empty_song_title(self):
        # Test whether an empty song title raises a ValueError
        with self.assertRaises(ValueError):
            EminemLyric(song_title='')

    def test_non_string_song_title(self):
        # Test whether a non-string song title raises a TypeError
        with self.assertRaises(TypeError):
            EminemLyric(song_title=123)

    def test_song_not_found(self):
        # Test whether fetching lyrics for a non-existent song raises an exception
        lyric_object = EminemLyric(song_title='NonExistentSong')
        with self.assertRaises(Exception) as context:
            _ = lyric_object.lyric
        self.assertTrue("No lyrics found" in str(context.exception))

    def test_lyrics_not_empty(self):
        # Test whether lyrics for a valid song title are not empty
        lyric_object = EminemLyric(song_title='Lose Yourself')
        lyrics = lyric_object.lyric
        self.assertTrue(lyrics)  # Assert that lyrics is not empty
