from dataclasses import dataclass, field
from typing import List, Dict

from Fixtures import *

BOOTSTRAP_STATIC_END_POINT = "/bootstrap-static/"

@dataclass
class Event:
  id: int
  name: str
  deadline_time: str
  release_time: str
  average_entry_score: int
  finished: bool
  data_checked: bool
  highest_scoring_entry: bool
  deadline_time_epoch: int
  deadline_time_game_offset: int
  highest_score: int
  is_previous: bool
  is_current: bool
  is_next: bool
  cup_leagues_created: bool
  h2h_ko_matches_created: bool
  ranked_count: int
  chip_plays: Dict
  most_selected: int
  most_transferred_in: int
  top_element: int
  top_element_info: Dict
  transfers_made: int
  most_captained: int
  most_vice_captained: int
  
  def __repr__(self) -> str:
    return self.name

@dataclass
class Team:
  code: int
  draw: int
  form: None
  id: int
  loss: int
  name: str
  played: int
  points: int
  position: int
  short_name: str
  strength: int
  team_division: None
  unavailable: bool
  win: int
  strength_overall_home: int
  strength_overall_away: int
  strength_attack_home: int
  strength_attack_away: int
  strength_defence_home: int
  strength_defence_away: int
  pulse_id: 1
  
  def __repr__(self) -> str:
    return f"{self.name}"
  
@dataclass
class Player:
  chance_of_playing_next_round: int
  chance_of_playing_this_round: int
  code: int
  cost_change_event: float
  cost_change_event_fall: float
  cost_change_start: float
  cost_change_start_fall: float
  dreamteam_count: int
  element_type: int
  ep_next: str
  ep_this: str
  event_points: int
  first_name: str
  form: str
  id: int
  in_dreamteam: bool
  news: str
  news_added: str
  now_cost: int
  photo: str
  points_per_game: str
  second_name: str
  selected_by_percent: str
  special: bool
  squad_number: int
  status: str
  team: int
  team_code: int
  total_points: int
  transfers_in: int
  transfers_in_event: int
  transfers_out: int
  transfers_out_event: int
  value_form: str
  value_season: str
  web_name: str
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
  expected_goals: str
  expected_assists: str
  expected_goal_involvements: str
  expected_goals_conceded: str
  influence_rank: int
  influence_rank_type: int
  creativity_rank: int
  creativity_rank_type: int
  threat_rank: int
  threat_rank_type: int
  ict_index_rank: int
  ict_index_rank_type: int
  corners_and_indirect_freekicks_order: int
  corners_and_indirect_freekicks_text: str
  direct_freekicks_order: int
  direct_freekicks_text: str
  penalties_order: int
  penalties_text: int
  expected_goals_per_90: float
  saves_per_90: float
  expected_assists_per_90: float
  expected_goal_involvements_per_90: float
  expected_goals_conceded_per_90: float
  goals_conceded_per_90: float
  now_cost_rank: int
  now_cost_rank_type: int
  form_rank: int
  form_rank_type: int
  points_per_game_rank: int
  points_per_game_rank_type: int
  selected_rank: int
  selected_rank_type: int
  starts_per_90: int
  clean_sheets_per_90: int
  fixtures: List[Fixture] = field(init=False)
  
  def get_fixtures(self):
    self.fixtures = FixturesData(437)
  
  
  def __repr__(self) -> str:
    return f"{self.first_name} {self.second_name}"
  
  def get_fixtures(self):
    pass
    
@dataclass
class BootstrapStaticData:
  events: List[Event]
  game_settings: List[None]
  phases: List[None]
  teams: List[Team]
  total_players: int
  elements: List[Player]
  element_stats: List[None]
  element_types: List[None]
  
  def __post_init__(self):
    self.teams = [Team(**team) for team in self.teams]
    self.elements = [Player(**player) for player in self.elements]
    self.events = [Event(**event) for event in self.events]
  
  def __repr__(self) -> str:
    return "Response"