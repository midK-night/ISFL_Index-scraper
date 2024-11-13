from genJson import gen_json
from json_classes import Root, AStatsDef, AStatsKicking, AStatsOther, AStatsPassing, AStatsPunting, AStatsReceiving, AStatsRushing, AStatsST, HStatsDef, HStatsKicking, HStatsOther, HStatsPassing, HStatsPunting, HStatsReceiving, HStatsRushing, HStatsST
from test_csv import export_stats_to_csv
import json

def main(i_d: str, player_id: int, pathname: str, season: int):
    number = (int(player_id) % 10) + 1
    json_string = gen_json(number, player_id, i_d, season)
    
    # print("Generated JSON string:")
    # print(json_string)
    
    root = json.loads(json_string)
    
    final_game = root[0]
    for game in root:
        if game['id'] == player_id:
            final_game = game
            break
    
    for key in final_game:
        print(key)
        print(final_game[key])

    # print("Final game selected:")
    # print(final_game.id)
    # # print(final_game.to_dict())
    
    export_stats_to_csv(final_game, pathname)

if __name__ == '__main__':
    # player_id = int(input("Enter ID: "))  # Ensure player_id is an integer
    # season = int(input("Enter Season: "))  # Ensure season is an integer
    # pathname = input("Enter desired pathname: ")
    # i_d = "I" if int(input("ISFL or DSFL? (1/2): ")) == 1 else "D"
    # main(i_d, player_id, pathname, season)
    main("D", 4455, "s50_bbb_1", 50)
