import streamlit as st
import pandas as pd

st.title("草加・散策マップ 🐾")

# 緯度・経度のデータを作成
data = pd.DataFrame({
    'lat': [35.8291, 35.8250], # 草加駅付近の緯度
    'lon': [139.8000, 139.8050] # 経度
})

# これだけで地図が出る！
st.map(data)
