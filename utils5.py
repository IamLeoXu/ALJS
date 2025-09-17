import csv
import json

# Initialize the JSON template structure
json_template = {
    "num_matches": 5,
    "teams": []
}

# Read the CSV file and print headers for debugging
with open('./data/csv/s10.csv', newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)

    # Print column headers to debug
    print("CSV Headers:", reader.fieldnames)

    for row in reader:
        # Use the exact column name from the CSV; assuming '队伍' for team name
        team_name = row.get('队伍', 'Unknown_Team')  # Fallback to 'Unknown_Team' if column missing

        # Calculate total points and kills from CSV
        total_points = int(row['总总分']) if row.get('总总分') else 0
        total_kills = sum([
            int(row['第一局击杀']) if row.get('第一局击杀') else 0,
            int(row['第二局击杀']) if row.get('第二局击杀') else 0,
            int(row['第三局击杀']) if row.get('第三局击杀') else 0,
            int(row['第四局击杀']) if row.get('第四局击杀') else 0,
            int(row['第五局击杀']) if row.get('第五局击杀') else 0
        ])

        # Create team entry
        team_entry = {
            "team_id": team_name,
            "total": {
                "points": total_points,
                "placement": int(row['总总排名']) if row.get('总总排名') else 0,
                "kills": total_kills
            },
            "matches": {
                "match1": {
                    "points": int(row['第一局总分']) if row.get('第一局总分') else 0,
                    "placement": int(row['第一局排名']) if row.get('第一局排名') else 0,
                    "kills": int(row['第一局击杀']) if row.get('第一局击杀') else 0
                },
                "match2": {
                    "points": int(row['第二局总分']) if row.get('第二局总分') else 0,
                    "placement": int(row['第二局排名']) if row.get('第二局排名') else 0,
                    "kills": int(row['第二局击杀']) if row.get('第二局击杀') else 0
                },
                "match3": {
                    "points": int(row['第三局总分']) if row.get('第三局总分') else 0,
                    "placement": int(row['第三局排名']) if row.get('第三局排名') else 0,
                    "kills": int(row['第三局击杀']) if row.get('第三局击杀') else 0
                },
                "match4": {
                    "points": int(row['第四局总分']) if row.get('第四局总分') else 0,
                    "placement": int(row['第四局排名']) if row.get('第四局排名') else 0,
                    "kills": int(row['第四局击杀']) if row.get('第四局击杀') else 0
                },
                "match5": {
                    "points": int(row['第五局总分']) if row.get('第五局总分') else 0,
                    "placement": int(row['第五局排名']) if row.get('第五局排名') else 0,
                    "kills": int(row['第五局击杀']) if row.get('第五局击杀') else 0
                }
            },
            "players": [
                {
                    "player_id": "/",
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
                        },
                        "match5": {
                            "kills": "/",
                            "damage": "/",
                            "assists": "/",
                            "knockdowns": "/",
                            "revives": "/",
                            "respawns": "/",
                            "avg_survival": "/"
                        }
                    }
                }
            ]
        }

        # Append team entry to teams list
        json_template["teams"].append(team_entry)

# Write the JSON data to a file
with open('input.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(json_template, jsonfile, indent=2, ensure_ascii=False)