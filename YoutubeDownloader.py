from tkinter import *
from pytube import YouTube
import getpass

user = getpass.getuser()

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.iconbitmap('ico\\youtube.ico')
root.title("Youtube video downloader")

Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()

link = StringVar()

Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 53,textvariable = link,justify="center").place(x = 32, y = 90)

def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download('C:\\Users\\'+user+'\\Downloads')
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)  

Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)

root.mainloop()