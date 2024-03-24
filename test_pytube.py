from pytube.contrib.playlist import Playlist
from pytube import YouTube

#this one is for Play New World- Forged in Aeternum 
#  pl = Playlist(url='https://youtube.com/playlist?list=PLZK0wLfINcocJCorOYFzRgxC0RcBnOS1S&si=RuLI2iq9tY5SEkFl')
# folder = "Forged in Aeternum"

# this one is for Play New World - Dev updates
# pl = Playlist(url='https://youtube.com/playlist?list=PLZK0wLfINcoehm-WNRKpyd86_EV_Mh4v-&si=69Laj9khXkyAnD51')
# folder = "Dev Updates"

# this one is for Dashup 
# pl = Playlist(url='https://youtube.com/playlist?list=PLav6EACPY8gU6Wnag9rlIoE-_Iraefoc8&si=2YpH5loxTTsbXgJw')
# folder = "Dashup"

# this one is for Dashup 
# pl = Playlist(url='https://youtube.com/playlist?list=PLav6EACPY8gU6Wnag9rlIoE-_Iraefoc8&si=2YpH5loxTTsbXgJw')
# folder = "Dashup"

pl = Playlist(url='https://youtube.com/playlist?list=PLj7RUk5mYgYrT0soglXJqq0HujQimKB5K&si=N9vjxplRLgWUddKw')
folder = "Mixtape"

# urls = list(pl.url_generator())
# count = 0
for url in urls:
    # if count > 10:
    #     break
    print(url)
    yt = YouTube(url)
    title = yt.title.replace(":","_",10).replace(";","_",10).replace(" ","_",10).replace("!","").replace("?","")
    date = str(yt.publish_date.date())
    author = yt.author
    filename = f"{folder}/{author}_{title}_{date}.mp4"
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(filename=filename)
    # yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(filename="New WorldForged in AeternumPlayStyles2022112")
    # count += 1
 