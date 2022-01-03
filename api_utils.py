import requests
from dotenv import dotenv_values



def get_json_from_fpl_api(url, login=True, headers=None, querystring=None, cookies=None):
  payload={
    "login": dotenv_values('.env.secret')['FPL_EMAIL'], 
    "password": dotenv_values('.env.secret')['FPL_PASSWORD'], 
    "app":"plfpl-web", 
    "redirect_uri":"https://fantasy.premierleague.com/"
  }
  with requests.Session() as s:
    if login == True:
      p = s.post("https://users.premierleague.com/accounts/login/", data=payload)
      # print the html returned or something more intelligent to see if it's a successful login page.
      # print(p.text)

    # An authorised request.
    res = s.get('https://fantasy.premierleague.com/api/my-team/2563990/')
    return res.json()