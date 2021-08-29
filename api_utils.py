# %%
def get_json_from_api(url):
  import requests
  response = requests.get(url)
  json = response.json()

  return json

# %%
