import streamlit as st
from utils.image_utils import base64_to_image

def render_history():
    """Render the history component"""
    st.subheader("🔙 Retrieve Previous Query & Answer")
    
    if st.session_state.history:
        # Get all unique files that have history entries
        file_history_options = list(set(item["file"] for item in st.session_state.history if "file" in item))
        
        # Default to current file if it has history, otherwise use the first file
        default_file_idx = 0
        current_file = st.session_state.preview_file.name
        if current_file in file_history_options:
            default_file_idx = file_history_options.index(current_file)
        
        # File selection for history
        selected_file_history = st.selectbox(
            "Select file to see its prompts", 
            options=file_history_options,
            index=default_file_idx,
            key="file_history_select"
        )
        
        # Filter prompts by the selected file
        file_specific_prompts = [
            item["prompt"] for item in st.session_state.history 
            if "file" in item and item["file"] == selected_file_history
        ]
        
        if file_specific_prompts:
            # Prompt selection
            selected_prev = st.selectbox(
                f"Select a previous prompt for '{selected_file_history}'", 
                options=file_specific_prompts, 
                key="prev_prompt"
            )
            
            if st.button("Retrieve Answer", key="retrieve_prev"):
                # Reset feedback state when retrieving a previous answer
                st.session_state.feedback_submitted = False
                st.session_state.current_prompt = selected_prev
                
                # Find the matching history item
                for item in st.session_state.history:
                    if item["prompt"] == selected_prev and item.get("file") == selected_file_history:
                        st.session_state.current_response = item["answer"]
                        if "chart" in item:
                            st.session_state.current_chart = item["chart"]
                        else:
                            st.session_state.current_chart = None
                        break
                        
            # Display retrieved response and chart
            if st.session_state.current_response:
                st.write("### Previous Answer:")
                st.write(st.session_state.current_response)
                if st.session_state.current_chart:
                    try:
                        img = base64_to_image(st.session_state.current_chart)
                        st.image(img)
                    except Exception as e:
                        st.error(f"An error occurred while displaying the graph: {e}")
        else:
            st.info(f"No previous prompts available for '{selected_file_history}'.")
    else:
        st.info("No previous prompts available yet.")