import streamlit as st
from pytubefix import YouTube
import numpy as np
import matplotlib.pyplot as plt

# YouTube video URL input
url = st.text_input("Enter YouTube Video URL", "")

if url:
    try:
        # Initialize YouTube object with the provided URL
        yt = YouTube(url)

        

        # Select stream to download
        stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()

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
