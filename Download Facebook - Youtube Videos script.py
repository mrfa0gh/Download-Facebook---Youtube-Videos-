import pytube
import requests
import re
import pyfiglet
import time
import webbrowser
logo = pyfiglet.figlet_format("Download Videos By Ghalwash")
print(logo)
print("")


choice = input("What do you want to do?\n1) Open developer accounts\n2) Run script\n")


if choice == "1":
        webbrowser.open("http://t.me/mrfa0gh")
        webbrowser.open("https://www.instagram.com/mrfa0gh")
        webbrowser.open('https://twitter.com/mrfa0gh')
 
elif choice == "2":
        print("Script is running...")
else:
        print("Invalid choice.")

# Function to download a video from a YouTube link
def download_youtube_video(link):
    video = pytube.YouTube(link)
    print("Title: " + video.title)
    print("Length: " + str(video.length) + " seconds")
    print("Available quality options: ")
    # Get available quality options
    streams = video.streams.filter(progressive=True).all()
    for i in range(len(streams)):
        print(str(i+1) + ") " + str(streams[i]))
    # Prompt user to select quality
    selected_stream = streams[int(input("Select the quality you want to download: ")) - 1]
    # Download video
    print("Downloading...")
    selected_stream.download()
    print("Download complete!")

# Function to download a video from a Facebook link
def download_facebook_video(link):
    # Get video source code
    source_code = requests.get(link).text
    # Extract video URL
    video_url = re.search('hd_src:"(.+?)"', source_code).group(1)
    # Download video
    print("Downloading...")
    response = requests.get(video_url, stream=True)
    with open("video.mp4", "wb") as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    print("Download complete!")

# Prompt user for link and website
link = input("Enter the video link: ")
website = input("Enter the website (Y For YouTube  //  F For Facebook): ")

# Call appropriate function based on website input
if website.lower() == "y":
    download_youtube_video(link)
elif website.lower() == "f":
    download_facebook_video(link)
else:
    print("Invalid website input.")
