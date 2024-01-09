import tkinter as tk 
from tkinter import filedialog
import customtkinter as ctk
from pytube import YouTube, Playlist
from PIL import Image, ImageTk
import os

ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    
    def __init__(self):
        super().__init__()
        
        # Basic setup
        self.title("YouTube Downloader")
        self.geometry("1000x600")
        
        # Split up the window in 2 frames
        self.frame_picture = ctk.CTkFrame(self)
        self.frame_download = ctk.CTkFrame(self, fg_color = "#C4BA9A", border_color = '#978F75', border_width = 2) #FF393C
        # Place the 2 frames on the master window
        self.frame_picture.place(x = 0, y = 0, relwidth = 0.3, relheight = 1)
        self.frame_download.place(relx = 0.3, y = 0, relwidth = 0.7, relheight = 1)
        
        
        # How to add an image onto the window
        self.canvas_for_image = tk.Canvas(master = self.frame_picture, bg = 'red', width = 1024, height = 1024, highlightthickness = 0)
        self.canvas_for_image.pack()
        self.bg_downl = Image.open('images/YTB_bg.png')
        self.canvas_for_image.image = ImageTk.PhotoImage(self.bg_downl.resize((1024, 1024), Image.Resampling.LANCZOS))
        self.canvas_for_image.create_image(0, 0, image = self.canvas_for_image.image, anchor='nw')

        ## Download layout
        self.frame_download.columnconfigure((0,1), weight = 1)
        self.frame_download.rowconfigure((0,1,2,3,5,6,7,8), weight = 1)
        
        self.title_label = ctk.CTkLabel(master = self.frame_download, text = "YouTube Downloader", font = (None, 40, 'bold'), text_color = '#FFFFFF', fg_color = '#343638', corner_radius = 32)
        self.title_label.grid(row = 0, column = 0, columnspan = 2, sticky = "ew", padx = 50)
        
        ## Frame Download options + Progress   
        self.url_entry = ctk.CTkEntry(master = self.frame_download, placeholder_text = 'Video URL', fg_color="#343638", corner_radius = 32)
        self.url_entry.grid(row = 1, column = 0, columnspan = 2, sticky = "ew", padx = 50)    
        
        ## Choose directory to download the files
        self.current_dir = os.getcwd()
        self.dir_label = ctk.CTkLabel(master = self.frame_download, text = f"{self.current_dir}", fg_color="#343638", corner_radius = 32)
        self.dir_label.grid(row = 2, column = 0, columnspan = 2, sticky = "ew", padx = 50)
        self.dir_button = ctk.CTkButton(master = self.frame_download, text = 'Select Directory', command = self.get_directory)
        self.dir_button.grid(row = 3, column = 0, columnspan = 2, sticky = "ew", padx = 140)
        
        #If want to change how radio buttons are shown need to adjust the avoe which the dir label is far too long
        self.radio_var = tk.StringVar()  # Will convert any type of variable into a string
        self.download_stream_btn = ctk.CTkRadioButton(master = self.frame_download,
                                text = 'Download YT Stream',     # Default value automatically set is 0, when multiple buttons gets complicated
                                value = 'Stream',          # When a value is set and there are multiple radio buttons, it will now not trigger together
                                variable = self.radio_var,
                                text_color = '#343638')  # This will return the value 'radio 1'
        self.download_stream_btn.grid(row = 4, column = 0)
                                    
        self.download_playlist_btn = ctk.CTkRadioButton(master = self.frame_download,
                                text = 'Download YT Playlist',
                                value = 'Playlist',
                                variable = self.radio_var,   # Setting the same tk variable for 2nd radio button
                                text_color = '#343638')
        self.download_playlist_btn.grid(row = 4, column = 1)

        self.download_button = ctk.CTkButton(master = self.frame_download, text = 'Download', command = lambda: self.get_url())
        self.download_button.grid(row = 5, column = 0, columnspan = 2, sticky = "ew", padx = 140)
        
        self.finish_label = ctk.CTkLabel(master = self.frame_download, text = "")
        self.finish_label.grid(row = 6, column = 0, columnspan = 2, sticky = "ew", padx = 50)
        
        self.pPerc_label = ctk.CTkLabel(master = self.frame_download, text = '0 %', font = (None, 20), text_color = '#000000')
        self.pPerc_label.grid(row = 7, column = 0, columnspan = 2)
        
        self.progressbar = ctk.CTkProgressBar(master = self.frame_download, width = 200, height = 15)
        self.progressbar.set(0)
        self.progressbar.grid(row = 8, column = 0, columnspan = 2, sticky = "ew", padx = 50)
    
    
    def get_directory(self):
        filepath = filedialog.askdirectory(initialdir = f"{self.current_dir}", title = "Select direcotry to save downloaded content")
        self.dir_label.configure(text = f'{filepath}')
        self.current_dir = filepath
        
        
    def get_url(self):
        
        if self.radio_var.get() == 'Stream':
            # Download the video link
            self.download_vid(self.url_entry.get())
        
        elif self.radio_var.get() == 'Playlist':
            self.download_playlist(self.url_entry.get())
        
    def download_vid(self,link):
        # This is to create a YouTube object
        yt = YouTube(link, 
                on_progress_callback = self.on_progress,  # This is to work with a progress bar
                #on_complete_callback = complete_func  # After fully downlaoded post-download processing
                )
        # Link to the URL saved in a variable
        thumbnail = yt.thumbnail_url # Removing everything after '?' results in original image
        
        try: 
            # Get the highest resolution
            yt = yt.streams.get_highest_resolution()
            
            self.finish_label.configure(text = f'{yt.title}', fg_color="#343638", corner_radius = 32)
            # Download the video
            yt.download(f'{self.current_dir}')
            
        
        except:
            self.finish_label.configure(text = 'There has been error downloading!', fg_color="#343638", corner_radius = 32)
    
    def download_playlist(self, link):
        # This is to create a YouTube Object
        p = Playlist(link)
        
        try:
            # Get the total amount of videos
            total_vids = len(p.video_urls)
            vid_count = 0
            
            def update_progress():
                # Want to treat the variable to the outer scope under downlaod playlist not only within update_progress
                nonlocal vid_count
                # Since len starts from 1, but index from 0 last vid will lawyas be lower then len, once equal index means total vids downloaded and stop iteration
                if vid_count < total_vids:
                    
                    video = p.videos[vid_count]
                    # Get the highest stream
                    yt_stream = video.streams.get_highest_resolution()
                    # Change the label to title of video being downloaded
                    self.finish_label.configure(text = f'{video.title}', fg_color="#343638", corner_radius = 32)
                    # Downlaod the video
                    yt_stream.download(f'{self.current_dir}')
                    # Once download done increment counter
                    vid_count += 1

                    tot_per = vid_count / total_vids * 100
                    self.pPerc_label.configure(text = f'{str(int(tot_per))} %')
                    self.progressbar.set(float(tot_per / 100))
                
                    #Schedule the next update after 100 milliseconds
                    self.after(100, update_progress)
            
            update_progress()
                
        except:
            self.finish_label.configure(text = 'There has been error downloading!', fg_color="#343638", corner_radius = 32)
            
    def on_progress(self, video_stream, chunck, bytes_remaining):
        # Total size of the video
        total_size = video_stream.filesize
        # Get the bytes remaining
        bytes_downloaded = total_size - bytes_remaining
        # The perc complete of the video
        perc_complete = bytes_downloaded / total_size * 100
        # Convert to a string
        per = str(int(perc_complete))
        # Adjust the label to percentage
        self.pPerc_label.configure(text = f'{per} %', font = (None, 20), text_color = '#000000')
        self.pPerc_label.update()   # Update on every iteration
        
        # The progress bar part >> Value between 0 and 1
        self.progressbar.set(float(perc_complete / 100))
    
    
if __name__ == "__main__":      
    app = App()
    app.mainloop()