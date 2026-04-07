import streamlit as st
import random
import os

st.title("マスターのランダム画像ギャラリー")

# --- 運用設計：自動ファイルスキャン ---
# app.pyと同じ場所にあるファイルの中から、画像っぽい拡張子だけを自動で抜き出します
target_extensions = [".jpg", ".jpeg", ".png", ".gif", ".webp"]
images_list = [f for f in os.listdir(".") if os.path.splitext(f)[1].lower() in target_extensions]

st.write(f"現在、倉庫（GitHub）には {len(images_list)} 枚の画像があります。")

if st.button("画像をランダムに表示"):
    if len(images_list) > 0:
        chosen_image = random.choice(images_list)
        st.image(chosen_image, caption=f"表示中: {chosen_image}", use_column_width=True)
        st.balloons()
    else:
        st.error("倉庫に画像ファイルが見当たりません。GitHubに画像をアップロードしてください。")
