from tkinter import *
import tkinter as tk
from pytube import YouTube
import getpass
from tkinter import filedialog
from tkinter import messagebox
import os

user = getpass.getuser()

filename = 'C:\\Users\\'+user+'\\Downloads'

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    browse_text.set("loading...")
    global filename
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    way.set(filename)
    browse_text.set('Success')

root = Tk()
root.geometry('550x300')
root.resizable(0,0)
root.iconbitmap('ico\\youtube.ico')
root.title("Youtube video downloader")
root.config(bg='white')

folder_path = StringVar()

options = [ 
    "mp4", 
    "mp3"
] 

clicked = StringVar() 
clicked.set( "mp4" )

Label(root,text = 'Youtube Video Downloader', font ='Raleway 20 bold', bg = 'white').pack()

link = StringVar()
way = StringVar()

Label(root, text = 'Paste Link Here:', font = 'Raleway 15 bold', bg = 'white').place(x= 185 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link,justify="center", bg = '#eaeaea').place(x = 32, y = 90)
way_enter = Entry(root, width = 30,textvariable = way,justify="center", bg = '#eaeaea')
way.set(filename)
way_enter.place(x = 32, y = 125)
drop = OptionMenu( root , clicked , *options)
drop.config(bg='gray', activebackground='gray', activeforeground='white', font = 'Raleway 10', fg='white')
drop.place(x = 460, y = 82) 
browse_text = tk.StringVar()
button2 = Button(textvariable=browse_text, command=browse_button, width="10", bg = '#7197e7', activebackground='#80cee7', activeforeground='white', font = 'Raleway 11', fg = 'white')
browse_text.set("browse")
button2.place(x = 225, y = 120)

def Downloader():    
    choice = clicked.get() 
    folder = way.get()
    try:
        if choice == 'mp4':
                url =YouTube(str(link.get()))
                video = url.streams.first()
                try:
                    video.download(folder)
                    Label(root, text = 'downloaded', font = 'Raleway 15').place(x= 205 , y = 220)
                except:
                    tk.messagebox.showerror(title='error', message='You must try another folder.')
        
        else:
            url =YouTube(str(link.get()))
            video = url.streams.filter(only_audio=True).first()
            try:
                out_file = video.download(filename)

                base, ext = os.path.splitext(out_file) 
                new_file = base + '.mp3'
                os.rename(out_file, new_file) 
                Label(root, text = 'downloaded', font = 'Raleway 15').place(x= 205 , y = 220) 
            except:
                tk.messagebox.showerror(title='error', message='You must try another folder.')

             
    except:
        tk.messagebox.showerror(title='error', message='You must add link for video from youtube')

Button(root,text = 'download', font = 'Raleway 15' ,bg = '#21d2d2', activebackground='#21d2d2', activeforeground='white', fg="white", padx = 2, command = Downloader, height=1, width=10).place(x=205 ,y = 160)

root.mainloop()