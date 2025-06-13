import streamlit as st
import json
from generate_story import generate_storyboard
import time

st.set_page_config(
    page_title="Story Generation App",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Story Generator and Visualizer")

# Input area for the story
st.subheader("Enter Your Story")
story_input = st.text_area(
    "Write a short story (2-3 sentences)",
    """A young girl finds a mysterious map in her grandmother's attic 
    and sets out on an adventure to find a hidden treasure deep in 
    the forest.""",
    height=100
)

# Generate button
if st.button("Generate Storyboard"):
    with st.spinner('Generating storyboard and images...'):
        try:
            # Create progress bar
            progress_bar = st.progress(0)
            
            # Generate storyboard
            storyboard_data = generate_storyboard(story_input)
            
            # Display scenes in a grid
            st.subheader("Generated Storyboard")
            
            # Create columns for the grid layout
            cols = st.columns(2)
            
            for idx, scene in enumerate(storyboard_data):
                col_idx = idx % 2
                with cols[col_idx]:
                    st.markdown(f"### Scene {scene['scene_number']}")
                    st.image(
                        scene['image_url'],
                        caption=f"Scene {scene['scene_number']}",
                        use_column_width=True
                    )
                    st.markdown(f"**Storyline:** {scene['storyline']}")
                    st.markdown(f"*Image Prompt: {scene['image_prompt']}*")
                    st.markdown("---")
                
                # Update progress bar
                progress_bar.progress((idx + 1) * 10)
                
            st.success("Storyboard generated successfully!")
            
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")