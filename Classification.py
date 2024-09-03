import streamlit as st
import cv2

def main():
    # 设置页面标题
    st.title("Video Player App")

    # 上传视频文件
    video_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])

    # 创建一个按钮，并使其居中显示
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        play_video = st.button("Play Video")

    if video_file is not None:
        # 读取视频文件
        video_bytes = video_file.read()

        # 创建一个容器用于显示视频
        video_container = st.empty()

        if play_video:
            # 如果按钮被按下，则显示视频
            video_container.video(video_bytes)
        else:
            # 如果按钮未被按下，则显示提示信息
            st.write("Click the button to play the video.")

if __name__ == "__main__":
    main()
