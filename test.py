from genJson import gen_json
from json_classes import Root, AStatsDef, AStatsKicking, AStatsOther, AStatsPassing, AStatsPunting, AStatsReceiving, AStatsRushing, AStatsST, HStatsDef, HStatsKicking, HStatsOther, HStatsPassing, HStatsPunting, HStatsReceiving, HStatsRushing, HStatsST
from test_csv import export_stats_to_csv
import json

def deserialize(obj):
    # Debugging print to inspect object content
    print("Deserializing object:", obj)
    
    # Handling missing keys by providing default values
    return Root(
        obj.get('id', None), 
        obj.get('hId', None), 
        obj.get('aId', None), 
        obj.get('weather', ''), 
        obj.get('hMascot', ''), 
        obj.get('aMascot', ''), 
        obj.get('hAbb', ''), 
        obj.get('aAbb', ''), 
        obj.get('hRec', ''), 
        obj.get('aRec', ''), 
        obj.get('h1Q', 0), 
        obj.get('hF', 0), 
        obj.get('a1Q', 0), 
        obj.get('a2Q', 0), 
        obj.get('a3Q', 0), 
        obj.get('a4Q', 0), 
        obj.get('aF', 0), 
        obj.get("oPOGId", None), 
        obj.get('dPOGId', None), 
        obj.get('oPOG', ''), 
        obj.get('dPOG', ''), 
        obj.get('aFD', 0), 
        obj.get('a3rdM', 0), 
        obj.get('a3rdA', 0), 
        obj.get('aYds', 0), 
        obj.get('aPassing', 0), 
        obj.get('aComp', 0), 
        obj.get('aAtt', 0), 
        obj.get('aYPP', 0.0), 
        obj.get('aRushing', 0), 
        obj.get('aRushes', 0), 
        obj.get('aYPR', 0.0), 
        obj.get('aPen', 0), 
        obj.get('aPenYds', 0), 
        obj.get('aTO', 0), 
        obj.get('aInt', 0), 
        obj.get('aTOP', ''), 
        obj.get('hFD', 0), 
        obj.get('h3rdM', 0), 
        obj.get('h3rdA', 0), 
        obj.get('h4thA', 0), 
        obj.get('hYds', 0), 
        obj.get('hPassing', 0), 
        obj.get('hComp', 0), 
        obj.get('hAtt', 0), 
        obj.get('hYPP', 0.0), 
        obj.get('hRushing', 0), 
        obj.get('hRushes', 0), 
        obj.get('hYPR', 0.0), 
        obj.get('hPen', 0), 
        obj.get('hPenYds', 0), 
        obj.get('hTOP', ''), 
        obj.get('scoring1Q', ''), 
        obj.get('scoring2Q', ''), 
        obj.get('scoring3Q', ''), 
        obj.get('scoring4Q', ''), 
        obj.get('scoringOT', ''), 
        obj.get('aStatsPassing', {}), 
        obj.get('hStatsPassing', {}), 
        obj.get('aStatsRushing', {}), 
        obj.get('hStatsRushing', {}), 
        obj.get('aStatsReceiving', {}), 
        obj.get('hStatsReceiving', {}), 
        obj.get('aStatsKicking', {}), 
        obj.get('hStatsKicking', {}), 
        obj.get('aStatsPunting', {}), 
        obj.get('hStatsPunting', {}), 
        obj.get('aStatsST', {}), 
        obj.get('hStatsST', {}), 
        obj.get('aStatsDef', {}), 
        obj.get('hStatsDef', {}), 
        obj.get('aStatsOther', {}), 
        obj.get('hStatsOther', {}), 
        obj.get('h2Q', 0), 
        obj.get('hFum', 0), 
        obj.get('aFum', 0), 
        obj.get('h4thM', 0), 
        obj.get('hTO', 0), 
        obj.get('hFumL', 0), 
        obj.get('h4Q', 0), 
        obj.get('a4thM', 0), 
        obj.get('a4thA', 0), 
        obj.get('h3Q', 0), 
        obj.get('hInt', 0), 
        obj.get('aFumL', 0)
    )

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
