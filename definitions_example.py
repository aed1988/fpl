import os


ROOT_DIR = os.path.dirname(os.path.abspath('__file__'))
PICKLE_DIR = os.path.join(ROOT_DIR,'csv')

RAPID_API_KEY="rapid123api456key789"
FPL_EMAIL="email@email.com"
FPL_PASSWORD="password1"

points = {
  'Goalkeeper': {
    'clean_sheet': 4,
    'goal': 6,
    'assist': 3,
    'appearance': 1,
    'more_than_sixty_minutes': 1,
    'yellow_card': -1,
    'red_card': -2,
    'every_three_saves': 1,
    'penalty_save': 5,
    'penalty_miss': -2,
    'every_two_goals_conceded': -1,
    'own_goal': -2
  },
  'Defender': {
    'clean_sheet': 4,
    'goal': 6,
    'assist': 3,
    'appearance': 1,
    'more_than_sixty_minutes': 1,
    'yellow_card': -1,
    'red_card': -2,
    'penalty_miss': -2,
    'every_two_goals_conceded': -1,
    'own_goal': -2
  },
  'Midfielder': {
    'clean_sheet': 1,
    'goal': 5,
    'assist': 3,
    'appearance': 1,
    'more_than_sixty_minutes': 1,
    'yellow_card': -1,
    'red_card': -2,
    'penalty_miss': -2,
    'own_goal': -2
  },
  'Attacker': {
    'clean_sheet': 4,
    'goal': 4,
    'assist': 3,
    'appearance': 1,
    'more_than_sixty_minutes': 1,
    'yellow_card': -1,
    'red_card': -2,
    'penalty_miss': -2,
    'own_goal': -2
  }
}