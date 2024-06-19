import streamlit as st
import tensorflow
from tensorflow.keras.models import load_model

model = load_model('model.etlt')

page_bg_img ="""
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://cdn.pixabay.com/photo/2016/10/28/08/47/wallpaper-1777483_1280.jpg");
background-size: cover;
}
</style>
"""
st.markdown(page_bg_img,unsafe_allow_html=True)

st.title('Text translation')

choice = st.selectbox('select the source language',['hindi','marathi','other'])

if choice=='hindi':
    a = st.text_input('enter text')
    translate = model.translate(a)
    st.write(translate)
elif choice=='marathi':
    a = st.text_input('enter text')
    translate = model.translate(a)
    st.write(translate)
else:
    st.write('language translation under work')
