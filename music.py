# Import Modules
import pygame
import tkinter as tkr
import os

player = tkr.Tk()

player.title(" Audio Player ")
player.geometry("205x340")

# Playlist Register
os.chdir("E:\neeraj\playlist")
print(os.getcwd)
songlist = os.listdir()

# Volume Input
VolumeLevel1 = tkr.Scale(player,from_=0.0, to_=1.0,orient = tkr.HORIZONTAL, resolution = 0.1)


#Playlist Input
playlist = tkr.Listbox(player, highlightcolor='blue', selectmode = tkr.SINGLE)
print(songlist)
for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos = pos + 1

def Play():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(VolumeLevel1.get())
    print(pygame.mixer.music.get_volume())
    print(VolumeLevel1.get())

def ExitPlayer():
    pygame.mixer.music.stop()

def Pause():
    pygame.mixer.music.pause()

def UnPause():
    pygame.mixer.music.unpause()


button1 = tkr.Button(player, width=5, height=3, text='PLAY', command=Play )
button2 = tkr.Button(player, width=5, height=3, text='STOP', command=ExitPlayer )
button3 = tkr.Button(player, width=5, height=3, text='PAUSE', command=Pause )
button4 = tkr.Button(player, width=5, height=3, text='UNPAUSE', command=UnPause )

var = tkr.StringVar()
songtitle = tkr.label(player, textvariable=var)


# Play Widgets
button1.pack(fill='x')
button2.pack(fill='x')
button3.pack(fill='x')
button4.pack(fill='x')
songlist.pack()
VolumeLevel1.pack(fill='x')
playlist.pack(fill="both" , expand="yes")

player.mainloop()
