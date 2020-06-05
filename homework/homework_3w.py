import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

for page in range(1, 5):
    data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200530=N&pg='+str(page),headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
    for song in songs:
        rank_tags = song.select_one('td.number').contents
        # print(rank_tags)
        rank = None  #초기화
        if rank_tags and len(rank_tags) is not None:
            rank = rank_tags[0].strip() 
            title = song.select_one('td.info > a.title.ellipsis').text.strip()
            singer = song.select_one('td.info > a.artist.ellipsis').text.strip()
            print(rank, title, singer)
                                    

#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis