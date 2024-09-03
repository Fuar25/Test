import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 创建三个标签页
tab1, tab2, tab3 = st.tabs(['Page 1', 'Page 2', 'Page 3'])

# 在第一个标签页中添加内容
with tab1:
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

# 在第二个标签页中添加内容
with tab2:
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

# 在第三个标签页中添加内容
with tab3:
    st.title('Page 3')
    st.write('Welcome to Page 3!')

    # 添加一些数据展示
    st.subheader('Data Frame')
    df = pd.DataFrame({
        'first column': [201, 202, 203, 204],
        'second column': [2001, 2002, 2003, 2004]
    })
    st.dataframe(df)

    # 添加一个图表
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['p', 'q', 'r'])

    st.area_chart(chart_data)
