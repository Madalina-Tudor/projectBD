import os
import csv
import cv2
import datetime
from tqdm import tqdm

from src.Demo import VideoEmotionProcessor
from src.FrameExtractor import FrameExtractor
from src.VideoAnalysis import VideoAnalysis
from src.VideoDownloader import VideoDownloader


class VideoProcessor:
    def __init__(self, video_url, frame_interval=10, frames_dir="saves"):
        self.video_url = video_url
        self.frame_interval = frame_interval
        self.frames_dir = frames_dir
        self.analysis = VideoAnalysis()
        self.demo = VideoEmotionProcessor(self.video_url)

    def process_video(self):
        downloader = VideoDownloader(self.video_url)
        video_path = downloader.download_video()

        extractor = FrameExtractor(video_path, self.frame_interval, self.frames_dir)
        frame_paths = extractor.extract_frames()

        self.analysis.process_frames(frame_paths)
    
    def make_demo(self):
        self.demo.process_video()
        self.demo.display_video()
