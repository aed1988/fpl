# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import requests
from utils.api_utils import get_json_from_api
import pandas as pd


# %%
def left_merge_player_info(
  df: pd.core.frame.DataFrame, file_path: str = '../csv/player_info.csv', 
  left_on: str = 'id', right_index: bool = True
  ):

  try:
     right_df = pd.read_csv(file_path, index_col=0)
     df = df.merge(right_df, left_on=left_on, right_index=right_index)


  except FileNotFoundError:
    json = get_json_from_api('http://fantasy.premierleague.com/api/bootstrap-static/')

    elements_df = pd.DataFrame(json['elements'])[['id', 'web_name', 'first_name', 'second_name', 'photo', 'team_code', 'element_type']]
    teams_df = pd.DataFrame(json['teams'])[['code', 'short_name', 'name']]
    element_types_df = pd.DataFrame(json['element_types'])[['id', 'singular_name', 'singular_name_short']]
    elements_df.set_index('id', inplace=True)
    teams_df.set_index('code', inplace=True)
    element_types_df.set_index('id', inplace=True)

    merge_1 = elements_df.merge(teams_df, how='left', left_on='team_code', right_on='code')
    df = merge_1.merge(element_types_df, how='left', left_on='element_type', right_index=True)
    
    df.to_csv(file_path)

  return df
