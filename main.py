import streamlit as st
from dotenv import load_dotenv
import os
import importlib
import time

# Preload problematic modules
def preload_modules():
    """Preload potentially problematic modules"""
    try:
        import pandas
        import pandasai
        # Force import of specific modules that might cause issues
        importlib.import_module('pandas.core.arrays')
    except Exception as e:
        st.warning(f"Module preloading warning (app will still work): {e}")
        time.sleep(1)  # Give a moment for imports to stabilize

# Call preload at the very beginning
preload_modules()

# Import components
from components.sidebar import render_sidebar
from components.data_preview import render_data_preview
from components.query_data import render_query_data
from components.generate_graph import render_generate_graph
from components.history import render_history

# Load environment variables
load_dotenv()

# Initialize session state
def init_session_state():
    if 'history' not in st.session_state:
        st.session_state.history = []
    if 'feedback_data' not in st.session_state:
        st.session_state.feedback_data = {"Useful": 0, "Not Useful": 0}
    if 'uploaded_files' not in st.session_state:
        st.session_state.uploaded_files = []
    if 'preview_file' not in st.session_state:
        st.session_state.preview_file = None
    if 'current_response' not in st.session_state:
        st.session_state.current_response = None
    if 'current_chart' not in st.session_state:
        st.session_state.current_chart = None
    if 'feedback_submitted' not in st.session_state:
        st.session_state.feedback_submitted = False
    if 'current_prompt' not in st.session_state:
        st.session_state.current_prompt = None
    if 'previous_menu' not in st.session_state:
        st.session_state.previous_menu = None

def main():
    # UI Configuration
    st.set_page_config(page_title="AI Powered Data Explorer 🚀", layout="wide")
    st.title("AI Powered Data Explorer 🚀")
    st.markdown("### Explore your data with AI-powered queries and graphs 💡")
    
    # Initialize session state
    init_session_state()
    
    # Render sidebar
    render_sidebar()
    
    # Main area content
    if st.session_state.preview_file is not None:
        render_data_preview()
        
        # Top-level menu for query options
        current_menu = st.selectbox(
            "Choose an Option", 
            ["Query your Data", "Generate Graph from your Data", "Use Previous Prompt"], 
            key="menu", 
            index=0
        )
        
        # Check if menu changed and reset output if it did
        if 'previous_menu' in st.session_state and st.session_state.previous_menu != current_menu:
            reset_current_output()
        
        # Store current menu selection for next comparison
        st.session_state.previous_menu = current_menu
        
        # Render appropriate component based on selected menu
        if current_menu == "Query your Data":
            render_query_data()
        elif current_menu == "Generate Graph from your Data":
            render_generate_graph()
        elif current_menu == "Use Previous Prompt":
            render_history()
    else:
        st.info("📂 Upload files to start exploring your data!")

def reset_current_output():
    st.session_state.current_response = None
    st.session_state.current_chart = None
    st.session_state.feedback_submitted = False

if __name__ == "__main__":
    main()