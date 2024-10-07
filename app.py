import streamlit as st
from sympy.physics.units import time

from main import generate_ai_video


# Use caching for expensive computations
@st.cache(allow_output_mutation=True)
def cached_generate_ai_video(script, output_file, is_vertical):
    return generate_ai_video(script, output_file, is_vertical)


st.title("AI Video Generator")

script = st.text_area("Enter your script here:")
is_vertical = st.checkbox("Vertical video (for TikTok/Instagram)", value=True)

if st.button("Generate Video"):
    if script:
        st.write("Generating video... This may take a few minutes.")
        progress_bar = st.progress(0)

        # Use the cached function
        output_file = cached_generate_ai_video(script, "output_video.mp4", is_vertical)

        # Update progress bar (you'll need to modify your generate_ai_video function to return progress)
        for i in range(100):
            # Simulate progress (replace with actual progress updates)
            progress_bar.progress(i + 1)
            time.sleep(0.1)

        st.video(output_file)
    else:
        st.write("Please enter a script first.")