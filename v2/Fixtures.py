from dataclasses import dataclass, field
from typing import List

from Classes import API

@dataclass
class Fixture:
  id: int
  code: int
  team_h: int
  team_h_score: int
  team_a: int
  team_a_score:int
  event:int
  finished: bool
  minutes: int
  provisional_start_time: bool
  kickoff_time: str
  event_name: str
  is_home: bool
  difficulty: int
  
  def __repr__(self) -> str:
    return f"{self.event_name} - {'Vs.' if self.is_home else '@'} {self.team_h if self.is_home else self.team_a}"
  

@dataclass
class Result:
  element: int
  fixture: int
  opponent_team: int
  total_points: int
  was_home: bool
  kickoff_time: str
  team_h_score: int
  team_a_score: int
  round: int
  minutes: int
  goals_scored: int
  assists: int
  clean_sheets: int
  goals_conceded: int
  own_goals: int
  penalties_saved: int
  penalties_missed: int
  yellow_cards: int
  red_cards: int
  saves: int
  bonus: int
  bps: int
  influence: str
  creativity: str
  threat: str
  ict_index: str
  starts: int
  expected_goals: int
  expected_assists: int
  expected_goal_involvements: int
  expected_goals_conceded: int
  value: int
  transfers_balance: int
  selected: int
  transfers_in: int
  transfers_out: int
  
  def __repr__(self) -> str:
    home_away_text = 'Vs' if self.was_home else '@'
    return f"Fixture {self.round :02}: {home_away_text: <4} {self.opponent_team}.  {self.team_h_score if self.was_home else self.team_a_score} - {self.team_a_score if self.was_home else self.team_h_score}"
  
@dataclass
class FixturesData:
  element_id: int
  fixtures: List[Fixture] = field(init = False , default_factory=list)
  history: List[Result] = field(init = False , default_factory=list)
  history_past:None = field(init = False , default_factory=list)
  
  def __post_init__(self) -> None:
    res = API.FPL_request('PL_PLAYEr', self.element_id).get_json_data()
    self.fixtures = [Fixture(**fixture) for fixture in res['fixtures']]
    self.history = [Result(**result) for result in res['history']]
    


if __name__ == "__main__":
  f = FixturesData(437)
  print(f.fixtures)