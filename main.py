import urllib.request
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from time import sleep
import shutil
import wget
import os


url = "http://mp3-red.org/album/8880942/carriere-d-honneur-retirada-vol-1.html"

hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win32; x84)' }

req = urllib.request.Request(url, headers=hdr)
response = urllib.request.urlopen(req)
# response.read()

soup = BeautifulSoup(response)

tracks = soup.find_all("div", {"class": "player"})

# track = tracks[0]
# track_url = track.get("data-mp3url")
# track_title = track.get("data-title") + ".mp3"
# track_download_url = "http://mp3-red.org{}".format(track_url)

# r = requests.get(track_download_url, stream=True, headers={'User-agent': 'Mozilla/5.0'})
# if r.status_code == 200:
#     with open(track_title, 'wb') as f:
#         r.raw.decode_content = True
#         shutil.copyfileobj(r.raw, f)

for track in tracks:

    track_url = track.get("data-mp3url")
    track_title = track.get("data-title")
    track_download_url = "http://mp3-red.org{}".format(track_url)

    print(track_title, track_download_url)