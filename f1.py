from tkinter import *
from tkinter import filedialog 
#from moviepy import *
#from moviepy.editor import VideoFileClip
#from pytube import YouTube
import shutil

screen = Tk()

title = screen.title("Yt mpp3")
#screen.iconbitmap("youtube.png")
canvas = Canvas(screen , width  =  500, height = 500)
canvas.pack()

logo_im= PhotoImage(file = "SVDR.png")
logo_im = logo_im.subsample(2,2)

canvas.create_image(250,80, image = logo_im)

link_feild = Entry(screen, width = 60 )
link_label = Label(screen , text = "Enter the youtube link", font = ('Helvetica' , 15 ))

canvas.create_window(250, 150 , window = link_label)
canvas.create_window(250,  220, window = link_feild)

path_label = Label(screen , text = "Select the path for download", font = ("Helvetica", 15))
select_btn = Button(screen , text = "Select" )

canvas.create_window(250, 270, window = path_label)
canvas.create_window(250, 300, window = select_btn )


#dwnld = PhotoImage("download.png")
dwnld_btn = Button(screen , text = "Download" , font = ("Helvetica", 15))
canvas.create_window(250,390, window = dwnld_btn)

screen.mainloop() # infinite loop for program