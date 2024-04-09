import streamlit as st
import pandas as pd

#123
# 创建一个示例DataFrame
data = {
    'Name': ['John', 'Jane', 'Michael', 'Emma', 'Sophia'],
    'Age': [25, 30, 35, 28, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}

df = pd.DataFrame(data)

# 使用Streamlit创建一个交互式应用
st.title('DataFrame 数据处理')

# 显示原始的 DataFrame 数据
st.subheader('原始数据')
st.dataframe(df)

# 显示 DataFrame 的描述统计信息
st.subheader('描述统计信息')
st.write(df.describe())

# 显示 DataFrame 中的某一列
selected_column = st.selectbox('选择要显示的列', df.columns)
st.subheader(f'显示 {selected_column} 列')
st.write(df[selected_column])

# 根据条件过滤 DataFrame
age_threshold = st.slider('选择年龄阈值', min_value=0, max_value=100, value=30, step=1)
st.subheader(f'年龄大于 {age_threshold} 的人')
filtered_df = df[df['Age'] > age_threshold]
st.write(filtered_df)