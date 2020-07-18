from flask import Flask, jsonify, abort, make_response, request
from app import app
import unittest
import os
import subprocess
import time
import socket
import json

# test functionality using curl
class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_players(self):
        response = self.app.get("http://localhost:5000/api/v1/players/get")
        self.assertEqual(response.status_code, 200)

    def test_get_tournaments(self):
        response = self.app.get("http://localhost:5000/api/v1/tournaments/get")
        self.assertEqual(response.status_code, 200)

    def test_get_draw(self):
        response = self.app.get("http://localhost:5000/api/v1/draws/get")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()