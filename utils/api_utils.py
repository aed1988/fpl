# %%
def get_json_from_api(url):
  import requests
  response = requests.get(url)
  json = response.json()

  return json

# %%
def get_player_info():
  try:
    import pandas as pd
    return pd.read_excel('/info.xlsx')
  except:
    import requests
    json = get_json_from_api('https://fantasy.premierleague.com/api/bootstrap-static')
    elements_df = pd.DataFrame(json['elements'])
    elementtypes_df = pd.DataFrame(json['element_types'])
