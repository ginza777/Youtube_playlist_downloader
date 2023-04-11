import re
import time

from pytube import Playlist
from pytube import  YouTube
from tqdm import tqdm
from time import sleep
#




links=[]
n=int(input("playlist sonini kiriting: "))
for i in range(n):
    link=input(f"{i+1} chi linkni kiriting:")
    links.append(link)


for link in links:
    playlist = Playlist(link)
    print("playlist nomi:",playlist.title)
    DOWNLOAD_DIR=playlist.title
    soni=len(playlist.video_urls)
    print("videolar soni:" ,soni)

    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")


    i=1

    for j in tqdm(range(soni), desc="downloading"):
        url=playlist.video_urls[j]
        youtube = YouTube(url)
        video = youtube.streams.get_highest_resolution()
        video.download(output_path=DOWNLOAD_DIR)
        i=i+1
        time.sleep(0.01)

    print("completed !")


