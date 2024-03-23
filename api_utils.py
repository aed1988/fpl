import requests
from definitions import FPL_EMAIL, FPL_PASSWORD



def get_json_from_fpl_api(url, login=False, headers=None, querystring=None, cookies=None):
  payload={
    "login": FPL_EMAIL, 
    "password": FPL_PASSWORD, 
    "app":"plfpl-web", 
    "redirect_uri":"https://fantasy.premierleague.com/"
  }
  with requests.Session() as s:
    if login == True:
      p = s.post("https://users.premierleague.com/accounts/login/", data=payload)
      # print the html returned or something more intelligent to see if it's a successful login page.
      # print(p.text)

    # An authorised request.
    res = s.get(url)
    return res.json()