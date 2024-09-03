import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 初始化 session state
if 'page' not in st.session_state:
    st.session_state.page = 'Page 1'

# 侧边栏选择器
page = st.sidebar.selectbox("Select a page:", ['Page 1', 'Page 2', 'Page 3'])

# 根据选择的页面显示相应的内容
if page == 'Page 1':
    st.title('Page 1')
    st.write('Welcome to Page 1!')

    # 添加一些数据展示
    data = pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
    })
    st.dataframe(data)

    # 添加一个图表
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

elif page == 'Page 2':
    st.title('Page 2')
    st.write('Welcome to Page 2!')

    # 添加一些数据展示
    st.subheader('Data Frame')
    df = pd.DataFrame({
        'first column': [101, 102, 103, 104],
        'second column': [1001, 1002, 1003, 1004]
    })
    st.dataframe(df)

    # 添加一个图表
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['x', 'y', 'z'])

    st.bar_chart(chart_data)

else:
    st.title('Page 3')
    st.write('Welcome to Page 3!')
