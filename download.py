import streamlit as st
from pytube import YouTube
from pytubefix import YouTube
import numpy as np
import matplotlib.pyplot as plt

# Title of the app
st.title('My Streamlit App with Pytube Integration')

# Description
st.write("This app allows you to download YouTube videos and displays a simple chart.")

# Section for YouTube video downloader
st.header('YouTube Video Downloader')

# YouTube video URL input
url = st.text_input("Enter YouTube Video URL", "")

if url:
    try:
        # Initialize YouTube object with the provided URL
        yt = YouTube(url)

        # Display video title and description
        st.write(f"Video Title: {yt.title}")
        st.write(f"Description: {yt.description}")

        # Display thumbnail
        

        # Select stream to download
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

        # Button to download video
        if st.button('Download Video'):
            # Download the video
            stream.download()
            st.success('Video downloaded successfully!')

    except Exception as e:
        st.error(f"Error: {e}")

# Add a slider to the app for plotting purposes
slider_value = st.slider('Select a value', 0, 100, 50)

# Display the selected value
st.write(f"You selected: {slider_value}")

# Generate data based on the slider value
x = np.linspace(0, 10, 100)
y = np.sin(x) * slider_value / 50

# Create a plot
fig, ax = plt.subplots()
ax.plot(x, y, label=f'Sine wave scaled by {slider_value}')
ax.legend()

# Display the plot in Streamlit
st.pyplot(fig)
