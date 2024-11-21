import csv
import os
from dataclasses import dataclass

def main():
    folder = input('enter the folder name: ')
    gameData = gameMetadata(folder)
    h_passing = passingString(folder, "h_stats_passing.csv")
    a_passing = passingString(folder, "a_stats_passing.csv")
    h_rushing = rushingString(folder, "h_stats_rushing.csv")
    a_rushing = rushingString(folder, "a_stats_rushing.csv")
    h_receiving = receivingString(folder, "h_stats_receiving.csv")
    a_receiving = receivingString(folder, "a_stats_receiving.csv")
    h_blocking = blockingString(folder, "h_stats_other.csv")
    a_blocking = blockingString(folder, "a_stats_other.csv")
    h_defense = f"{gameData['hMascot']} - " + defenseString(folder, 'h_stats_def.csv')
    a_defense = f"{gameData['aMascot']} - " + defenseString(folder, "a_stats_def.csv")
    h_defense_players = defensivePlayers(folder, 'h_stats_def.csv')
    a_defense_players = defensivePlayers(folder, 'a_stats_def.csv')
    h_def_players = defensivePlayerString(h_defense_players)
    a_def_players = defensivePlayerString(a_defense_players)
    h_kicking = kickingString(folder, "h_stats_kicking.csv")
    a_kicking = kickingString(folder, "a_stats_kicking.csv")
    h_punting = puntingString(folder, "h_stats_punting.csv")
    a_punting = puntingString(folder, "a_stats_punting.csv")
    h_kr = krString(folder, "h_stats_st.csv")
    a_kr = krString(folder, "a_stats_st.csv")
    h_pr = prString(folder, "h_stats_st.csv")
    a_pr = prString(folder, "a_stats_st.csv")
    toPdf(folder, gameData, h_passing, a_passing, h_rushing, a_rushing, h_receiving, a_receiving, h_blocking, a_blocking, h_defense, a_defense, h_def_players, a_def_players, h_kicking, a_kicking, h_punting, a_punting, h_kr, a_kr, h_pr, a_pr)

def toPdf(folder, gameData, h_pass, a_pass, h_rush, a_rush, h_rec, a_rec, h_block, a_block, h_def, a_def, h_def_player, a_def_player, h_kick, a_kick, h_punt, a_punt, h_kr, a_kr, h_pr, a_pr):
    with open(os.path.join(folder, "writeup.txt"), mode='w') as file:
        file.write(f"{gameData['hMascot']} VS {gameData['aMascot']}\n\nSummary TBD\n\n" +
f"OFFENSE\n\nPassing:\n{gameData['hMascot']}: \n{h_pass}\n\n{gameData['aMascot']}: \n{a_pass}\n\nTakeaways: TBD\n\n" +
f"Rushing:\n{gameData['hMascot']}: \n{h_rush}\n\n{gameData['aMascot']}: \n{a_rush}\n\nTakeaways: TBD\n\n" +
f"Receiving\n{gameData['hMascot']}: \n{h_rec}\n\n{gameData['aMascot']}: \n{a_rec}\n\nTakeaways: TBD\n\n" +
f"Blocking\n{gameData['hMascot']}: \n{h_block}\n\n{gameData['aMascot']}: \n{a_block}\n\nTakeaways: TBD\n\n\n" +
f"DEFENSE\n\nSo uh there’s a whole lot of stats for this, so I’m going to break it down into team stats and note down some important players and what stats they got\n____________________________________________________________________________\n\n" +
f"{gameData['hMascot']}: \n{h_def}\n\n{h_def_player}\n{gameData['aMascot']}: \n{a_def}\n\n{a_def_player}\nBig Takeaways: TBD\n\n\n" +
f"SPECIAL TEAMS\n\nKicking:\n{gameData['hMascot']}: \n{h_kick}\n\n{gameData['aMascot']}: \n{a_kick}\n\nPunting:\n{gameData['hMascot']}: \n{h_punt}\n\n{gameData['aMascot']}: \n{a_punt}\n\nTakeaways: TBD\n\n\n" +
f"Kick Returns:\n{gameData['hMascot']}:  \n{h_kr}\n\n{gameData['aMascot']}: \n{a_kr}\n\nPunt Returns:\n{gameData['hMascot']}: \n{h_pr}\n\n{gameData['aMascot']}: \n{a_pr}\n\nTakeaways: TBD\n\nFinal Notes: TBD")
    pass

@dataclass
class defensivePlayer:
    id: int
    name: str
    t: int
    tfl: int
    sack: int
    ff: int
    fr: int
    pd: int
    i: int
    safety: int
    td: int
    bp: int
    bxp: int
    bfg: int

    def WAG_points(this) -> float:
        return (.75 * this.t) + (2.5 * this.tfl) + (3 * this.sack) + (4 * this.ff) + (2 * this.fr) + (1.25 * this.pd) + (6 * this.i) + (6 * this.safety) + (8 * this.td) + (6 * (this.bp + this.bxp)) + (7 * this.bxp)
    
    def check_plural(stat, name, ending, singular=''):
        if stat > 1:
                return f"{name}{ending}"
        return f"{name}{singular}"
    
    def getString(this) -> str:
        fullString = f"{this.name} - "
        fullString += f"{this.t} {this.check_plural(this.t, 'tackle','s')}, " if this.t > 0 else ""
        fullString += f"{this.tfl} {this.check_plural(this.tfl, 'tackle', 's')} for loss, " if this.tfl > 0 else ""
        fullString += f"{this.sack} {this.check_plural(this.sack, 'sack', 's')}, " if this.sack > 0 else ""
        fullString += f"{this.ff} {this.check_plural(this.ff, 'forced fumble', 's')}, " if this.ff > 0 else ""
        fullString += f"{this.fr} {this.check_plural(this.fr, 'fumble', 's')} recovered, " if this.fr > 0 else ""
        fullString += f"{this.pd} {this.check_plural(this.pd, 'pass', 'es')} deflected, " if this.pd > 0 else ""
        fullString += f"{this.i} {this.check_plural(this.i, 'interception')}, " if this.i > 0 else ""
        fullString += f"{this.safety} {this.check_plural(this.safety, 'safet', 'ies', singular='y')}, " if this.safety > 0 else ""
        fullString += f"{this.td} {this.check_plural(this.td, 'defensive touchdown', 's')}, " if this.td > 0 else ""
        fullString += f"{this.bp} {this.check_plural(this.bp, 'blocked punt', 's')}, " if this.bp > 0 else ""
        fullString += f"{this.bxp} {this.check_plural(this.bxp, 'blocked extra point', 's')}, " if this.bxp > 0 else ""
        fullString += f"{this.bfg} {this.check_plural(this.bfg, 'blocked field goal', 's')}, " if this.bfg > 0 else ""
        
        if fullString.endswith(', '): 
            fullString = fullString[:-2]
        return fullString

def gameMetadata(foldername: str) -> dict:
    important = {}
    with open(os.path.join(foldername, "game_metadata.csv"), mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            important['hMascot'] = row['hMascot']
            important['aMascot'] = row['aMascot']
            important['hAbb'] = row['hAbb']
            important['aAbb'] = row['aAbb']
            important['oPOG'] = row['oPOG']
            important['dPOG'] = row['dPOG']
    return important

def passingString(foldername: str, filename: str) -> str:
    final_string = ''
    with open(os.path.join(foldername, filename), mode='r', newline='') as file: 
        reader = csv.DictReader(file) 
        for row in reader: 
            name = row["name"] 
            comp = row["c"] 
            att = row["a"] 
            comp_percentage = row["per"] 
            yards = row["y"] 
            tds = row["td"] if row['td'] != '' else '0'
            ints = row["i"] if row["i"] != '' else "0"
            sacks = row["sacked"] if row['sacked'] != '' else '0'
            qbr = row["r"] 
            formatted_string = ( f"{name} - {comp}/{att}, {comp_percentage}% completion percentage, {yards} yards, " +
                                f"{tds} TD{'s' if tds != '1' else ''} and {ints} INT{'s' if tds != '1' else ''}, {sacks} sack{'s' if sacks != '1' else ''} taken, and a {qbr} QBR" )
            final_string += formatted_string
            final_string += '\n'
    return final_string

def rushingString(foldername: str, filename: str) -> str:
    final_string = ''
    with open(os.path.join(foldername, filename), mode='r', newline='') as file: 
        reader = csv.DictReader(file) 
        for row in reader: 
            name = row["name"] 
            attempts = row["a"] 
            yards = row["y"] 
            ypc = row["avg"] 
            tds = row["td"] if row['td'] != '' else '0'
            formatted_string = ( f"{name} - {attempts} touch{'es' if attempts != '1' else ''} for {yards} yards, {ypc} yards per carry" + 
                                f"{f' and {tds} TD' if tds != '0' else '' }{'s' if int(tds) > 1 else ''}" )
            final_string += formatted_string
            final_string += '\n'
    return final_string

def receivingString(foldername: str, filename: str) -> str:
    final_string = ''
    with open(os.path.join(foldername, filename), mode='r', newline='') as file: 
        reader = csv.DictReader(file) 
        for row in reader: 
            name = row["name"] 
            catches = row["c"]
            targets = row['tar'] 
            yards = row["y"] 
            tds = row["td"] if row['td'] != '' else '0'
            formatted_string = ( f"{name} - {catches}/{targets} for {yards} yards" + 
                                f"{f' and {tds} TD' if tds != '0' else '' }{'s' if int(tds) > 1 else ''}" )
            final_string += formatted_string
            final_string += '\n'
    return final_string

def kickingString(foldername: str, filename: str) -> str:
    final_string = ''
    with open(os.path.join(foldername, filename), mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            hasBeenUsed = False
            name = row['name']
            formatted_string = f"{name} - "
            if row['xpa'] != '':
                xpm = row['xpm'] if row['xpm'] != '' else '0'
                xpa = row['xpa']
                formatted_string += f"{xpm}/{xpa} on xps"
                hasBeenUsed = True
            if row['fga_u20'] != '':
                fga = row['fga_u20']
                fgm = row['fgm_u20'] if row['fgm_u20'] != '' else '0'
                formatted_string += f"{', 'if hasBeenUsed else ''}{fgm}/{fga} on fgs under 20"
                hasBeenUsed = True
            if row['fga_2029'] != '':
                fga = row['fga_2029']
                fgm = row['fgm_2029'] if row['fgm_2029'] != '' else '0'
                formatted_string += f"{', 'if hasBeenUsed else ''}{fgm}/{fga} on fgs from 20-29"
                hasBeenUsed = True
            if row['fga_3039'] != '':
                fga = row['fga_3039']
                fgm = row['fgm_3039'] if row['fgm_3039'] != '' else '0'
                formatted_string += f"{', 'if hasBeenUsed else ''}{fgm}/{fga} on fgs from 30-39"
                hasBeenUsed = True
            if row['fga_4049'] != '':
                fga = row['fga_4049']
                fgm = row['fgm_4049'] if row['fgm_4049'] != '' else '0'
                formatted_string += f"{', 'if hasBeenUsed else ''}{fgm}/{fga} on fgs from 40-49"
                hasBeenUsed = True
            if row['fga_50'] != '':
                fga = row['fga_50']
                fgm = row['fgm_50'] if row['fgm_50'] != '' else '0'
                formatted_string += f"{', 'if hasBeenUsed else ''}{fgm}/{fga} on fgs above 50"
            formatted_string += "\n"
            final_string += formatted_string
    return final_string

def puntingString(foldername: str, filename: str) -> str:
    final_string = ''
    with open(os.path.join(foldername, filename), mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['name']
            punts = row['p']
            yards = row['y']
            avg = row['a']
            in20 = row['i']
            formatted_string = f"{name} - {punts} punts for {yards} yards, {avg} average yards per punt, and {in20} punt{'s' if in20 != '1' else ''} that landed in the 20\n"
            final_string += formatted_string
    return final_string

def blockingString(foldername: str, filename: str) -> str:
    final_string = ''
    with open(os.path.join(foldername, filename), mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['pan'] != '' or row['sacks'] != '':
                name = row['name']
                pancakes = row['pan'] if row['pan'] != '' else '0'
                sacks = row['sacks'] if row['sacks'] != '' else '0'
                formatted_string = f"{name} - {pancakes} pancake{'s' if pancakes != '1' else ''}, {sacks} sack{'s' if pancakes != '1' else ''} allowed\n"
                final_string += formatted_string
    return final_string

def defenseString(foldername: str, filename: str) -> str:
    final_string = ''
    tackles = 0
    tfl = 0
    sack = 0
    ff = 0
    fr = 0
    pd = 0
    i = 0
    safety = 0
    td = 0
    bp = 0
    bxp = 0
    bfg = 0

    with open(os.path.join(foldername, filename), mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            t = row['t'] if row['t'] != '' else '0'
            tfls = row['tfl'] if row['tfl'] != '' else '0'
            sacks = row['s'] if row['s'] != '' else '0'
            ffs = row['ff'] if row['ff'] != '' else '0'
            frs = row['fr'] if row['fr'] != '' else '0'
            pds = row['pd'] if row['pd'] != '' else '0'
            ints = row['i'] if row['i'] != '' else '0'
            safeties = row['sf'] if row['sf'] != '' else '0'
            touchdowns = row['td'] if row['td'] != '' else '0'
            blockP = row['bp'] if row['bp'] != '' else '0'
            blockXP = row['bxp'] if row['bxp'] != '' else '0'
            blockFG = row['bfg'] if row['bfg'] != '' else '0'
            tackles += int(t)
            tfl += int(tfls)
            sack += int(sacks)
            ff += int(ffs)
            fr += int(frs)
            pd += int(pds)
            i += int(ints)
            safety += int(safeties)
            td += int(touchdowns)
            bp += int(blockP)
            bxp += int(blockXP)
            bfg += int(blockFG)
    final_string += f"{tackles} tackles, {tfl} tackle{'s' if tfl > 1 else ''} for loss, {sack} sack{'s' if sack > 1 else ''}, {ff}/{fr} forced fumble{'s' if ff > 1 else ''}/recovered fumble{'s' if fr > 1 else ''}, {pd} pass{'es' if pd > 1 else ''} deflected, {i} int{'s' if i != 1 else ''}"
    if safety > 0:
        final_string += f", {safety} safet{'y' if safety == 1 else 'ies'}"
    if td > 0:
        final_string += f", {td} touchdown{'s' if td > 1 else ''}"
    if bp > 0:
        final_string += f", {bp} blocked punt{'s' if bp > 1 else ''}"
    if bxp > 0:
        final_string += f", {bxp} blocked extra point{'s' if bxp > 1 else ''}"
    if bfg > 0:
        final_string += f", {bfg} blocked field goal{'s' if bfg > 1 else ''}"
    return final_string

def defensivePlayers(foldername: str, filename: str) -> list[defensivePlayer]:
    allStats = []
    with open(os.path.join(foldername, filename), mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            t = row['t'] if row['t'] != '' else '0'
            tfl = row['tfl'] if row['tfl'] != '' else '0'
            sack = row['s'] if row['s'] != '' else '0'
            ff = row['ff'] if row['ff'] != '' else '0'
            fr = row['fr'] if row['fr'] != '' else '0'
            pd = row['pd'] if row['pd'] != '' else '0'
            i = row['i'] if row['i'] != '' else '0'
            safety = row['sf'] if row['sf'] != '' else '0'
            td = row['td'] if row['td'] != '' else '0'
            bp = row['bp'] if row['bp'] != '' else '0'
            bxp = row['bxp'] if row['bxp'] != '' else '0'
            bfg = row['bfg'] if row['bfg'] != '' else '0'
            player = defensivePlayer(row['id'], row['name'], int(t), int(tfl), int(sack), int(ff), int(fr), int(pd), int(i), int(safety), int(td), int(bp), int(bxp), int(bfg))
            allStats.append(player)
    return allStats

def defensivePlayerString(players: list[defensivePlayer]) -> str:
    final_string = 'Standout players (including but not limited to) - \n'
    players.sort(key=defensivePlayer.WAG_points, reverse=True)
    for x in range(3):
        final_string += f"{players[x].getString}\n"
    return final_string

def krString(foldername: str, filename: str) -> str:
    final_string = ''
    with open(os.path.join(foldername, filename), mode='r', newline='') as file: 
        reader = csv.DictReader(file) 
        for row in reader: 
            if row['kr'] != '':
                attempts = row['kr'] 
                name = row["name"] 
                yards = row["kry"] if row['kry'] != '' else '0'
                longest = row["krl"] if row['krl'] != '' else '0'
                average = round(float(yards)/float(attempts), 2)
                tds = row["krt"] if row['krt'] != '' else '0'
                formatted_string = ( f"{name} - {attempts} returns for {yards} yards, {average} yards per carry, and a longest return of {longest}" + 
                                    f"{f' and {tds} TD' if tds != '0' else '' }{'s' if int(tds) > 1 else ''}" )
                final_string += formatted_string
                final_string += '\n'
    return final_string

def prString(foldername: str, filename: str) -> str:
    final_string = ''
    with open(os.path.join(foldername, filename), mode='r', newline='') as file: 
        reader = csv.DictReader(file) 
        for row in reader: 
            if row['pr'] != '':
                attempts = row['pr'] 
                name = row["name"] 
                yards = row["pry"] if row['pry'] != '' else '0'
                longest = row["prl"] if row['prl'] != '' else '0'
                average = round(float(yards)/float(attempts), 2)
                tds = row["prt"] if row['prt'] != '' else '0'
                formatted_string = ( f"{name} - {attempts} returns for {yards} yards, {average} yards per carry, and a longest return of {longest}" + 
                                    f"{f' and {tds} TD' if tds != '0' else '' }{'s' if int(tds) > 1 else ''}" )
                final_string += formatted_string
                final_string += '\n'
    return final_string


if __name__ == '__main__':
    main()