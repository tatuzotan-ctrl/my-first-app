import streamlit as st
import random
import time
import base64

# ページ設定
st.set_page_config(page_title="猫スロット", page_icon="🐾")

# 音源ファイルをBase64エンコードする関数
def get_audio_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# 音源の準備（エラー回避のためtry-exceptを入れています）
try:
    click_b64 = get_audio_base64("click.mp3")
    fanfare_b64 = get_audio_base64("fanfare.mp3")
except:
    click_b64 = ""
    fanfare_b64 = ""

st.title("🐈 ニャンコ・スロット 🐾")

# セッション状態
if 'reels' not in st.session_state:
    st.session_state.reels = ["❓", "❓", "❓"]
if 'spin_count' not in st.session_state:
    st.session_state.spin_count = 0
if 'do_spin' not in st.session_state:
    st.session_state.do_spin = False

symbols = ["🐱", "🐟", "🧶", "🐾", "🔔", "🌟"]

# スロット表示
cols = st.columns(3)
placeholders = [cols[0].empty(), cols[1].empty(), cols[2].empty()]

for i in range(3):
    placeholders[i].markdown(f"<h1 style='text-align: center;'>{st.session_state.reels[i]}</h1>", unsafe_allow_html=True)

# --- iPhone対応: JavaScriptボタン ---
# Streamlitのボタンではなく、HTMLのボタンを使うことでクリックの瞬間に音を鳴らします
st.components.v1.html(f"""
    <div style="display: flex; justify-content: center;">
        <button id="spin_btn" style="
            width: 100%; 
            padding: 15px; 
            background-color: #ff4b4b; 
            color: white; 
            border: none; 
            border-radius: 10px; 
            font-size: 18px; 
            font-weight: bold;
            cursor: pointer;
        ">🐈 SPIN! (スロットを回す) 🐾</button>
    </div>
    
    <audio id="snd_click" src="data:audio/mp3;base64,{click_b64}"></audio>
    <audio id="snd_fanfare" src="data:audio/mp3;base64,{fanfare_b64}"></audio>

    <script>
        const btn = document.getElementById('spin_btn');
        const sndClick = document.getElementById('snd_click');
        
        btn.addEventListener('click', function() {{
            // 1. クリック音を即座に再生（ユーザー操作に直結）
            sndClick.play();
            
            // 2. Streamlit側に「ボタンが押された」ことを通知
            window.parent.postMessage({{type: 'streamlit:setComponentValue', value: true}}, '*');
        }});
    </script>
""", height=70)

# JSボタンが押されたあとの処理
# 注意: この「値を受け取る」部分は少し特殊なため、簡易的にセッションをトリガーにします
if st.button("（更新を反映させる）", use_container_width=True):
    st.session_state.do_spin = True

if st.session_state.do_spin:
    st.session_state.do_spin = False # フラグリセット
    st.session_state.spin_count += 1
    
    # 演出
    for _ in range(10):
        temp_reels = [random.choice(symbols) for _ in range(3)]
        for i in range(3):
            placeholders[i].markdown(f"<h1 style='text-align: center;'>{temp_reels[i]}</h1>", unsafe_allow_html=True)
        time.sleep(0.08)

    # 確率操作ロジック
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

    for i in range(3):
        placeholders[i].markdown(f"<h1 style='text-align: center;'>{st.session_state.reels[i]}</h1>", unsafe_allow_html=True)

    unique_symbols = len(set(st.session_state.reels))
    
    if unique_symbols == 1:
        # ファンファーレ再生（JSを再度注入）
        st.components.v1.html(f"""
            <script>
                var audio = new Audio("data:audio/mp3;base64,{fanfare_b64}");
                audio.play();
            </script>
        """, height=0)
        st.balloons()
        st.success(f"おめでとう！ {st.session_state.reels[0]} が揃ったニャ！")
    elif unique_symbols == 2:
        st.warning("惜しい！あと一歩だニャ！")
    else:
        st.info("残念！もう一度挑戦してニャ。")

st.markdown("---")
st.caption("iPhoneで音が鳴らない場合は、本体横の消音スイッチ（マナーモード）をオフにしてください。")
