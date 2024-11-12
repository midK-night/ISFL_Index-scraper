import csv
from typing import List
from json_classes import Root, AStatsDef, AStatsKicking, AStatsOther, AStatsPassing, AStatsPunting, AStatsReceiving, AStatsRushing, AStatsST, HStatsDef, HStatsKicking, HStatsOther, HStatsPassing, HStatsPunting, HStatsReceiving, HStatsRushing, HStatsST
import os
import collections
from collections import UserList

def write_to_csv(filename: str, objects: List, path):
    if not os.path.exists(path):
        os.makedirs(path)

    
    # with open(os.path.join(path, filename), mode='w', newline='') as file:
    #     writer = csv.DictWriter(file, fieldnames=fieldnames)
    #     writer.writeheader()
    #     for row in data:
    #         writer.writerow(row)

    fieldnames = UserList(objects[0].to_dict().keys())
    with open(os.path.join(path, filename), mode='w', newline='') as file: 
        writer = csv.DictWriter(file, fieldnames=fieldnames) 
        writer.writeheader() 
        for obj in objects: 
            writer.writerow(obj.to_dict())

def export_stats_to_csv(root: Root, path):
    write_to_csv('a_stats_passing.csv', root.aStatsPassing, path)
    write_to_csv('a_stats_rushing.csv', root.aStatsRushing, path)
    write_to_csv('a_stats_receiving.csv', root.aStatsReceiving, path)
    write_to_csv('a_stats_kicking.csv', root.aStatsKicking, path)
    write_to_csv('a_stats_punting.csv', root.aStatsPunting, path)
    write_to_csv('a_stats_st.csv', root.aStatsST, path)
    write_to_csv('a_stats_def.csv', root.aStatsDef, path)
    write_to_csv('a_stats_other.csv', root.aStatsOther, path)

    write_to_csv('h_stats_passing.csv', root.hStatsPassing, path)
    write_to_csv('h_stats_rushing.csv', root.hStatsRushing, path)
    write_to_csv('h_stats_receiving.csv', root.hStatsReceiving, path)
    write_to_csv('h_stats_kicking.csv', root.hStatsKicking, path)
    write_to_csv('h_stats_punting.csv', root.hStatsPunting, path)
    write_to_csv('h_stats_st.csv', root.hStatsST, path)
    write_to_csv('h_stats_def.csv', root.hStatsDef, path)
    write_to_csv('h_stats_other.csv', root.hStatsOther, path)

    # Exporting game metadata
    game_data = {
        'id': root.id,
        'hId': root.hId,
        'aId': root.aId,
        'weather': root.weather,
        'hMascot': root.hMascot,
        'aMascot': root.aMascot,
        'hAbb': root.hAbb,
        'aAbb': root.aAbb,
        'hRec': root.hRec,
        'aRec': root.aRec,
        'h1Q': root.h1Q,
        'h2Q': root.h2Q,
        'h3Q': root.h3Q,
        'h4Q': root.h4Q,
        'hF': root.hF,
        'a1Q': root.a1Q,
        'a2Q': root.a2Q,
        'a3Q': root.a3Q,
        'a4Q': root.a4Q,
        'aF': root.aF,
        'oPOGId': root.oPOGId,
        'dPOGId': root.dPOGId,
        'oPOG': root.oPOG,
        'dPOG': root.dPOG,
        'aFD': root.aFD,
        'hFD': root.hFD,
        # Add other relevant fields as needed
    }
    with open(os.path.join(path, 'game_metadata.csv'), mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=game_data.keys())
        writer.writeheader()
        writer.writerow(game_data)

# Assuming you have an instance of Root
# root_instance = Root(...)
# export_stats_to_csv(root_instance)
