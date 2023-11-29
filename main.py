from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import requests
import json
import re

hostname = "0.0.0.0"
serverPort = os.getenv("HTTP_PORT", 8080)

headers = {
  "Accept": "application/vnd.github+json",
  "X-GitHub-Api-Version": "2022-11-28"
}

# Ensure the provided username meets the GitHub username requirements
def validate_username(username):
   valid = re.compile("^[a-z\d](?:[a-z\d]|-(?=[a-z\d])){0,38}$")
   return valid.match(username) is not None

# Return a 4xx or 5xx response
def return_error(self, code, message):
  message = {
    "msg": message
  }

  self.send_response(code)
  self.send_header("Content-type", "application/json")
  self.end_headers()
  self.wfile.write(bytes(json.dumps(message), "utf-8"))

class GitHubQueryServer(BaseHTTPRequestHandler):
  def do_GET(self):
    username = re.sub("^/|/$", "", self.path)

    if not validate_username(username):
      return_error(self, 400, "Invalid username provided.")
      return

    url = f'https://api.github.com/users/{username}/gists'

    gh_response = requests.get(url, headers=headers)

    if gh_response.status_code == 404:
      # user not found
      return_error(self, 404, "User not found.")
      return
    elif gh_response.status_code == 403:
      # Authentication failed / API rate limit hit
      return_error(self, 403, "GitHub authentication error - possibly due to rate limiting.") 
    elif gh_response.status_code >= 400 and gh_response.status_code < 500:
      # client-side error
      return_error(self, 400, "Client-side error when requesting data from GitHub.")
      return
    elif gh_response.status_code >= 500:
      # server-side error (GitHub)
      return_error(self, 500, "GitHub failed to return requested data.")
      return

    gists = []

    for gist in gh_response.json():
      gist = {
          "id": gist["id"],
          "url": gist["html_url"]
      }

      gists.append(gist)
    
    response = {
      "gists": gists
    }

    self.send_response(200)
    self.send_header("Content-type", "application/json")
    self.end_headers()
    self.wfile.write(bytes(json.dumps(response), "utf-8"))

if __name__ == "__main__":        
  webServer = HTTPServer((hostname, serverPort), GitHubQueryServer)
  print("Server started http://%s:%s" % (hostname, serverPort))

  try:
    webServer.serve_forever()
  except KeyboardInterrupt:
    pass

  webServer.server_close()
  print("Server stopped.")
