# importing the required modules
from pytube import YouTube
import os

# asking user to enter the link
link = input("Enter Video Link: ")

# setting the download path (default path is the downloads folder)
download_folder = os.path.join(os.path.expanduser("~"), "downloads")

# using try and except to catch errors while downloading
try:
    yt = YouTube(link)

   # list the available video streams with both video and audio
    available_streams = []
    for stream in yt.streams:
        if "video" in stream.mime_type and stream.includes_audio_track:
            available_streams.append(stream)

    # sort the available streams based on resolution
    available_streams = sorted(
        available_streams, key=lambda x: int(x.resolution[:-1]))

    # print the sorted list of available video qualities with audio
    print("Available Video Qualities (with audio):")
    for stream in available_streams:
        print(
            f"{stream.resolution} - {stream.mime_type} - includes audio: {stream.includes_audio_track}")

    # download the highest resolution stream with both video and audio
    stream = available_streams[-1]
    # stream.download(output_path=download_folder)

    print("Downloaded Successfully!")
except Exception as e:
    print("Download Failed! - Exception: ", e)
