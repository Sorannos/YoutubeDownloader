from tkinter import *
from pytube import YouTube
import getpass
from tkinter import filedialog

user = getpass.getuser()

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    global filename
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)

root = Tk()
root.geometry('550x300')
root.resizable(0,0)
root.iconbitmap('ico\\youtube.ico')
root.title("Youtube video downloader")

folder_path = StringVar()

options = [ 
    "mp4", 
    "mp3"
] 

clicked = StringVar() 
clicked.set( "mp4" )

Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()

link = StringVar()

Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 185 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link,justify="center").place(x = 32, y = 90)

drop = OptionMenu( root , clicked , *options ).place(x = 460, y = 82) 
button2 = Button(text="Browse", command=browse_button, width="10").place(x = 250, y = 120)

def Downloader():    
    choice = clicked.get() 
    if choice == 'mp4':
        url =YouTube(str(link.get()))
        video = url.streams.first()
        video.download(filename)
        Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 205 , y = 220)  
        
    else:
        url =YouTube(str(link.get()))
        video = url.streams.filter(only_audio=True).first()
        video.download(filename)
        Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 205 , y = 220)

Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=205 ,y = 160)

root.mainloop()