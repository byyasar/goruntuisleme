import re
import pytube
from pytube import Playlist
from pytube import Caption
from pytube import YouTube
import os
import random

caption_list = []
index = 0

#ink = input('ses kodu\n')
YOUTUBE_STREAM_AUDIO = '251' # modify the value to download a different stream
DOWNLOAD_DIR = 'D:\\flutterders1\\'

playlist = Playlist('https://www.youtube.com/playlist?list=PLrWGe5fM0LZ4Iin0j-zOl-KXYjWJkj9Fs')


# this fixes the empty playlist.videos list
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
#print(len(playlist.video_urls))
print(playlist.video_urls)
'''for i in range (len(playlist.video_urls)):
    try:
        youtube=pytube.YouTube(playlist[i])
       #streams=youtube.streams.all()
        audioStream =  youtube.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
        audioStream.download(output_path=DOWNLOAD_DIR)
        videoAdi = audioStream.title
        yeniDosyaAdi = videoAdi.replace("/","")
        yeniDosyaAdi = videoAdi.replace(".","")
        try:
            yeniIsım,ext = os.path.splitext(DOWNLOAD_DIR+yeniDosyaAdi+".webm")
            os.rename(DOWNLOAD_DIR+yeniDosyaAdi+".webm",DOWNLOAD_DIR+videoAdi+".mp3")
        except FileExistsError:
            rndSayi = random.randint(0,99)
            yeniIsım,ext = os.path.splitext(DOWNLOAD_DIR+yeniDosyaAdi+".webm")
            os.rename(DOWNLOAD_DIR+yeniDosyaAdi+".webm",DOWNLOAD_DIR+videoAdi+str(rndSayi)+".mp3")
    except Exception as e:
        print('hata {}'.format(e))'''

