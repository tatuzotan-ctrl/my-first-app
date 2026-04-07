import streamlit as st
import random
import os

# アプリのタイトル
st.title("マスターのランダム画像ギャラリー")

# --- 運用設計：画像リストの定義 ---
# GitHubのリポジトリのルート（app.pyと同じ場所）にある画像ファイル名をリストにします。
# 【重要】自分がアップロードしたファイル名に書き換えてください！
images_list = [
    "cat01.jpg",      # 例：アルフォンス
    "cat02.jpg",      # 例：茶々丸
    "cat003.jpg"  # 例：DTMスタジオ
]

# --- メインロジック ---
st.write("ボタンを押すと、倉庫（GitHub）からランダムに画像を取り出して表示します。")

# ボタンを設置
if st.button("画像をランダムに表示"):
    # リストからランダムに1つ選択
    chosen_image = random.choice(images_list)
    
    # 画像を表示
    # use_column_width=True で横幅を画面に合わせます
    st.image(chosen_image, caption=f"表示中の画像: {chosen_image}", use_column_width=True)
    
    # お祝いの balloons も残しておきましょう（笑）
    st.balloons()
