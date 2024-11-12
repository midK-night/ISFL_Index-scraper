from genJson import gen_json
from json_classes import Root, AStatsDef, AStatsKicking, AStatsOther, AStatsPassing, AStatsPunting, AStatsReceiving, AStatsRushing, AStatsST, HStatsDef, HStatsKicking, HStatsOther, HStatsPassing, HStatsPunting, HStatsReceiving, HStatsRushing, HStatsST
from new_scrape import export_stats_to_csv
import json

def deserialize (obj):
    return Root(obj['id'], obj['hId'], obj['aId'], obj['weather'], obj['hMascot'], obj['aMascot'], obj['hAbb'], obj['aAbb'], obj['hRec'], obj['aRec'], obj['h1Q'], obj['hF'], obj['a1Q'], obj['a2Q'], obj['a3Q'], obj['a4Q'], obj['aF'], obj["oPOGId"], obj['dPOGId'], obj['oPOG'], obj['dPOG'], obj['aFD'], obj['a3rdM'], obj['a3rdA'], obj['aYds'], obj['aPassing'], obj['aComp'], obj['aAtt'], obj['aYPP'], obj['aRushing'], obj['aRushes'], obj['aYPR'], obj['aPen'], obj['aPenYds'], obj['aTO'], obj['aInt'], obj['aTOP'], obj['hFD'], obj['h3rdM'], obj['h3rdA'], obj['h4thA'], obj['hYds'], obj['hPassing'], obj['hComp'], obj['hAtt'], obj['hYPP'], obj['hRushing'], obj['hRushes'], obj['hYPR'], obj['hPen'], obj['hPenYds'], obj['hTOP'], obj['scoring1Q'], obj['scoring2Q'], obj['scoring3Q'], obj['scoring4Q'], obj['scoringOT'], obj['aStatsPassing'], obj['hStatsPassing'], obj['aStatsRushing'], obj['hStatsRushing'], obj['aStatsReceiving'], obj['hStatsReceiving'], obj['aStatsKicking'], obj['hStatsKicking'], obj['aStatsPunting'], obj['hStatsPunting'], obj['aStatsST'], obj['hStatsST'], obj['aStatsDef'], obj['hStatsDef'], obj['aStatsOther'], obj['hStatsOther'], obj['h2Q'], obj['hFum'], obj['aFum'], obj['h4thM'], obj['hTO'], obj['hFumL'], obj['h4Q'], obj['a4thM'], obj['a4thA'], obj['h3Q'], obj['hInt'], obj['aFumL'])

def main(i_d: str, player_id: int, pathname: str, season: int):
    number = (int(player_id) % 10) + 1
    json_string = gen_json(number, player_id, i_d, season)
    root = json.loads(json_string, object_hook=deserialize)
    final_game = root[0]
    for game in root:
        if game.id == player_id:
            final_game = game
            break
    export_stats_to_csv(final_game, pathname)



if __name__ == '__main__':
    # Replace with the desired ID

    player_id = input("Enter ID: ")
    season = input("Enter Season: ")
    pathname = input("Enter desired pathname: ")
    i_d = ""
    if (int(input("ISFL or DSFL? (1/2): ")) == 1) :
        i_d = "I"
    else:
        i_d = "D"
    main(i_d,player_id, pathname, season)
