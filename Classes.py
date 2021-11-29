from datetime import datetime 

import pandas as pd



class Fixture():

  def __init__(self, fixture_id):
    self._id = fixture_id
    self._kick_off_time = None
    self._venue = None 
    self._home_team_id = None
    self._away_team_id = None
    self._home_team_score = None
    self._away_team_score = None

    self.get_fixture_info()

  def __str__(self):
    return f"{Team.Team(self._home_team_id).get_team_name()} VS. {Team.Team(self._away_team_id).get_team_name()}.  KO: {self._kick_off_time}"

  def get_fixture_info(self):
    fixture_df = pd.read_csv('../csv/fixtures.csv', index_col = 'fixture_id')
    fixture_series = fixture_df.loc[self._id]
    self._kick_off_time = datetime.utcfromtimestamp(fixture_series.timestamp)
    self._venue = fixture_series.venue
    self._home_team_id = fixture_series.api_home_team_id
    self._away_team_id = fixture_series.api_away_team_id
    self._home_team_score = fixture_series.home_score
    self._away_team_score = fixture_series.away_score
    
  
  def get_venue(self):
    return self._venue

  def get_kickoff_time(self):
    return self._kickoff_time



class Team():

  def __init__(self, id: int):
    self.__id = id
    self._team_name = None
    self._venue_name = None

  def get_team_name(self) -> str:
    if self._team_name is None:
      self._team_name = pd.read_csv('../csv/team_info.csv', index_col='api_team_id').loc[self.__id][1]
    return self._team_name

  def get_home_venue(self):
    if self._venue_name is None:
      self._venue_name = pd.read_csv('csv/team_info.csv', index_col='api_team_id').loc[self.__id][3]
    return self._venue_name

  def get_next_fixtures(self, number) -> Fixture:
    gameweek_df = pd.read_csv('../csv/gameweek.csv')
    gameweek_df = gameweek_df[gameweek_df['deadline_time_epoch'] > time.time()]
    next_gameweek_deadline = min(gameweek_df['deadline_time_epoch'])

    fixtures_df = pd.read_csv('../csv/fixtures.csv', usecols=['fixture_id', 'timestamp', 'venue', 'api_home_team_id', 'api_away_team_id'])
    fixtures_df = fixtures_df[
      (fixtures_df['timestamp'] > next_gameweek_deadline) &
      ((fixtures_df['api_home_team_id'] == self.__id) | (fixtures_df['api_away_team_id'] == self.__id))
    ]
    fixtures_df.sort_values(by=['timestamp'])

    for i in range(number):
      next_fixture_id = fixtures_df.iloc[i - 1].fixture_id
      print(Fixture.Fixture(next_fixture_id))
