import streamlit as st
import numpy as np

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

model = load_model("cat_dog_cnn_model.h5")

st.title("Cat vs Dog Image Classifier")

uploaded_file = st.file_uploader(
    "Upload an Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    img = image.load_img(
        uploaded_file,
        target_size=(128,128)
    )

    st.image(img, caption="Uploaded Image")

    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    prediction = model.predict(img_array)

    confidence = prediction[0][0]

    if confidence > 0.5:
        st.success(f"Dog 🐶 ({confidence*100:.2f}% confidence)")
    else:
        st.success(f"Cat 🐱 ({(1-confidence)*100:.2f}% confidence)")