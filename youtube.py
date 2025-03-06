import yt_dlp

def download_video(video_url, resolution):
    # Ensure resolution is a valid number (e.g., '1080p' -> '1080')
    resolution = resolution.rstrip("p")

    ydl_opts = {
        'format': f'bestvideo[height<={resolution}]+bestaudio/best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ").strip()
    resolution = input("Enter the desired resolution (e.g., '720p'): ").strip()
    download_video(video_url, resolution)
