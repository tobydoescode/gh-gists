import unittest
from unittest import TestCase
import requests

class IntegrationTests(TestCase):
  def test_valid_username(self):
    result = requests.get("http://localhost:8080/octocat")
    gists = result.json()["gists"]
    assert result.status_code == 200 and len(gists) == 8

  def test_user_does_not_exist(self):
    result = requests.get("http://localhost:8080/hdgfhsjdkfjdhfjgkdhshgfjg")
    assert result.status_code == 404
  
  def test_invalid_username(self):
    result = requests.get("http://localhost:8080/--invalid--user--name--")
    assert result.status_code == 400

if __name__ == "__main__":
    unittest.main()
