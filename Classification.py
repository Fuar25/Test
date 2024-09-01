import cv2
import streamlit as st
import numpy as np


def main():
    st.title("Video Processing with OpenCV")

    # 上传视频文件
    video_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])

    if video_file is not None:
        # 读取视频文件
        video_bytes = video_file.read()

        # 使用 OpenCV 读取视频
        video = cv2.VideoCapture(video_bytes)

        # 创建一个容器用于显示视频
        video_container = st.empty()

        # 释放视频捕获对象
        video.release()
if __name__ == "__main__":
    main()
