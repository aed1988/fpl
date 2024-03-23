import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import re

class Scraper:
  def __init__(self):
    self.name_class = "haxmIv"
    self.position_class = "BFSeu"
    self.club_class = "cvAaWL"
    self.photo_id_class = "jNqegH"
    self.driver = webdriver.Firefox()
    
  def login(self):
    self.driver.get("https://fantasy.premierleague.com/")
    time.sleep(3)
    click_accept_cookies = self.driver.find_element(By.ID, 'onetrust-accept-btn-handler')
    click_accept_cookies.click()
    
  def get_inputweek_no(self, first_attempt = True) -> int:
    input_str = ''
    if first_attempt: input_str = 'Please enter gameweek number: '
    else: input_str = 'Please enter a valid gameweek number.  Your input must be an integer: ' 
    x = input(input_str)
    try:
      return  int(x) 
    except ValueError: self.get_gameweek_no(first_try=False)
    finally: print(f"You have entered: {int(x)}")
      
  def get_rivals_team(self, player_id, gameweek_no):
    team = []
    self.driver.get(f"https://fantasy.premierleague.com/entry/{player_id}/event/{gameweek_no}")
    time.sleep(3)
    driver = self.driver
    pitch_div = driver.find_element(By.CLASS_NAME, "Pitch__StyledPitch-sc-1mctasb-0")
      
    lineup = pitch_div.find_elements(By.CLASS_NAME, "ElementDialogButton__StyledElementDialogButton-sc-1vrzlgb-0")
    for player in lineup:
      player.click()
      time.sleep(0.5)
      name = driver.find_element(By.CLASS_NAME, f"{self.name_class}").text
      position = driver.find_element(By.CLASS_NAME, f"{self.position_class}").text
      club = driver.find_element(By.CLASS_NAME, f"{self.club_class}").text
      team.append({'name': name, 'position': position, 'club': club})
      driver.find_element(By.CLASS_NAME, "Dialog__CloseButton-sc-5bogmv-1").click()
    return team
  
  def quit_scraper(self):
    self.driver.quit()



# def get_player_photo_id(string:str) -> int:
#   (start, end) =  re.search("\/p\d+", string).span()
#   return string[start + 2 : end]


if __name__ == "__main__":   

  
  players = {'AD': 1312659, 'MS': 990931, 'MJ': 4240062, 'MD': 1763990, 'DC': 3111635, 'RM': 2746994}
  teams = []
  
  scrape = Scraper()


    # printProgressBar(0, l,  prefix = 'Progress:', suffix = 'Complete', length = 50)
    # for i, (player_name, id) in enumerate(players.items()):
    #   rival_team = {player_name: get_rival_teams(id, gameweek_no=gameweek_no)}
    #   teams.append(rival_team)
    #   printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
      
    # for team in teams: team_printing(team)




