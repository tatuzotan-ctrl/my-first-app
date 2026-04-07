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

# セッション状態の初期化
if 'reels' not in st.session_state:
    st.session_state.reels = ["❓", "❓", "❓"]
if 'spin_count' not in st.session_state:
    st.session_state.spin_count = 0  # 回した回数を記録

# スロット表示用のコンテナ
cols = st.columns(3)
placeholders = [cols[0].empty(), cols[1].empty(), cols[2].empty()]

# 初期の表示
for i in range(3):
    placeholders[i].markdown(f"<h1 style='text-align: center;'>{st.session_state.reels[i]}</h1>", unsafe_allow_html=True)

# 修正ポイント: ボタンの引数とロジック
if st.button("🐈 SPIN! (スロットを回す) 🐾", use_container_width=True):
    st.session_state.spin_count += 1
    
    # 演出用のループ
    for _ in range(10):
        temp_reels = [random.choice(symbols) for _ in range(3)]
        for i in range(3):
            placeholders[i].markdown(f"<h1 style='text-align: center;'>{temp_reels[i]}</h1>", unsafe_allow_html=True)
        time.sleep(0.1)

    # 10回に1回は強制的に揃える（天井機能）
    if st.session_state.spin_count >= 10:
        win_symbol = random.choice(symbols)
        st.session_state.reels = [win_symbol, win_symbol, win_symbol]
        st.session_state.spin_count = 0  # カウントをリセット
    else:
        # 通常時も1/10の確率で当たりやすく調整（あるいは完全ランダム）
        if random.random() < 0.1:
            win_symbol = random.choice(symbols)
            st.session_state.reels = [win_symbol, win_symbol, win_symbol]
            st.session_state.spin_count = 0
        else:
            st.session_state.reels = [random.choice(symbols) for _ in range(3)]
            # 偶然3つ揃ってしまった場合もカウントリセット
            if st.session_state.reels[0] == st.session_state.reels[1] == st.session_state.reels[2]:
                st.session_state.spin_count = 0

    # 最終結果を表示
    for i in range(3):
        placeholders[i].markdown(f"<h1 style='text-align: center;'>{st.session_state.reels[i]}</h1>", unsafe_allow_html=True)

    # 判定ロジック
    unique_symbols = len(set(st.session_state.reels))
    
    if unique_symbols == 1:
        # 3つ揃った場合
        st.balloons()
        st.success(f"おめでとう！ {st.session_state.reels[0]} が揃ったニャ！")
    elif unique_symbols == 2:
        # 2つ揃った場合（惜しい！）
        st.warning("惜しい！あと一歩だニャ！")
    else:
        # バラバラの場合
        st.info("残念！もう一度挑戦してニャ。")

st.markdown("---")
# デバッグ用（何回目か確認したい場合はコメントアウトを外してください）
# st.write(f"現在の試行回数: {st.session_state.spin_count}回目")
st.caption("Created with Streamlit 🎈")
