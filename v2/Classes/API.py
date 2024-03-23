import requests
from typing import Dict
from enum import Enum


# class Request_type(Dict[str,str],Enum):
#     PLAYER: {"name": "Player", "is_required": True}

# print(Request_type.PLAYER.value)

class APIRequest:
  def get_json_data(self):
    url = f"{self.base_url}{self.endpoint}"
    res = requests.get(url)
    return res.json()

class FPL_request(APIRequest):
  # options = {"PLAYER": {"endpoint": "element-summary/", "id_required": True},"TEAM": {"endpoint":"PLACEHOLDER", "id_required": True}}
  def __init__(self, req_type, id:int = None) -> None:
    self.base_url = "https://fantasy.premierleague.com/api/"
    self.endpoint = self.get_endpoint(req_type, id)
    
  def get_endpoint(self, req_type: str, id:int) -> str:
    match req_type.upper():
      case 'PL_PLAYER': 
        if id is None: raise ValueError
        else: return f"element-summary/{id}"
      case _: raise NotImplementedError
  
  def __repr__(self) -> str:
    return f"{self.base_url}{self.endpoint}"
