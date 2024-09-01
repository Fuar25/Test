import streamlit as st

def main():
    # 设置页面标题
    st.title("在线视频播放器")

    # 上传视频文件
    video_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])
    
    if video_file is not None:
        st.video(video_file)
            
if __name__ == "__main__":
    main()
