import csv
from typing import List
import os
import collections
from collections import UserList

def write_to_csv(filename: str, objects: List, path, fieldnames=None):
    if not os.path.exists(path):
        os.makedirs(path)

    if fieldnames is None:
        fieldnames = UserList(objects[0].keys())

    with open(os.path.join(path, filename), mode='w', newline='') as file: 
        writer = csv.DictWriter(file, fieldnames=fieldnames) 
        writer.writeheader() 
        for obj in objects: 
            writer.writerow(obj)

def export_stats_to_csv(root: dict, path):
    passingHeaders = ['id', 'name', 'c', 'a', 'y', 'avg', 'td', 'i', 'r', 'per', 'sacked', 'sackedyards']
    rushingHeaders = ['id', 'name', 'a', 'y', 'avg', 'l', 'td']
    receivingHeaders = ['id', 'name', 'c', 'tar', 'y', 'avg', 'td', 'l']
    kickingHeaders = ['id', 'name', 'xpm', 'xpa', 'fga_u20', 'fgm_u20', 'fga_2029', 'fgm_2029', 'fga_3039', 'fgm_3039', 'fga_4049', 'fgm_4049', 'fga_50', 'fgm_50']
    puntingHeaders = ['id', 'name', 'p', 'y', 'a', 'l', 'i']
    STHeaders = ['id', 'name', 'kr', 'kry', 'krl', 'krt', 'pr', 'pry', 'prl', 'prt'] 
    #TODO: fix block xp for defense
    defenseHeaders = ['id', 'name', 't', 'tfl', 's', 'ff', 'fr', 'pd', 'i', 'sf', 'td', 'bp', 'bxp', 'bfg']
    otherHeaders = ['id', 'name', 'pen', 'y', 'pan', 'sacks']

    write_to_csv('a_stats_passing.csv', root['aStatsPassing'], path, passingHeaders)
    write_to_csv('a_stats_rushing.csv', root['aStatsRushing'], path, rushingHeaders)
    write_to_csv('a_stats_receiving.csv', root['aStatsReceiving'], path, receivingHeaders)
    write_to_csv('a_stats_kicking.csv', root['aStatsKicking'], path, kickingHeaders)
    write_to_csv('a_stats_punting.csv', root['aStatsPunting'], path, puntingHeaders)
    write_to_csv('a_stats_st.csv', root['aStatsST'], path, STHeaders)
    write_to_csv('a_stats_def.csv', root['aStatsDef'], path, defenseHeaders)
    write_to_csv('a_stats_other.csv', root['aStatsOther'], path, otherHeaders)

    write_to_csv('h_stats_passing.csv', root['hStatsPassing'], path, passingHeaders)
    write_to_csv('h_stats_rushing.csv', root['hStatsRushing'], path, rushingHeaders)
    write_to_csv('h_stats_receiving.csv', root['hStatsReceiving'], path, receivingHeaders)
    write_to_csv('h_stats_kicking.csv', root['hStatsKicking'], path, kickingHeaders)
    write_to_csv('h_stats_punting.csv', root['hStatsPunting'], path, puntingHeaders)
    write_to_csv('h_stats_st.csv', root['hStatsST'], path, STHeaders)
    write_to_csv('h_stats_def.csv', root['hStatsDef'], path, defenseHeaders)
    write_to_csv('h_stats_other.csv', root['hStatsOther'], path, otherHeaders)

    # Exporting game metadata
    game_data = {
        'id': root['id'],
        'hMascot': root.get('hMascot', None),
        'aMascot': root.get('aMascot', None),
        'hAbb': root.get('hAbb', None),
        'aAbb': root.get('aAbb', None),
        'h1Q': root.get('h1Q', None),
        'h2Q': root.get('h2Q', None),
        'h3Q': root.get('h3Q', None),
        'h4Q': root.get('h4Q', None),
        'hF': root.get('hF', None),
        'a1Q': root.get('a1Q', None),
        'a2Q': root.get('a2Q', None),
        'a3Q': root.get('a3Q', None),
        'a4Q': root.get('a4Q', None),
        'aF': root.get('aF', None),
        'oPOG': root['oPOG'],
        'dPOG': root['dPOG'],
        'aFD': root['aFD'],
        'hFD': root['hFD'],
        'aYds': root['aYds'],
        'hYds': root['hYds']
        # Add other relevant fields as needed
    }

    with open(os.path.join(path, 'game_metadata.csv'), mode='w', newline='') as file: 
        writer = csv.DictWriter(file, game_data.keys())
        writer.writeheader()
        writer.writerow(game_data)
