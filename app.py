import streamlit as st
import random
import os
from PIL import Image

st.title("マスターのランダム画像ギャラリー")

# 倉庫（GitHub）の中をスキャン
target_extensions = [".jpg", ".jpeg", ".png", ".gif", ".webp"]
images_list = [f for f in os.listdir(".") if os.path.splitext(f)[1].lower() in target_extensions]

st.write(f"現在、倉庫には {len(images_list)} 枚の候補があります。")

if st.button("画像をランダムに表示"):
    if len(images_list) > 0:
        # 成功するまで最大10回チャレンジする（無限ループ防止）
        success = False
        for _ in range(10):
            chosen_image = random.choice(images_list)
            try:
                # 実際に画像が開けるかチェック
                img = Image.open(chosen_image)
                st.image(img, caption=f"表示中: {chosen_image}", use_column_width=True)
                st.balloons()
                success = True
                break # 成功したらループを抜ける
            except Exception as e:
                # ダメだった場合は、リストからそのファイルを除外して次へ
                images_list.remove(chosen_image)
                continue
        
        if not success:
            st.error("表示できる正常な画像が見つかりませんでした。")
    else:
        st.error("画像ファイルが見当たりません。")
