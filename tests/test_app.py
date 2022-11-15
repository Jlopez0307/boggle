from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!
    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_boggle_homepage(self):
        with self.client:
            response = self.client.get('/')
            self.assertIn('game_board', session)
    
    def test_valid_word(self):
        with self.client as client:
            with client.session_transaction() as sess:
                sess['game_board'] = [["t", "e", "s", "t"],
                                      ["t", "e", "s", "t"],
                                      ["t", "e", "s", "t"],
                                      ["t", "e", "s", "t"],
                                      ["t", "e", "s", "t"]]
        response = self.client.get('/guess?word=test')
        print(response)

