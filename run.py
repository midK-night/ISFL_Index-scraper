from genJson import gen_json
from json_classes import Root, AStatsDef, AStatsKicking, AStatsOther, AStatsPassing, AStatsPunting, AStatsReceiving, AStatsRushing, AStatsST, HStatsDef, HStatsKicking, HStatsOther, HStatsPassing, HStatsPunting, HStatsReceiving, HStatsRushing, HStatsST
from new_scrape import export_stats_to_csv
import json

def main(i_d: str, player_id: int, pathname: str, season: int):
    number = (int(player_id) % 10) + 1
    json_string = gen_json(number, player_id, i_d, season)
    root = json.loads(json_string)
    final_game = root[0]
    for game in root:
        if game['id'] == player_id:
            final_game = game
            break
    export_stats_to_csv(final_game, pathname)



if __name__ == '__main__':
    # Replace with the desired ID

    player_id = input("Enter ID: ")
    season = input("Enter Season: ")
    pathname = input("Enter desired pathname: ")
    i_d = "I" if int(input("ISFL or DSFL? (1/2): ")) == 1 else "D"
    main(i_d,player_id, pathname, season)
