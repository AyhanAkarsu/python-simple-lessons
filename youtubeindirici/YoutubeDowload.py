from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube  import YouTube
import os

def konum():
    konum = filedialog.askdirectory()
    path_label.config(text=konum)

def indirme():
    Link = link.get()
    yt = YouTube(Link)
    folder = path_label.cget("text")
    uzanti = cmb.get()
    if uzanti == ".mp3":
        mp3 = yt.streams.filter(only_audio=True).first()
        cikis = mp3.download(folder)
        base, ext = os.path.splitext(cikis)
        to_mp3 = base + ".mp3"
        os.rename(cikis, to_mp3)
    elif uzanti == ".mp4":
        mp4 = yt.streams.get_highest_resolution().download(folder)


ekran = Tk()
baslik = ekran.title("Youtube İndirici")
canvas = Canvas(ekran,width=500,height=500)
canvas.pack()

yt_logo = PhotoImage(file="download.png")
canvas.create_image(250,95,image=yt_logo)

link = Entry(ekran,width=50)
lin_label = Label(ekran,text="Link Giriniz",font=("helwetica",12), fg="#911b13")
canvas.create_window(250,195,window=lin_label)
canvas.create_window(250,220,window=link)
path_button = Button(ekran,text="Konum Seçiniz",fg="white",bg="#911b13",command=konum)
canvas.create_window(250,300,window=path_button)
path_label = Label(ekran,text="...",font=("helwetica",12), fg="green")
canvas.create_window(250,260,window=path_label)
ayarlar = [".mp3",
           ".mp4"]
cmb = ttk.Combobox(ekran,values=ayarlar,width=10)
canvas.create_window(250,340,window=cmb)
dow_button = Button(ekran,text="İndir",fg="white",bg="#911b13",command=indirme)
canvas.create_window(250,375,window=dow_button)
ekran.mainloop()

