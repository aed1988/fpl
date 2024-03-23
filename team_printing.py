def team_printing(team : dict):
  print([k for k in team.keys()][0])
  for value in team.values():
    position = ''
    goalkeeper_count = 0
    output_string = ""
    for v in value:
      if v['position'] != position and goalkeeper_count <= 1: 
        position = v['position']
        output_string += "\n"  
        if v['position'] == 'Goalkeeper': goalkeeper_count += 1    
      output_string += v['id'] + v['name'] + ". "
  
  print(output_string + "\n\n")  
  
def test_team_printing(): team_printing(({'MS': [{'name': 'Jason Steele', 'position': 'Goalkeeper', 'club': 'Brighton'}, {'name': 'Pervis Estupiñán', 'position': 'Defender', 'club': 'Brighton'}, {'name': 'Trent Alexander-Arnold', 'position': 'Defender', 'club': 'Liverpool'}, {'name': 'Kieran Trippier', 'position': 'Defender', 'club': 'Newcastle'}, {'name': 'Gabriel Martinelli Silva', 'position': 'Midfielder', 'club': 'Arsenal'}, {'name': 'Kaoru Mitoma', 'position': 'Midfielder', 'club': 'Brighton'}, {'name': 'Marcus Rashford', 'position': 'Midfielder', 'club': 'Man Utd'}, {'name': 'Mohamed Salah', 'position': 'Midfielder', 'club': 'Liverpool'}, {'name': 'Callum Wilson', 'position': 'Forward', 'club': 'Newcastle'}, {'name': 'Alexander Isak', 'position': 'Forward', 'club': 'Newcastle'}, {'name': 'Erling Haaland', 'position': 'Forward', 'club': 'Man City'}, {'name': 'Kepa Arrizabalaga', 'position': 'Goalkeeper', 'club': 'Chelsea'}, {'name': 'Luke Shaw', 'position': 'Defender', 'club': 'Man Utd'}, {'name': 'Benjamin White', 'position': 'Defender', 'club': 'Arsenal'}, {'name': 'Jack Grealish', 'position': 'Midfielder', 'club': 'Man City'}]}))

if __name__ == '__main__':
  test_team_printing()