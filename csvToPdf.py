import csv
import os

def main():
    folder = input('enter the folder name: ')


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
                                f"{tds} TD{'s' if sacks != '1' else ''} and {ints} INT{'s' if sacks != '1' else ''}, {sacks} sack{'s' if sacks != '1' else ''} taken, and a {qbr} QBR" )
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
            formatted_string = ( f"{name} - {attempts} touches for {yards} yards, {ypc} yards per carry" + 
                                f"{' and {tds} TD' if tds != '0' else '' }{'s' if int(tds) > 1 else ''}" )
            final_string += formatted_string
            final_string += '\n'
    return final_string

def receivingString(foldername: str, filename: str):
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
                                f"{' and {tds} TD' if tds != '0' else '' }{'s' if int(tds) > 1 else ''}" )
            final_string += formatted_string
            final_string += '\n'
    return final_string

def kickingStats():
    pass

def puntingStats(foldername: str, filename: str):
    final_string = ''
    with open(os.path.join(foldername, filename), mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['name']
            punts = row['p']
            yards = row['y']
            avg = row['a']
            in20 = row['i']
            formatted_string = f"{name} - {punts} punts for {yards} yards, {avg} average yards per punt, and {in20} punts that landed in the 20\n"
            final_string += formatted_string
    return final_string

def blockingStats(foldername: str, filename: str):
    final_string = ''
    with open(os.path.join(foldername, filename), mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['pan'] != '' or row['sacks'] != '':
                name = row['name']
                pancakes = row['pan']
                sacks = row['sacks']
                formatted_string = f"{name} - {pancakes} pancake{'s' if pancakes != '1' else ''}, {sacks} sack{'s' if pancakes != '1' else ''} allowed\n"
                final_string += formatted_string
    return final_string

def defenseString(foldername: str):
    pass

def krString(foldername: str, filename: str):
    final_string = ''
    with open(os.path.join(foldername, filename), mode='r', newline='') as file: 
        reader = csv.DictReader(file) 
        for row in reader: 
            if row['kr'] != '':
                attempts = row['kr'] 
                name = row["name"] 
                yards = row["kry"] 
                longest = row["krl"] 
                average = float(yards)/float(attempts)
                tds = row["td"] if row['krtd'] != '' else '0'
                formatted_string = ( f"{name} - {attempts} returns for {yards} yards, {average} yards per carry, and a longest return of {longest}" + 
                                    f"{' and {tds} TD' if tds != 0 else '' }{'s' if int(tds) > 1 else ''}" )
                final_string += formatted_string
                final_string += '\n'
    return final_string

def prString(foldername: str, filename: str):
    final_string = ''
    with open(os.path.join(foldername, filename), mode='r', newline='') as file: 
        reader = csv.DictReader(file) 
        for row in reader: 
            if row['pr'] != '':
                attempts = row['pr'] 
                name = row["name"] 
                yards = row["pry"] 
                longest = row["prl"] 
                average = float(yards)/float(attempts)
                tds = row["td"] if row['prtd'] != '' else '0'
                formatted_string = ( f"{name} - {attempts} returns for {yards} yards, {average} yards per carry, and a longest return of {longest}" + 
                                    f"{' and {tds} TD' if tds != 0 else '' }{'s' if int(tds) > 1 else ''}" )
                final_string += formatted_string
                final_string += '\n'
    return final_string

if __name__ == '__main__':
    main()