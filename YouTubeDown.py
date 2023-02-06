#/usr/bin/python3
########################################
# Installing a python youtube Downloader

# Importint the module
from pytube import YouTube

def Download(link):
    yt_vid = YouTube(link)
    yt_vid = yt_vid.streams.get_highest_resolution()

    try:
        yt_vid.download()
    except:
        print("There has been error downloading!")
    print("Task succesfull!")

link = input("Give a link to the YT video: ")
Download(link)