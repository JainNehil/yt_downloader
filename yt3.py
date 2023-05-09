from pytube import YouTube


link = input("Enter url : ")
yt_1= YouTube(link)

#print("title : " , yt_1.title)
#print(yt_1.thumbnail_url)

video = yt_1.streams.all()
vid = list(enumerate(video))
for  i in vid:
    print(i)

strm = int(input("Enter : "))
video[strm].download()

print("Done.")