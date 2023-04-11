
import re
from pytube import Playlist
# url=input("linkni kiriting : ")
# print("downloading: ")
#
# youtube = YouTube(url)
# print(youtube.title)
# video = youtube.streams.get_highest_resolution()
# video.download(output_path='videolar')
# print("completed !")

from pytube import  YouTube

while True:
    url = input("linkni kiriting : ")
    print("video_nomi: ", YouTube(url).title)
    video=YouTube(url).streams.get_highest_resolution()
    print("hajmi: ", int(video.filesize/1024),"MB")
    video.download(output_path='Videoklip')





