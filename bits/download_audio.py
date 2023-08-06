import re
from pytube import Playlist

YOUTUBE_STREAM_AUDIO = '140' # modify the value to download a different stream
DOWNLOAD_DIR = './data/videos'

# the first playlist
playlist = Playlist('https://www.youtube.com/playlist?list=PLTuuW2RV9qWmYn-JY1dEHbLYslDsjonWM')
# the second playlist
#playlist = Playlist('https://www.youtube.com/playlist?list=PLTuuW2RV9qWkP2X_hFG2CMehm67L4y4SH')

playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

print(len(playlist.video_urls))

for url in playlist.video_urls:
    print(url)

# actually download the audio track
for video in playlist.videos:
    audioStream = video.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
    audioStream.download(output_path=DOWNLOAD_DIR)