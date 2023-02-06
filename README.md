# YTDownloader
This is a Python script to download YouTube videos and playlists with a Command Line Interface (CLI). The script uses the pytube module to perform the download tasks.

Usage
usage: youtube.py [-h] [-f] [-p] url

YouTube Download

positional arguments:
  url         Give a singular url of the YouTube video.

optional arguments:
  -h, --help  show this help message and exit
  -f, --f     Provide a file containing all the links of the YouTube videos
  -p, --p     Give the link of a PLaylist
The script accepts either a single URL, a file containing multiple URLs or a playlist URL. When downloading a playlist, all videos in the playlist will be downloaded.

Options
-f, --f: This option is used to specify a file containing all the links of the YouTube videos that you want to download. The links should be separated by a new line.

-p, --p: This option is used to specify the link of a YouTube playlist that you want to download. All videos in the playlist will be downloaded.

Requirements
The script requires pytube module to be installed. You can install it by running pip install pytube.

Output
The downloaded videos will be stored in a Videos folder in the current working directory.

Examples
Downloading a single video:
python youtube.py https://www.youtube.com/watch?v=jNQXAC9IVRw

Downloading videos from a file:
python youtube.py -f file.txt

Downloading a playlist:
python youtube.py -p https://www.youtube.com/watch?v=jNQXAC9IVRw&list=PL_jNQXAC9IVRw_
