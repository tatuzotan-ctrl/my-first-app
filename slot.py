import streamlit as st
import random
import time

# --- ページ設定（iPhoneで見やすく） ---
st.set_page_config(page_title="にゃんこスロット", page_icon="🐈")

# タイトル
st.title("🐈 にゃんこスロット 🐾")

# スロットに使う猫の絵文字リスト
cats = ["😺", "😸", "😻", "😽", "🐈", "🐾", "🐟"]

# --- 運用設計：セッション状態の管理 ---
# ストリームリットはボタンを押すたびにコードが最初から実行されるため、
# 前回のスロットの結果を「セッション状態」として保存しておく必要があります。
if 'reel1' not in st.session_state:
    st.session_state['reel1'] = cats[0]
if 'reel2' not in st.session_state:
    st.session_state['reel2'] = cats[1]
if 'reel3' not in st.session_state:
    st.session_state['reel3'] = cats[2]
if 'message' not in st.session_state:
    st.session_state['message'] = "「SPIN」を押してにゃんこを揃えてね！"

# --- UIレイアウト（スロット表示部分） ---
# 大きな文字で中央寄せにするためのCSS
st.markdown("""
    <style>
    .big-font {
        font-size:100px !important;
        font-weight: bold;
        text-align: center;
        margin: 20px 0;
    }
    .msg-font {
        font-size:24px !important;
        text-align: center;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# 3つのリールを横並びに表示
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(f'<p class="big-font">{st.session_state["reel1"]}</p>', unsafe_allow_html=True)
with c2:
    st.markdown(f'<p class="big-font">{st.session_state["reel2"]}</p>', unsafe_allow_html=True)
with c3:
    st.markdown(f'<p class="big-font">{st.session_state["reel3"]}</p>', unsafe_allow_html=True)

# メッセージ表示
st.markdown(f'<p class="msg-font">{st.session_state["message"]}</p>', unsafe_allow_html=True)

# --- メインロジック（スロットを回すボタン） ---
# iPhoneで押しやすいよう、横幅いっぱいの大きなボタンにする
if st.button("🐈 SPIN! (スロットを回す) 🐾", use_column_width=True):
    # ドラムロール的な演出（少し待たせる）
    with st.spinner("にゃんこが走っています..."):
        time.sleep(1.0) # 1秒待つ
        
        # ランダムに猫を選ぶ
        r1 = random.choice(cats)
        r2 = random.choice(cats)
        r3 = random.choice(cats)
        
        # 結果をセッション状態に保存（これで画面が更新される）
        st.session_state['reel1'] = r1
        st.session_state['reel2'] = r2
        st.session_state['reel3'] = r3
        
        # --- 当たり判定 ---
        if r1 == r2 == r3:
            st.session_state['message'] = f"🎉 🎉🎉 大当たり！ {r1} が揃ったにゃ！ 🎉🎉🎉"
            st.balloons() # 風船飛ばす
        elif r1 == r2 or r1 == r3 or r2 == r3:
            st.session_state['message'] = "🐾 惜しい！2つ揃ったにゃ！あと少し！ 🐾"
        else:
            st.session_state['message'] = "🐟 残念...また挑戦してにゃ！ 🐟"
            
    # 画面を再読み込みして結果を反映
    st.rerun()

# --- フッター（プロデューサーへの敬意） ---
st.markdown("---")
st.caption("Produced by マスター (Powered by AI assistant)")
