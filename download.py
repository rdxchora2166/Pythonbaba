import streamlit as st
import pytubefix as pytube

# Streamlit App Title
st.title("🎥 YouTube Video Downloader")

# Input for YouTube URL
video_url = st.text_input("Enter YouTube Video URL:", "")

if st.button("Download Video"):
    if video_url:
        try:
            # Get YouTube video
            yt = pytube.YouTube(video_url)
            stream = yt.streams.get_highest_resolution()
            
            # Download video
            stream.download()
            st.success(f"✅ Download Completed: {yt.title}")
        
        except Exception as e:
            st.error(f"❌ Error: {e}")
    else:
        st.warning("⚠️ Please enter a valid YouTube URL")
