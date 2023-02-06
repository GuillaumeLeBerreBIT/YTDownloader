#/usr/bin/python3
##############################################
# IMPORTING NECASSARY MODULES
##############################################

import os, argparse 
import YouTubeModule as ytmod

##############################################
# COMMAND LINE INTERFACE
##############################################

parser = argparse.ArgumentParser(description='YouTube Download')                       
parser.add_argument('url', type=str, help='Give a singular url of the YouTube video.')
parser.add_argument('-f', '--f', action = 'store_true' ,required = False, help='Provide a file containing all the links of the YouTube videos')
parser.add_argument('-p', '--p',action = 'store_true' ,required = False, help='Give the link of a PLaylist')                                   
args = parser.parse_args()

##############################################
# Art
##############################################
print('\n██████╗ ██╗   ██╗████████╗██╗   ██╗██████╗ ███████╗\n\
██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║   ██║██╔══██╗██╔════╝\n\
██████╔╝ ╚████╔╝    ██║   ██║   ██║██████╔╝█████╗  \n\
██╔═══╝   ╚██╔╝     ██║   ██║   ██║██╔══██╗██╔══╝  \n\
██║        ██║      ██║   ╚██████╔╝██████╔╝███████╗\n\
╚═╝        ╚═╝      ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝\n')

##############################################
# MAIN BODY OF THE CODE
##############################################

if args.f == True:
    flag = 1

elif args.p == True:
    flag = 2

else:
    flag = 0

# Get the link from the command line in a variable
link = args.url

# Get the current working directory
wd = os.getcwd()
# Make a path if not exist and change to the path
if not os.path.isdir("Videos"):
    os.mkdir("Videos")
    os.chdir("Videos")
else: 
    os.chdir("Videos")

print('\n' + '='*25 + "\nPROCESSING LINKS\n" + '='*25)

if flag == 0:
    print("Downloading: {}".format(link))
    # Download Object to get the video
    ytmod.Download(link)

elif flag == 1: 
    # Opening the file with links
    file = wd + '/' + link
    
    with open(file, 'r') as read_file:
        reader = read_file.readlines()
        # Iterating over the list of urls
        for url in reader:
            print("Downloading: {}".format(url))
            ytmod.Download(url)

elif flag == 2:
    print("Downloading: {}".format(link))
    # Download Object to get the video
    ytmod.PLayDownload(link)


