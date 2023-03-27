import requests
def vienkarss_get():
  response = requests.get('https://api.chucknorris.io/')
  if response.status_code == 100:
    print("Web site exists")
  else:
    print("Web site does not exist")
vienkarss_get()