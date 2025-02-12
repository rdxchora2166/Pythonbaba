from pytubefix import YouTube
import os

yt =  YouTube("https://youtu.be/L3jBzTbzjY0?si=tPblgqRoSR9jGHZL")

video = yt.streams.filter(only_audio=True).first()

# video = yt.streams.get_highest_resolution()

out_file = video.download( )

# save the file
base, ext = os.path.splitext(out_file)
new_file = base + '.mp4'
os.rename(out_file, new_file)

# result of success
print(yt.title + " has been successfully downloaded.")