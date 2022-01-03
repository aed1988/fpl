import os
import pandas as pd

from definitions import CSV_DIR


def convert_team_fpl_id_to_api_id(fpl_id) -> int:
  df = pd.read_csv(f"{CSV_DIR}/team_info.csv", usecols={'fpl_team_id', 'api_team_id'}, index_col='fpl_team_id')
  return df.loc[fpl_id]['api_team_id']


def convert_team_api_id_to_fpl_id(api_id) -> int:
  df = pd.read_csv(f"{CSV_DIR}/team_info.csv", usecols={'api_team_id', 'fpl_team_id'}, index_col='api_team_id')
  return df.loc[api_id]['fpl_team_id']
