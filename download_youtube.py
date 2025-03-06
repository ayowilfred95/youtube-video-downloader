import os
import re
import ssl
import certifi
from pytube import YouTube
ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())

def is_valid_youtube_url(url):
    """Check if the given URL is a valid YouTube link."""
    youtube_regex = r"(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+"
    return re.match(youtube_regex, url) is not None

def download_video(video_url, resolution):
    try:
        if not is_valid_youtube_url(video_url):
            print("Invalid YouTube URL. Please enter a valid link.")
            return
        
        # Create a YouTube object
        yt = YouTube(video_url)
        
        # Print video details
        print(f'\nTitle: {yt.title}')
        print(f'Author: {yt.author}')
        print(f'Length: {yt.length} seconds')
        
        # List available resolutions
        print('\nAvailable resolutions:')
        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        available_resolutions = sorted(
            (stream.resolution for stream in streams if stream.resolution),
            key=lambda x: int(x[:-1]), reverse=True
        )

        for res in available_resolutions:
            print(res)

        # Filter streams by the desired resolution
        stream = yt.streams.filter(res=resolution, progressive=True, file_extension='mp4').first()
        
        if stream:
            os.makedirs("downloads", exist_ok=True)  # Ensure 'downloads' directory exists
            print(f'\nDownloading "{yt.title}" at {resolution}...')
            stream.download(output_path='downloads')
            print('Download completed!')
        else:
            print(f'\nResolution {resolution} is not available.')
            print('Please choose one of the available resolutions listed above.')
    except Exception as e:
        print(f'\nAn error occurred: {e}')

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ").strip()
    resolution = input("Enter the desired resolution (e.g., '720p'): ").strip()
    download_video(video_url, resolution)
