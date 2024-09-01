import streamlit as st

def main():
    # 设置页面标题
    st.title("在线视频播放器")

    # 上传视频文件
    video_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])
    play_video = st.button("播放视频")
    
    if video_file is not None:
        if play_video:
        # 直接在 Streamlit 中显示视频
            st.video(video_file)
        else:
            st.write("按下按钮以播放视频")
            
if __name__ == "__main__":
    main()
