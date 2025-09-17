import json
import csv

# Load JSON data
with open('input.json', 'r', encoding='utf-8') as json_file:
    json_data = json.load(json_file)

# Read CSV data from file
csv_file_path = './data/csv/s9team.csv'
with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    csv_rows = list(csv_reader)

# Extract team names (first row) and player names (rows 2-4)
team_names = csv_rows[1]
player_rows = csv_rows[2:5]  # Rows 2 to 4 for players

# Validate CSV data
if len(team_names) != len(json_data['teams']):
    raise ValueError(f"Number of teams in CSV ({len(team_names)}) does not match JSON ({len(json_data['teams'])})")
for row in player_rows:
    if len(row) != len(team_names):
        raise ValueError(
            f"Number of players in CSV row ({len(row)}) does not match number of teams ({len(team_names)})")

# Process each team in the JSON
for team_idx, team in enumerate(json_data['teams']):
    # Update team_id with the corresponding team name from CSV
    team['team_id'] = team_names[team_idx]

    # Replace the single player entry with three player entries
    team['players'] = [
        {
            "player_id": player_rows[row_idx][team_idx],
            "total": {
                "kills": "/",
                "damage": "/",
                "assists": "/",
                "knockdowns": "/",
                "revives": "/",
                "respawns": "/",
                "avg_survival": "/"
            },
            "matches": {
                "match1": {
                    "kills": "/",
                    "damage": "/",
                    "assists": "/",
                    "knockdowns": "/",
                    "revives": "/",
                    "respawns": "/",
                    "avg_survival": "/"
                },
                "match2": {
                    "kills": "/",
                    "damage": "/",
                    "assists": "/",
                    "knockdowns": "/",
                    "revives": "/",
                    "respawns": "/",
                    "avg_survival": "/"
                },
                "match3": {
                    "kills": "/",
                    "damage": "/",
                    "assists": "/",
                    "knockdowns": "/",
                    "revives": "/",
                    "respawns": "/",
                    "avg_survival": "/"
                },
                "match4": {
                    "kills": "/",
                    "damage": "/",
                    "assists": "/",
                    "knockdowns": "/",
                    "revives": "/",
                    "respawns": "/",
                    "avg_survival": "/"
                }
            }
        } for row_idx in range(3)  # Create three player entries
    ]

# Save updated JSON to a new file
with open('updated.json', 'w', encoding='utf-8') as json_file:
    json.dump(json_data, json_file, ensure_ascii=False, indent=2)

print("JSON file has been updated with team and player names from the CSV.")