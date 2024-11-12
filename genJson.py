import json
import requests
import csv, os
import lzstring
import urllib3
urllib3.disable_warnings()

def gen_json(filenum: int, id: int, I_D: str, season: int):
    headers = {
        'Host': 'index.sim-football.com',
        'Sec-Ch-Ua': '"Not;A=Brand";v="24", "Chromium";v="128"',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.120 Safari/537.36',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': f'https://index.sim-football.com/{I_D}SFLS{season}/Boxscores/Boxscore.html?id={id}',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Priority': 'u=4, i',
    }
    response = requests.get(f'https://index.sim-football.com/{I_D}SFLS{season}/Boxscores/boxscoreData{filenum}.txt', headers=headers, verify=False)
    data = response.content.decode('utf-8')
    if data.startswith('\ufeff'):
        data = data[1:]
    if response.status_code == 200:
        # Decompress the content
        compressed_data = data
        decompressed_data = lzstring.LZString().decompressFromEncodedURIComponent(compressed_data)
        return(decompressed_data)
    else:
        print(f"Error: Received status code {response.status_code}")
