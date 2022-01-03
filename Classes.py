from datetime import datetime 
import time

import pandas as pd

from definitions import CSV_DIR
from df_utils import convert_team_api_id_to_fpl_id, convert_team_fpl_id_to_api_id


class Fixture():

  def __init__(self, api_fixture_id: int):
    self._id = api_fixture_id
    self._kickoff_time = None
    self._venue_id = None
    self._venue = None
    self._home_team_api_id = None
    self._away_team_api_id = None
    self._home_team_score = None
    self._away_team_score = None

    self.populate_fixture_info()

  def __str__(self):
    home_team_fpl_id = convert_team_api_id_to_fpl_id(self._home_team_api_id)
    away_team_fpl_id = convert_team_api_id_to_fpl_id(self._away_team_api_id)
    return f"{Team(home_team_fpl_id).get_team_name()} VS. {Team(away_team_fpl_id).get_team_name()}.  KO: {self._kickoff_time}"

  def populate_fixture_info(self) -> None:
    fixture_df = pd.read_csv(f"{CSV_DIR}/fixtures.csv", index_col = 'fixture_id')
    fixture_df = fixture_df.convert_dtypes()
    fixture_series = fixture_df.loc[self._id]
    self._kickoff_time = datetime.utcfromtimestamp(fixture_series.timestamp)
    self._venue_id = fixture_series.venue
    # self._venue = None
    self._home_team_api_id = fixture_series.api_home_team_id
    self._away_team_api_id = fixture_series.api_away_team_id
    self._home_team = Team(convert_team_api_id_to_fpl_id(self._home_team_api_id))
    self._away_team = Team(convert_team_api_id_to_fpl_id(self._away_team_api_id))
    self._home_team_score = fixture_series.home_score
    self._away_team_score = fixture_series.away_score

    if None in (self._kickoff_time, self._venue_id, self._home_team_api_id, self._away_team_api_id):
      print('Unable to populate all fixture information')
    
  
  def get_venue_id(self) -> str:
    return self._venue_id
  def get_kickoff_time(self) -> int:
    return self._kickoff_time
  def get_home_team(self) -> str:
    return self._home_team
  def get_away_team(self) -> str:
    return self._away_team



class Team():

  def __init__(self, fpl_id: int):
    self.__id = fpl_id
    self._team_name = None
    self._venue_name = None
    self._fixtures = None
    self._results = None
    self._api_id = convert_team_fpl_id_to_api_id(self.__id)

  def get_team_name(self) -> str:
    if self._team_name is None:
      self._team_name = pd.read_csv(f"{CSV_DIR}/team_info.csv", index_col='fpl_team_id').loc[self.__id, 'name']
    return self._team_name

  def get_home_venue(self) -> str:
    if self._venue_name is None:
      self._venue_name = pd.read_csv(f"{CSV_DIR}/team_info.csv", index_col='fpl_team_id').loc[self.__id, 'venue_name']
    return self._venue_name

  def next_fixtures(self, number):
    gameweek_df = pd.read_csv(f"{CSV_DIR}/gameweek.csv")
    gameweek_df = gameweek_df[gameweek_df['deadline_time_epoch'] > time.time()]
    next_gameweek_deadline = min(gameweek_df['deadline_time_epoch'])

    fixtures_df = pd.read_csv(f"{CSV_DIR}/fixtures.csv", usecols=['fixture_id', 'timestamp', 'api_home_team_id', 'api_away_team_id'])
    fixtures_df = fixtures_df[
      (fixtures_df['timestamp'] > next_gameweek_deadline) &
      ((fixtures_df['api_home_team_id'] == self._api_id) | (fixtures_df['api_away_team_id'] == self._api_id))
    ]
    fixtures_df.sort_values(by=['timestamp'])

    for i in range(number):
      next_fixture_id = fixtures_df.iloc[i - 1].fixture_id
      print(Fixture(next_fixture_id))



class Player():
  def __init__(self, fpl_id: int):
    self.__id = fpl_id
    self.team = None
    self._full_name = None
    self._position = None
    self._ingame_stats = None
    self._fpl_stats = None

  def get_full_name(self) -> str:
    if self._full_name == None:
      name_arr = pd.read_csv(f"{CSV_DIR}/pl_player_info.csv", usecols={'id', 'first_name', 'second_name'}, index_col='id').loc[self.__id]
      self._full_name = f"{name_arr['first_name']} {name_arr['second_name']}"
    return self._full_name
  
  def get_team(self) -> str:
    if self.team == None:
      team_id = pd.read_csv(f"{CSV_DIR}/pl_player_info.csv", usecols={'id', 'team'}).loc[self.__id, 'team']
      self.team = Team(team_id)
    return self.team

  def get_position(self) -> str:
    if self._position == None:
      position_id = pd.read_csv(f"{CSV_DIR}/pl_player_info.csv", usecols={'id', 'element_type'}, index_col='id').loc[self.__id, 'element_type']
      self._position = pd.read_csv(f"{CSV_DIR}/element_info.csv", usecols={'id', 'singular_name'}, index_col='id').loc[position_id, 'singular_name']
    return self._position


