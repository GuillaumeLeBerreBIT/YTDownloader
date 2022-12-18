#/usr/bin/python3
########################################
# Installing a python youtube Downloader

# Importint the module
from pytube import YouTube

'''
# Where to save the video
save_path = "/home/guest/Videos"

# Link to the viedo to be downloaded
link = input("Give a YouTube link: ")
vid_name = input("Name to save the file: ")

try:
    #Object creation using YouTube
    #Which was imported in the beginning
    yt = YouTube(link)

except:
    print("Connection Error")   #To handle exception

# Filter all the files with "mp4" extension
mp4files = yt.filter('mp4')

#Set the filename to save the video
yt.set_filemane(vid_name)

# Get the video with the extension and
# Resolution passed in the get() function

d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)
try:
    #Downloading the video
    d_video.download(save_path)
except:
    print("Some Error!")

print("Task completed!")
'''

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