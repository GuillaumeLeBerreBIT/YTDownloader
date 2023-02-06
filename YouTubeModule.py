#/usr/bin/python3
##############################################
# IMPORTING NECASSARY MODULES
##############################################
from pytube import YouTube, Playlist, Channel

##############################################
# FUNCTIONS
##############################################
# This makes it that it can download a link from a video provided.

def Download(link):
    # This is to create a YouTube object
    yt = YouTube(link)
    yt = yt.streams.get_highest_resolution()

    try:
        print(yt.title)
        yt.download()
        print("Task succesfull!\n" + '-'*30)
    except:
        print("There has been error downloading!")

# With this function you can practically download a Playlsit from YouTube
def PLayDownload(link):
    # This is to create a YouTube Object
    p = Playlist(link)
    
    try:
        print("Downloading: {}".format(p.title))
        for video in p.videos:
            print(video.title)
            resolution = video.streams.get_highest_resolution()
            resolution.download()
        print("Task succesfull!\n" + '-'*30)
    except:
        print("There has been error downloading!")

