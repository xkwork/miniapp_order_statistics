import pandas as pd
import streamlit as st

st.title("商品数量汇总")

uploaded_file = st.file_uploader("选择要上传的 Excel 文档", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    grouped = df.groupby(["提货点/配送门店", "商品名称"]).size().reset_index(name='数量')
    st.write(grouped)
