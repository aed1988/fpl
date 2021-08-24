# Data analysis of fantasy premier league

## Objectives
1.  To boost knowledge of using pandas, matplotlib & seaborn
2.  To optimise purchase of players in both draft and standard format of the game


## Initial thoughts 
There is a lot of data to wade through from the api.  Will have to dig deeper to get view of how stats vary by week.  Long term goal is to analyse players/teams based on matchup and/or form.  API has this option in game, hope to see how useful this is.

## 24/08/2021
Created basic plotting function to show how points vary by position.  Function is slow, I think this is due to the size of DataFrame created.  Will look to remove information that isn't relevant.  i.e. Players who haven't played any minutes.  Also want to colour code by team, but this may become difficult to read as a lot of teams play in similar colours, (e.g. Liverpool, Arsenal etc.)