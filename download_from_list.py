import yt_dlp

ydl = yt_dlp.YoutubeDL({'outtmpl': '%(fulltitle)s.%(ext)s'})
filename = 'list.txt'

with open(filename) as infile:
   for row in infile:
      ydl.download(row)
