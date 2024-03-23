import os
import pandas as pd

from definitions import PICKLE_DIR


def convert_team_fpl_id_to_api_id(fpl_id) -> int:
  df = pd.read_pickle(f"{PICKLE_DIR}/team_info.pickle", usecols={'fpl_team_id', 'api_team_id'}, index_col='fpl_team_id')
  return df.loc[fpl_id]['api_team_id']


def convert_team_api_id_to_fpl_id(api_id) -> int:
  df = pd.read_pickle(f"{PICKLE_DIR}/team_info.pickle", usecols={'api_team_id', 'fpl_team_id'}, index_col='api_team_id')
  return df.loc[api_id]['fpl_team_id']

def get_next_gameweek() -> int:
  next_gameweek = pd.read_pickle(f"{PICKLE_DIR}/gw.pickle")
  return next_gameweek.loc[next_gameweek['is_next'] == True].index[0]