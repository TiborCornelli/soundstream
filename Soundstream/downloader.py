from pytube import YouTube
import os

def download(url: str, destination: str) -> None:
    yt: str = YouTube(url)
    video: object = yt.streams.filter(only_audio=True).first()
    out_file: str = video.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file: str = base + '.mp3'
    os.rename(out_file, new_file)