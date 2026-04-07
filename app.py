import streamlit as st

st.title("ハロー、マスター！")
st.write("これは、記念すべき最初の自作Webアプリです。")
st.write("30年のプロの経験と、AIという新しい腕の融合、ここから始まりますね！")

if st.button("お祝いのメッセージを表示"):
    st.balloons()  # 画面に風船が飛びます
    st.success("デプロイ成功、おめでとうございます！")
