# https://www.youtube.com/watch?v=eKgfEA4PTTI
# Import the required Libraries
import tkinter as tk
from pytube import YouTube

# Setup the screen
win = tk.Tk()
win.geometry("600x200")
win.config(bg="gray")
win.title('YouTube Video Downloader') 

# Video Downloading function
def Download():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    tk.Label(win,text='Your Video is downloaded!',fg="White",bg="gray").place(x=10,y=140)  

link = tk.StringVar()
tk.Label(win,text='YouTube Link:',fg="White",bg="gray").place(x= 1, y = 50)
link_enter = tk.Entry(win, width = 53,textvariable = link, bg="white").place(x=5, y=100)
tk.Button(win,text='DOWNLOAD!!',fg="white",bg='black',padx=2,command=Download).place(x=385,y=140)
 
win.mainloop()