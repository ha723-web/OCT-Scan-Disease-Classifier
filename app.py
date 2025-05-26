# app.py

import streamlit as st
import os
from utils.predict import predict_oct_image
from PIL import Image

st.set_page_config(page_title="OCT Disease Classifier", layout="centered")
st.title("👁️ OCT Scan Disease Classifier")

uploaded = st.file_uploader("Upload an OCT scan image", type=["jpg", "png", "jpeg"])

if uploaded:
    os.makedirs("uploads", exist_ok=True)
    file_path = os.path.join("uploads", uploaded.name)
    with open(file_path, "wb") as f:
        f.write(uploaded.read())

    st.image(Image.open(file_path), caption="Uploaded OCT Image", use_container_width=True)

    prediction = predict_oct_image(file_path)
    st.subheader(f"🧠 Predicted Class: `{prediction}`")
