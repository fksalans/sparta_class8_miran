import requests
from bs4 import BeautifulSoup             

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)


soup = BeautifulSoup(data.text, 'html.parser')

#print(soup)

#old_content > table > tbody > tr:nth-child(2) > td.title > div > a  
#old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img
#old_content > table > tbody > tr:nth-child(2) > td.point

movies = soup.select('#old_content > table > tbody > tr')
#print(movies)

rank = 1;

for movie in movies:
    title = movie.select_one('td.title > div > a')
    grade = movie.select_one('td.point')

    if title is not None:
        rank += 1
        print(rank, title.text, grade.text)
