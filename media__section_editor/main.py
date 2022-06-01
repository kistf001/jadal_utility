import vlc
import time
import tkinter
import secreat

from tkinter import *

# import shoot as sh
tk = Tk()
tk.title("User Interface")

# 화면 가로 * 세로 크기 설정
tk.geometry("840x800") 
tk.configure(bg='floralwhite')

tk.mainloop()


# vlc media player 객체 생성
media_player = vlc.MediaPlayer()
 
# 뮤직비디오 파일
media_file = "H:\\dump\\2.mp4"
 
# 미디어 파일을 vlc 객체로 읽어들이기
media = vlc.Media(media_file)
 
# 읽어드린 미디어파일을 media_player 객체에 세팅하기(재생목록)
media_player.set_media(media)
 
# 영상 스케일 조정하기
media_player.video_set_scale(0.6)
print(f"(0) 영상스케일을 {media_player.video_get_scale()}으로 초기 조정")

media_player.play()
time.sleep(3)