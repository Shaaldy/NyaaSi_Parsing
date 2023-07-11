import requests
import re
from bs4 import BeautifulSoup as BS
from time import sleep



header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/99.0.0.0"}
base_url = "https://nyaa.si"

way = "D:\\Videos\\One Piece\\"

name = ["One Piece", "Horimiya", "Ayaka"]


def replace_parentheses(string):
    replaced_string = re.sub(r'\(', '[', string)
    replaced_string = re.sub(r'\)', ']', replaced_string)
    return replaced_string


def downloadTor(url, name, quality, subers):
    resp = requests.get(url=url, headers=header)

    r = open(way + name + f'[{quality}]' + f'[{subers}]' + '.torrent', "wb")

    for value in resp.iter_content(1024**2):
        r.write(value)
    #Yprint(resp.text)
    r.close()
    


def animeParsing():
    for count in range(1, 15):
        sleep(3)
        url = f"https://nyaa.si/?p={count}"

        response = requests.get(url, headers=header)

        soup = BS(response.text, "lxml")

        data = soup.find_all("tr", class_="success")

        for el in data: 
            torrentFile = base_url + el.find("td", class_="text-center").find("a").get("href")
            match = el.find_all("a", title=True)[-1].text
            match = replace_parentheses(match)
            yield match, torrentFile
            
        
def array():
    for match, torrentFile in animeParsing():
        match_subers = re.search(r'\[(.*?)\]', match)

        match_nameAnime = re.search(r'\](.*?)\s-', match)

        match_episode = re.search(r'-\s(\d{1,5})\s\[', match)

        match_q = re.search(r'\[(\d+p)\]', match)
    

        if match_subers and match_nameAnime and match_episode and match_q:

            subers, nameAnime, episode, quality = match_subers.group(1), match_nameAnime.group(1), match_episode.group(1), match_q.group(1)
            
            yield subers, nameAnime, episode, quality, torrentFile
        
            for anime in name:
                if anime in nameAnime:
                
                    print(" Сабы: {}\n Название: {}\n Номер эпизода: {}\n Качество: {}\n Ссылка {}\n".format(subers, nameAnime, episode, quality, torrentFile), '\n\n')
                    if ('1080p' in quality):
                        print(nameAnime + '\n' + "Номер эпизода " + episode + '\n' + subers + '\n' + "Хотите скачать данный эпизод? [Y/N]")
                        answer = input()
                        if answer == 'Y':
                            downloadTor(torrentFile, nameAnime, quality, subers)
                        else: print('\n' + 'Continue...' + '\n')


