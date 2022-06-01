from pytube import YouTube

DOWNLOAD_FOLDER = "H:\\dump"

def start(url,key):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download(DOWNLOAD_FOLDER,str(key)+".mp4")
    return True
    