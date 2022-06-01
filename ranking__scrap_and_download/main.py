from datetime import datetime
import time
import threading
import scraping, db, UT_get

change_flag = False

def scrapping():

    global change_flag

    def functions():
        
        # 데이터를 긁어옴
        ass = scraping.today_all_rank_data()

        # DB에 전송
        for TT in ass:
            key = db.song_data_insert(TT)
            db.song_data_url(key,TT)
            db.save_daily(key,TT)
            print("Save Complete",key,TT)

    date = 0

    while(1):
        
        # 30분마다 실행하게끔
        time.sleep(60*30)

        now = datetime.now()
        if(date!=now.date()):
            date = now.date()

            functions()
            
            print("Save Complete")

            change_flag = True

def youtube_download():

    ax = db.media_not_downloaded_cheack()
    
    if(len(ax)>0):

        for rr in ax:
            
            print(URL,KEY)

            URL,KEY = rr[1], rr[0]

            UT_get.start(URL,KEY)
            
            time.sleep(5)

#youtube_download()
#def song_data_sort():
#def UT_download():

#print("현재 : ", now)
#print("현재 날짜 : ", now.date())
#print("현재 시간 : ", now.time())
#print("timestamp : ", now.timestamp())
#print("년 : ", now.year)
#print("월 : ", now.month)
#print("일 : ", now.day)
#print("시 : ", now.hour)
#print("분 : ", now.minute)
#print("초 : ", now.second)
#print("마이크로초 : ", now.microsecond)
#print("요일 : ", now.weekday())
#print("문자열 변환 : ", now.strftime('%Y-%m-%d %H:%M:%S'))