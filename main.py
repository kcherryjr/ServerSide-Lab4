from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo, playercareerstats

def get_player_id(name):
    player_list = players.find_players_by_full_name(name)
    if not player_list:
        return None
    return player_list[0]["id"]

def show_player_info(player_id):
    info = commonplayerinfo.CommonPlayerInfo(player_id=player_id)
    data = info.get_dict()

    headers = data["resultSets"][0]["headers"]
    row = data["resultSets"][0]["rowSet"][0]

    print("\n--- PLAYER INFO ---")
    print("Name:", row[headers.index("DISPLAY_FIRST_LAST")])
    print("Height:", row[headers.index("HEIGHT")])
    print("Weight:", row[headers.index("WEIGHT")])
    print("Position:", row[headers.index("POSITION")])
    print("Team:", row[headers.index("TEAM_NAME")])

def show_headline_stats(player_id):
    info = commonplayerinfo.CommonPlayerInfo(player_id=player_id)
    data = info.get_dict()

    # Headline stats are resultSets[1] in CommonPlayerInfo
    headers = data["resultSets"][1]["headers"]
    row = data["resultSets"][1]["rowSet"][0]

    print("\n--- PLAYER HEADLINE STATS ---")
    print("Season:", row[headers.index("TimeFrame")])
    print("Points:", row[headers.index("PTS")])
    print("Assists:", row[headers.index("AST")])
    print("Rebounds:", row[headers.index("REB")])

def main():
    print("NBA Player Lookup")
    print("------------------")

    while True:
        name = input("\nEnter full player name (or type 'exit' to quit): ")

        if name.lower() == "exit":
            print("Goodbye.")
            break

        player_id = get_player_id(name)

        if not player_id:
            print("Player not found.")
            continue

        while True:
            print("\nMenu:")
            print("1. View Player Info")
            print("2. View Player Headline Stats")
            print("3. Search Another Player")
            print("4. Exit")

            choice = input("Select an option (1-4): ")

            if choice == "1":
                show_player_info(player_id)
            elif choice == "2":
                show_headline_stats(player_id)
            elif choice == "3":
                break   # breaks back to name input
            elif choice == "4":
                print("Goodbye!")
                return
            else:
                print("Invalid option. Try again.")
if __name__ == "__main__":
 main()
