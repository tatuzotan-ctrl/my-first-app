import streamlit as st
import random
import time

# ページ設定
st.set_page_config(page_title="猫スロット", page_icon="🐾")

# タイトルと説明
st.title("🐈 ニャンコ・スロット 🐾")
st.write("3つ同じ絵柄が揃ったらラッキー！")

# スロットの絵柄候補
symbols = ["🐱", "🐟", "🧶", "🐾", "🔔", "🌟"]

# セッション状態の初期化（リール停止位置の保持）
if 'reels' not in st.session_state:
    st.session_state.reels = ["❓", "❓", "❓"]

# スロット表示用のコンテナ
cols = st.columns(3)
placeholders = [cols[0].empty(), cols[1].empty(), cols[2].empty()]

# 初期の表示
for i in range(3):
    placeholders[i].markdown(f"<h1 style='text-align: center;'>{st.session_state.reels[i]}</h1>", unsafe_allow_html=True)

# [span_0](start_span)修正ポイント: use_column_width を use_container_width に変更[span_0](end_span)
if st.button("🐈 SPIN! (スロットを回す) 🐾", use_container_width=True):
    # 演出用のループ
    for _ in range(10):
        temp_reels = [random.choice(symbols) for _ in range(3)]
        for i in range(3):
            placeholders[i].markdown(f"<h1 style='text-align: center;'>{temp_reels[i]}</h1>", unsafe_allow_html=True)
        time.sleep(0.1)

    # 最終的な結果を決定
    st.session_state.reels = [random.choice(symbols) for _ in range(3)]
    
    # 結果を表示
    for i in range(3):
        placeholders[i].markdown(f"<h1 style='text-align: center;'>{st.session_state.reels[i]}</h1>", unsafe_allow_html=True)

    # 判定
    if st.session_state.reels[0] == st.session_state.reels[1] == st.session_state.reels[2]:
        st.balloons()
        st.success(f"おめでとう！ {st.session_state.reels[0]} が揃ったニャ！")
    else:
        st.info("残念！もう一度挑戦してニャ。")

st.markdown("---")
st.caption("Created with Streamlit 🎈")
