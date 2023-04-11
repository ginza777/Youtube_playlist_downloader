import re
import time

from pytube import Playlist
from pytube import  YouTube
from tqdm import tqdm
from time import sleep
#







link=input(f"linkni kiriting:")




playlist = Playlist(link)
print("playlist nomi:",playlist.title)
DOWNLOAD_DIR=str(input("papka nomini kiriting: "))
soni=len(playlist.video_urls)
print("videolar soni:" ,soni)

playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")




for j in tqdm(range(soni), desc="downloading"):
    try:
        url=playlist.video_urls[j]
        youtube = YouTube(url)
        video = youtube.streams.get_highest_resolution()
        video.download(output_path=DOWNLOAD_DIR)

        time.sleep(0.01)
    except:
        continue

print("completed !")


