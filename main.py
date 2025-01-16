import os

# Add FFmpeg path to the system PATH dynamically
os.environ["PATH"] += r";C:\Users\madal\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg.Essentials_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-7.1-essentials_build\bin"

# Validate FFmpeg accessibility
ffmpeg_test = os.system("ffmpeg -version")
if ffmpeg_test != 0:
    raise EnvironmentError("FFmpeg is not accessible!")

import sys

from src.VideoProcessor import VideoProcessor

sys.path.append('./src')


def main(video_url):
    processor = VideoProcessor(video_url)
    processor.process_video()
    processor.make_demo()

if __name__ == "__main__":
    # video_url = "https://www.youtube.com/watch?v=MTWkfpa-jJw"
    #video_url ="https://youtu.be/6n4NSRi-gPY?si=UFJZvdghqgujoH9l"
    video_url="https://www.youtube.com/watch?v=cK7G8eSvso4&t=24s&ab_channel=MindStreamMedia"
    main(video_url)
