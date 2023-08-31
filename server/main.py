from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import base62
from urllib.parse import urlparse
import os
from datetime import datetime

# I didn't write this
import threading
import time

timestd = "%m:%d:%y:%H:%M:%S:%f"


class RepeatedTimer(object):

  def __init__(self, interval, function, *args, **kwargs):
    self._timer = None
    self.interval = interval
    self.function = function
    self.args = args
    self.kwargs = kwargs
    self.is_running = False
    self.next_call = time.time()
    self.start()

  def _run(self):
    self.is_running = False
    self.start()
    self.function(*self.args, **self.kwargs)

  def start(self):
    if not self.is_running:
      self.next_call += self.interval
      self._timer = threading.Timer(self.next_call - time.time(), self._run)
      self._timer.start()
      self.is_running = True

  def stop(self):
    self._timer.cancel()
    self.is_running = False


# End unoriginal code

hostName = "glitchtech.top"
serverPort = 8


def in_index(mylist, target):
  for i in mylist:
    if i == target:
      return True
  return False


def de(input_str):
  return base62.decodebytes(input_str).decode("utf-8")


def jwrite(file, out_json):
  outfile = open(file, "w")
  json.dump(out_json, outfile, indent=2)
  outfile.close()


def jload(file):
  jfile = open(file)
  jdict = json.load(jfile)
  jfile.close()
  return jdict


def get_query(query):
  keys = []
  values = []
  for qc in query.split("&"):
    pair = qc.split("=")
    keys.append(pair[0])
    values.append(pair[1])
  return dict(zip(keys, values))


def time2string(time):
  return time.strftime(timestd)


def get_time():
  return datetime.now()


def clean_time(time):
  return time[0:17:1]


def string2time(string):
  return time.strptime(string, timestd)


def cleaner():
  users = jload("users.json")
  for user in users:
    alive = user["keepalive"]
    dif = get_time() - string2time(alive)
    print(time2string(get_time()))
    print(dif.count_seconds())


def login(username, password):
  logins = jload("creds.json")
  ret = {"res": 0, "name": "noname"}
  if username in logins['users']:
    ret["res"] = 1
    if password == logins['users'][username]['Password']:
      ret["name"] = logins['users'][username]['Name']
      ret["res"] = 2
      if logins['users'][username]['Admin']:
        ret["res"] = 3
  return ret


class ChessServer(BaseHTTPRequestHandler):

  def do_GET(self):
    p = self.path.split("?")[0]
    # Refer to p[0] for get path
    query = urlparse(self.path).query
    query_components = {}
    if len(query) > 0:
      query_components = get_query(query)
    self.send_response(200)
    self.send_header("Content-type", "text/json")
    self.end_headers()

    if p == "/connect":
      # Result 0: Username already in use
      # Result 1: Connected

      #username = de(query_components["username"])
      username = query_components["username"]
      userjson = jload("users.json")
      res = {"result": 0}
      # Number activities are hardcoded as follows
      # 0 = Logged in
      # Interpret strings as chat room signatures
      if not {"name": username} in userjson:
        blank = {"name": username, "keepalive": get_time(), "activity": "0"}
        userjson.append(blank)
        jwrite("users.json", userjson)
        res["result"] = 1
      self.wfile.write(bytes(json.dumps(res), "utf-8"))

    if p == "/users":
      self.wfile.write(bytes(json.dumps(jload("users.json")), "utf-8"))

    if p == "/time":
      self.wfile.write(bytes(json.dumps({"result": get_time()}), "utf-8"))

    if p == "/keepalive":
      self.wfile.write(bytes(json.dumps({"result": ":c"}), "utf-8"))

  def do_POST(self):
    content_length = int(self.headers['Content-Length'])
    post_data = self.rfile.read(content_length)
    # POST requests requiring decode should be put here
    decode = []
    if in_index(decode, self.path):
      query = post_data.decode("utf-8")
      query_components = {}
      if len(query) > 0:
        query_components = get_query(query)
    self.send_response(200)
    self.send_header("Content-type", "text/json")
    self.end_headers()
    if self.path == "/addpost":
      handle_image(post_data)
      self.wfile.write(bytes(json.dumps({"success": 1}), "utf-8"))


if __name__ == "__main__":
  webServer = HTTPServer((hostName, serverPort), ChessServer)
  rt = RepeatedTimer(1, cleaner)  # it auto-starts, no need of rt.start()
  try:
    print("Server started http://%s:%s" % (hostName, serverPort))
    try:
      webServer.serve_forever()
    except KeyboardInterrupt:
      pass
  finally:
    rt.stop()

  webServer.server_close()
  print("Server stopped.")
