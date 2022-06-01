from bs4 import BeautifulSoup
import requests
import re

regex____today_all_rank_data = re.compile(r'\d\d\d\d\/\d+\/\d+')

def show(ffff_temp):
    print("===========================================")
    print("rank : ",ffff_temp['rank'])
    print("title : ",ffff_temp['title'])
    print("composer : ",ffff_temp['composer'])
    print("published : ",ffff_temp['published'])
    print("singer : ",ffff_temp['singer'])
    print("url : ",ffff_temp['url'])

def today_all_rank_data():
    
    url = "https://vocaloard.injpok.tokyo/"
    
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html5lib")
    
    tags = soup.select("html body div.mainrow main article div.article-body div.RankingItem")
    date = soup.select("html body div.mainrow main article header.article-header h1")

    ffff = []
    ffff_temp = []

    def date_changer(date):
        date = regex____today_all_rank_data.search(date[0].text).group()
        date = date.replace("/","-")
        return date

    date = date_changer(date)
    
    for tag  in tags:

        youtube_url = tag.find("a")["href"]

        explanation = tag.select("div.RankingItem a p")

        ffff_temp = {
            "rank":explanation[0].text,
            "title":explanation[2].text,
            "composer":explanation[-2].text,
            "published":explanation[-1].text.replace("/","-"),
            "singer":explanation[3].text,
            "url":youtube_url,
            "date":date
        }
        
        ffff.append(ffff_temp)

    return ffff
