import streamlit as st
import random
import time
import base64

# --- 音声を再生するための関数（キャッシュ回避版） ---
def play_audio(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        # 毎回違うID（乱数）を振ることで、ブラウザに再実行を強制させる
        unique_id = random.randint(0, 1000000)
        md = f"""
            <audio autoplay="true" id="audio_{unique_id}">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        # st.empty() を使って確実に新しい要素として流し込む
        st.components.v1.html(md, height=0)

# ページ設定
st.set_page_config(page_title="猫スロット", page_icon="🐾")

st.title("🐈 ニャンコ・スロット 🐾")

# セッション状態の初期化
if 'reels' not in st.session_state:
    st.session_state.reels = ["❓", "❓", "❓"]
if 'spin_count' not in st.session_state:
    st.session_state.spin_count = 0

symbols = ["🐱", "🐟", "🧶", "🐾", "🔔", "🌟"]

cols = st.columns(3)
placeholders = [cols[0].empty(), cols[1].empty(), cols[2].empty()]

for i in range(3):
    placeholders[i].markdown(f"<h1 style='text-align: center;'>{st.session_state.reels[i]}</h1>", unsafe_allow_html=True)

# スロットを回すボタン
if st.button("🐈 SPIN! (スロットを回す) 🐾", use_container_width=True):
    # 1. クリック音を鳴らす（まずは音から！）
    try:
        play_audio("click.mp3") 
    except:
        pass
        
    st.session_state.spin_count += 1
    
    # 演出用のループ（少しディレイを調整）
    for _ in range(10):
        temp_reels = [random.choice(symbols) for _ in range(3)]
        for i in range(3):
            placeholders[i].markdown(f"<h1 style='text-align: center;'>{temp_reels[i]}</h1>", unsafe_allow_html=True)
        time.sleep(0.08) # 0.1より少し速くしてテンポアップ

    # 当たり判定ロジック
    if st.session_state.spin_count >= 10:
        win_symbol = random.choice(symbols)
        st.session_state.reels = [win_symbol, win_symbol, win_symbol]
        st.session_state.spin_count = 0
    else:
        if random.random() < 0.1:
            win_symbol = random.choice(symbols)
            st.session_state.reels = [win_symbol, win_symbol, win_symbol]
            st.session_state.spin_count = 0
        else:
            st.session_state.reels = [random.choice(symbols) for _ in range(3)]
            if st.session_state.reels[0] == st.session_state.reels[1] == st.session_state.reels[2]:
                st.session_state.spin_count = 0

    # 最終結果を表示
    for i in range(3):
        placeholders[i].markdown(f"<h1 style='text-align: center;'>{st.session_state.reels[i]}</h1>", unsafe_allow_html=True)

    unique_symbols = len(set(st.session_state.reels))
    
    if unique_symbols == 1:
        # 2. 揃った時にファンファーレを鳴らす
        try:
            play_audio("fanfare.mp3")
        except:
            pass
        st.balloons()
        st.success(f"おめでとう！ {st.session_state.reels[0]} が揃ったニャ！")
    elif unique_symbols == 2:
        st.warning("惜しい！あと一歩だニャ！")
    else:
        st.info("残念！もう一度挑戦してニャ。")

st.markdown("---")
st.caption("Created with Streamlit 🎈")
