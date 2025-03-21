import streamlit as st
from utils.file_utils import read_excel_file

def render_sidebar():
    """Render the sidebar UI"""
    st.sidebar.header("File Upload & Preview Settings")
    
    # File uploader
    file_uploader = st.sidebar.file_uploader(
        "Upload CSV or Excel files", 
        type=["csv", "xlsx", "xls"], 
        accept_multiple_files=True
    )
    
    # Number input for preview rows
    st.session_state.selected_n_rows = st.sidebar.number_input(
        "Select number of rows to preview", 
        min_value=1, 
        max_value=100, 
        value=st.session_state.get('selected_n_rows', 5), 
        step=1
    )
    
    # Process uploaded files
    if file_uploader:
        st.session_state.uploaded_files = file_uploader
        st.sidebar.write(f"📝 You have uploaded {len(file_uploader)} file(s).")
        
        # File selection dropdown
        file_options = [file.name for file in file_uploader]
        selected_file_name = st.sidebar.selectbox("Select file to preview", options=file_options)
        
        # Save the selected file in session state
        for file in file_uploader:
            if file.name == selected_file_name:
                st.session_state.preview_file = file
                break
    
    # Feedback statistics
    feedback_container = st.sidebar.container()
    with feedback_container:
        st.markdown("### Feedback Statistics")
        st.bar_chart(st.session_state.feedback_data)

def update_feedback(feedback_type):
    """Update feedback and rerun the app"""
    st.session_state.feedback_data[feedback_type] += 1
    st.session_state.feedback_submitted = True
    # Force rerun to update the UI immediately
    st.rerun()