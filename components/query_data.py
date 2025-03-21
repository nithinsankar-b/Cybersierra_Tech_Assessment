import streamlit as st
from services.pandas_ai_service import PandasAiService
from utils.file_utils import read_excel_file
from components.sidebar import update_feedback

def render_query_data():
    """Render the query data component"""
    st.subheader("❓ Query Your Data")
    file = st.session_state.preview_file
    st.write(f"**Using file:** {file.name}")
    
    # Query input
    text_area = st.text_area("Enter your query about the data:", height=200)
    
    # Query button
    if st.button("Query Data", key="query_data"):
        if text_area.strip():
            # Reset feedback state for new query
            st.session_state.feedback_submitted = False
            st.session_state.current_prompt = text_area
            
            try:
                # Show loading message
                with st.spinner("Processing your query..."):
                    # Process the data
                    file.seek(0)
                    df = read_excel_file(file)
                    
                    # Create SmartDataframe and query
                    pandas_ai_service = PandasAiService()
                    
                    try:
                        smart_df = pandas_ai_service.create_smart_dataframe(df)
                        response = smart_df.chat(text_area)
                        
                        # Save response
                        st.session_state.current_response = response
                        
                        # Store in history
                        st.session_state.history.append({
                            "prompt": text_area, 
                            "answer": response, 
                            "file": file.name
                        })
                    except Exception as e:
                        st.error(f"Error processing query: {str(e)}")
                        st.info("Try clicking the query button again if the error persists.")
            except Exception as e:
                st.error(f"An error occurred: {e}")
                st.info("Try clicking the query button again if the error persists.")
    
    # Display current response
    if st.session_state.current_response:
        st.write("### 🧠 Answer:")
        st.write(st.session_state.current_response)
        
        # Show feedback options if not already submitted
        if not st.session_state.feedback_submitted:
            feedback = st.radio("Was this response useful?", ["Useful", "Not Useful"], key="feedback_query")
            if st.button("Submit Feedback", key="feedback_submit"):
                update_feedback(feedback)
        else:
            st.success("Thank you for your feedback!")