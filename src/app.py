import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
import pandas as pd
from src.recommend import recommend_food, CATEGORIES

st.set_page_config(
    page_title="NutriMatch",
    page_icon="🥗",
    layout="centered",
)

st.title("NutriMatch")
st.write(
    "Temukan rekomendasi (makanan | minuman | bumbu | rempah) "
    "sesuai kebutuhan nutrisi kamu"
)

st.divider()

st.subheader("Masukkan Target Nutrisi")

col1, col2 = st.columns(2)

with col1:
    calories = st.number_input(
        "Kalori (kcal)",
        min_value=0.0,
        value=300.0,
    )
    proteins = st.number_input(
        "Protein (g)",
        min_value=0.0,
        value=15.0,
    )

with col2:
    fat = st.number_input(
        "Lemak (g)",
        min_value=0.0,
        value=10.0,
    )
    carbohydrate = st.number_input(
        "Karbo (g)",
        min_value=0.0,
        value=40.0,
    )

st.subheader("Pilih Kategori Makanan")

category = st.selectbox(
    "Jenis makanan",
    options=CATEGORIES,
    index=0,
    help="Filter rekomendasi berdasarkan kategori dari dataset",
)

n = st.slider(
    "Jumlah Rekomendasi",
    min_value=1,
    max_value=10,
    value=5,
)

if st.button("Cari rekomendasi makanan", use_container_width=True):
    result = recommend_food(
        calories,
        proteins,
        fat,
        carbohydrate,
        n,
        category,
    )

    st.subheader("Hasil Rekomendasi")

    if result.empty:
        st.warning("Tidak ada makanan ditemukan untuk kategori tersebut.")
    else:
        st.caption(f"Kategori: **{category}** · {len(result)} hasil")

        for _, food in result.iterrows():
            st.markdown(f"### {food['name']}")
            st.markdown(f"**Kategori:** {food['category_v2']}")

            if pd.notna(food["image"]) and food["image"]:
                try:
                    st.image(food["image"], width=250)
                except Exception:
                    st.caption("Gambar tidak tersedia")

            st.markdown(
                f"""
                <div class="nutrition">
                Kalori <b>{food["calories"]:.1f}</b> kcal<br>
                Protein <b>{food["proteins"]:.1f}</b> g<br>
                Lemak <b>{food["fat"]:.1f}</b> g<br>
                Karbo <b>{food["carbohydrate"]:.1f}</b> g
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.write(f"Jarak nutrisi: `{food['distance']:.3f}`")
            st.divider()
