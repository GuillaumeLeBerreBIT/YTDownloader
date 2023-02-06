# YTDownloader

This is a simple YouTube downloader in python, which takes in a YouTube video link as input and downloads the video to your system.

## Description

* Downloads a single video by providing the link in command line argument.
* Downloads multiple videos by providing a file containing all the links of the YouTube videos.
* Downloads a YouTube playlist by providing the link to the playlist in the command line argument.

### Dependencies

* Python3
* Pytube3
* Argparse

## Getting Started

To start using this YouTube downloader, follow these steps:
* Clone or download the repository.
* Navigate to the folder containing the source code.
* Run the following command in terminal/command prompt to install the required dependencies:

### Installing

```
pip3 install pytube3 argparse
```

### Executing program

Run the following command to download a video:
```
python3 YouTubeDown.py <YouTube video link>
```

To download multiple videos, provide a file containing all the links and run the following command:
```
python3 YouTubeDown.py -f <file name with extension>
```

To download a YouTube playlist, run the following command:
```
python3 YouTubeDown.py -p <YouTube playlist link>
```
## Help

Any advise for common problems or issues.
```
python3 YouTubeDown.py -h
```

## Authors

Guillaume Le Berre  
BIT

## Version History

* 0.1
    * Initial Release

