from pytube import YouTube


# YouTube('https://www.youtube.com/watch?v=7avPoMhQxX8&list=PLj7RUk5mYgYpZb-dDuTmlFGYJ72Gjgrdv&index=143&ab_channel=blewoo').streams.first().download()
yt = YouTube('https://youtu.be/09jkJlwdRd8?si=BFlTsOo5ruD1KmdY')
print(yt)
# print("Initialdata :", yt.initial_data)
print("Metadata: ", yt.publish_date)
print("Author:", yt.author)
print("Title: ",yt.title)
# for each mp4 file need to put these info
# yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

list = ['https://youtu.be/09jkJlwdRd8?si=Sw6emIE1zNMyaYj2','https://youtu.be/BgKlvthYvXY?si=y1O6EA49BUPVavxk']
for i in list:
    print(i)
    yt = YouTube(i)
    title = yt.title.replace(":","_",10).replace(";","_",10).replace(" ","_",10)
    date = str(yt.publish_date.date())
    filename = f"{title}_{date}.mp4"
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(filename=filename)
    # yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(filename="New WorldForged in AeternumPlayStyles2022112")
   
