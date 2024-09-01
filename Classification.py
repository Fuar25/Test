import streamlit as st

def main():
    # 设置页面标题
    st.title("Video Player App")

    # 上传视频文件
    video_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])

    # 添加一些样式
    st.markdown(
        """
        <style>
        .centered-button {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh; /* 使按钮居中显示 */
        }
        .custom-button {
            background-color: #4CAF50; /* Green */
            border: none;
            color: white;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # 创建一个按钮，并使其居中显示
    st.markdown(
        """
        <div class="centered-button">
            <button class="custom-button" onclick="playVideo()">Play Video</button>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if video_file is not None:
        # 读取视频文件
        video_bytes = video_file.read()

        # 创建一个容器用于显示视频
        video_container = st.empty()

        # 使用 JavaScript 控制视频播放
        st.markdown(
            f"""
            <script>
            function playVideo() {{
                var videoContainer = document.getElementById('video-container');
                videoContainer.innerHTML = '<video controls autoplay><source src="data:video/mp4;base64,{video_bytes.decode()}" type="video/mp4"></video>';
            }}
            </script>
            """,
            unsafe_allow_html=True,
        )

if __name__ == "__main__":
    main()
