import cv2
import streamlit as st
import numpy as np
from PIL import Image

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

        while True:
            ret, frame = video.read()
            if not ret:
                break

            # 在这里可以添加任何 OpenCV 图像处理代码
            # 例如，转换为灰度图像
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # 将 OpenCV 图像转换为 RGB
            rgb_frame = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2RGB)

            # 将 NumPy 数组转换为 PIL 图像
            pil_image = Image.fromarray(rgb_frame)

            # 在 Streamlit 中显示图像
            video_container.image(pil_image, channels="RGB")

        # 释放视频捕获对象
        video.release()
if __name__ == "__main__":
    main()
