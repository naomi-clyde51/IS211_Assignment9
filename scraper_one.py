from bs4 import BeautifulSoup
import requests
import pandas as pd

# LINK: "https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/?sortcol=td&sortdir=descending"

URL = "https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/?sortcol=td&sortdir=descending"

def scrape_top_20_td_leaders():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Locate the stat table on the page
    table = soup.find('table', class_='TableBase-table')
    if not table:
        print("Could not find the stats table.")
        return []

    players_data = []
    rows = table.find('tbody').find_all('tr')
    
    # Extract data for the top 20 players (or all available if less than 20)
    for row in rows[:20]:
        cells = row.find_all('td')
        
        # Player name, position, and team are usually grouped in the first cell
        player_info_cell = cells[0].find('span', class_='CellPlayerName--long')
        if not player_info_cell:
            player_info_cell = cells[0].find('span', class_='CellPlayerName-short')
        
        # Name
        name_elem = player_info_cell.find('a') if player_info_cell else None
        name = name_elem.text.strip() if name_elem else "N/A"
        
        # Position and Team
        pos_team_span = row.find('span', class_='CellPlayerName-teamPosition')
        pos_team_text = pos_team_span.text.strip() if pos_team_span else "N/A"
        
        # Parse position and team from the combined string (format: POS | TEAM)
        try:
            parts = pos_team_text.split('|')
            position = parts[0].strip()
            team = parts[1].strip()
        except IndexError:
            position, team = "N/A", "N/A"
            
        # Total Touchdowns
        # (Change index based on the specific page category you visit)
        try:
            touchdowns = cells[3].text.strip() 
        except IndexError:
            touchdowns = "N/A"

        players_data.append({
            "Player": name,
            "Position": position,
            "Team": team,
            "Touchdowns": touchdowns
        })
        
    return players_data

# Run the scraper and display results
top_players = scrape_top_20_td_leaders()

if top_players:
    df = pd.DataFrame(top_players)
    print(df.to_string(index=False))
    
if __name__ == "__main__":
    print("Running scrapper one...")
