import streamlit as st

def main():
    # 设置页面标题
    st.title("Video Player App")
    
    # 添加一些样式
    st.markdown(
        """
        <style>
        .file-uploader {
            margin-top: 20px;
            margin-bottom: 20px;
        }
        .button-container {
            margin-top: 20px;
            margin-bottom: 20px;
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    # 创建三列布局
    col1, col2, col3 = st.columns([1, 4, 1])

    with col1:
        # 上传视频文件
        st.markdown("<div class='file-uploader'>", unsafe_allow_html=True)
        video_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        # 创建一个容器用于显示视频
        video_container = st.empty()

    with col3:
        # 创建一个按钮
        st.markdown("<div class='button-container'>", unsafe_allow_html=True)
        play_video = st.button("Play Video")
        
        # 显示提示信息
        if not play_video:
            st.write("Click the button to play the video.")
        st.markdown("</div>", unsafe_allow_html=True)

    if video_file is not None:
        if play_video:
            # 如果按钮被按下，则显示视频
            video_container.video(video_file)
        else:
            # 清空容器
            video_container.empty()

if __name__ == "__main__":
    main()
