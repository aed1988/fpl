import time

from progress_bar import printProgressBar
from selenium import webdriver
from selenium.webdriver.common.by import By
import re

import sqlite3

from team_printing import team_printing

driver = webdriver.Firefox()

def input_gameweek_no(first_try = True) -> int:
  input_str = ''
  if first_try: input_str = 'Please enter gameweek number: '
  else: input_str = 'Please enter a valid gameweek number.  Your input must be an integer: ' 
  x = input(input_str)
  try:
    return  int(x) 
  except ValueError: input_gameweek_no(first_try=False)
  finally: print(f"You have entered: {int(x)}")

def get_player_photo_id(string:str) -> int:
  (start, end) =  re.search("\/p\d+", string).span()
  return string[start + 2 : end]

def get_rival_teams(player_id, gameweek_no):
  team = []
  driver.get(f"https://fantasy.premierleague.com/entry/{player_id}/event/{gameweek_no}")
  time.sleep(3)
  
  pitch_div = driver.find_element(By.CLASS_NAME, "Pitch__StyledPitch-sc-1mctasb-0")
    
  lineup = pitch_div.find_elements(By.CLASS_NAME, "ElementDialogButton__StyledElementDialogButton-sc-1vrzlgb-0")
  for player in lineup:
    player.click()
    time.sleep(0.5)
    photo_id = get_player_photo_id(driver.find_element(By.CLASS_NAME, f"{photo_id_class}").get_attribute('srcset'))
    name = driver.find_element(By.CLASS_NAME, f"{name_class}").text
    position = driver.find_element(By.CLASS_NAME, f"{position_class}").text
    club = driver.find_element(By.CLASS_NAME, f"{club_class}").text
    team.append({'id': photo_id, 'name': name, 'position': position, 'club': club})
    driver.find_element(By.CLASS_NAME, "Dialog__CloseButton-sc-5bogmv-1").click()
  return team
  
def query_database(query:str):
  connection = sqlite3.connect('fpl.db')
  cursor = connection.cursor()
  res = cursor.execute(query)
  return res.fetchall()

if __name__ == "__main__":   

  name_class = "haxmIv"
  position_class = "BFSeu"
  club_class = "cvAaWL"
  photo_id_class = "jNqegH"
  players = {'AD': 1312659, 'MS': 990931, 'MJ': 4240062, 'MD': 1763990, 'DC': 3111635, 'RM': 2746994}
  teams = []
  
  try:
    gameweek_no = input_gameweek_no()
    
    l = len(players)
    driver.get("https://fantasy.premierleague.com/")
    time.sleep(3)
    click_accept_cookies = driver.find_element(By.ID, 'onetrust-accept-btn-handler')
    click_accept_cookies.click()

    printProgressBar(0, l,  prefix = 'Progress:', suffix = 'Complete', length = 50)
    for i, (player_name, id) in enumerate(players.items()):
      rival_team = {player_name: get_rival_teams(id, gameweek_no=gameweek_no)}
      teams.append(rival_team)
      printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
      
    for team in teams: team_printing(team)
      
  finally:
    driver.quit()



