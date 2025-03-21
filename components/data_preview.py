import streamlit as st
from utils.file_utils import read_excel_file

def render_data_preview():
    """Render the data preview component"""
    try:
        file = st.session_state.preview_file
        file.seek(0)
        df = read_excel_file(file)
        
        # Display preview
        st.markdown("## Preview of Data")
        selected_n_rows = st.session_state.get('selected_n_rows', 5)
        st.dataframe(df.head(selected_n_rows))
        
        return df
    except Exception as e:
        st.error(f"An error occurred while processing the file: {e}")
        return None