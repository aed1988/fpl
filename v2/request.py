from BootstrapStatic import BootstrapStaticData, BOOTSTRAP_STATIC_END_POINT
from Fixtures import FixturesData, FIXTURE_API_ENDPOINT
import requests

fpl_api_url = 'https://fantasy.premierleague.com/api'
endpoint_url = f"{fpl_api_url}{FIXTURE_API_ENDPOINT}"
req = requests.get(endpoint_url)

res_json = req.json()

res = FixturesData(**res_json)
for result in res.history:
  print(result)