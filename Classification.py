import streamlit as st

def main():
    # 设置页面标题
    st.title("Video Player App")

    # 上传视频文件
    video_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])

    if video_file is not None:
        # 直接在 Streamlit 中显示视频
        st.video(video_file)


if __name__ == "__main__":
    main()
