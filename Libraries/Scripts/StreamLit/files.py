import streamlit as st
import pandas as pd

# CSV Files
st.subheader("Loading CSV File")
file = st.file_uploader("Upload the csv file", type=['csv', 'xlsx'])

# if file:
#     st.table(file)

if file:
    st.write(pd.read_csv(file))
# st.dataframe(file)


# Images
st.subheader("Loading and Using the images")
st.image('R1.png')

img = st.file_uploader("Upload you're image : ", type=['jpeg', 'png', 'jpg'])

if img:
    st.image(img)


# Videos

st.subheader("Dealing with videos")

st.video(r"C:\Users\Asus\Videos\Captures\Student Guide - Brave 2023-09-29 09-46-10.mp4")

vid = st.file_uploader("Upload you're file : ", type=['mp4', 'mkv'])

if vid:
    st.video(vid)


# Audios
st.subheader("Working with Audio Files")

st.audio(r"C:\Users\Asus\Music\[iSongs.info] 08 - Yaalo Yaalaa.mp3")

aud = st.file_uploader("Upload the audio file : ", type=['mp3'])

if aud:
    st.audio(aud)