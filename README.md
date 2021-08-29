# Data analysis of fantasy premier league

## Objectives
1.  To boost knowledge of using pandas, matplotlib & seaborn
2.  To optimise purchase of players in both draft and standard format of the game


## Initial thoughts 
There is a lot of data to wade through from the api.  Will have to dig deeper to get view of how stats vary by week.  Long term goal is to analyse players/teams based on matchup and/or form.  API has this option in game, hope to see how useful this is.


#### 24/08/2021
Created basic plotting function to show how points vary by position.  Function is slow, I think this is due to the size of DataFrame created.  Will look to remove information that isn't relevant.  i.e. Players who haven't played any minutes.  Also want to colour code by team, but this may become difficult to read as a lot of teams play in similar colours, (e.g. Liverpool, Arsenal etc.)




#### Known endpoints (http://fantasy.premierleague.com/api)
1.  /bootstrap-static
  - Includes data about events, current points, players (actual & fantasy), teams and game settings.
2.  /fixtures
  - Response is fixtures & results.  Can query individual weeks "?event=1".
3.  /element-summary/{element_id}/
  - An element_id is required.  In this instance, element_id refers to a premier league player and responds with their fixtures & history (present and past seasons).
4.  /event/{event_id}/live/
  - Shows live updates of the selected event broken down by player.
5.  /entry/{manager_id}/
  - Returns info about yourself or a certain manager.  Can append "history/" to view previous seasons.
6.  /leagues-classic/{league_id}/standings/
  - Returns standings of any classic league.
7.  /my-team/{manager_id}/
  - Returns 'Picks', 'Chips' (triple captain, bench boost, wild card) and 'Transfers' for a certain team.