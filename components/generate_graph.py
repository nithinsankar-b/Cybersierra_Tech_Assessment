import streamlit as st
from services.lida_service import LidaService
from utils.file_utils import read_excel_file
from utils.image_utils import base64_to_image
from components.sidebar import update_feedback

def render_generate_graph():
    """Render the graph generation component"""
    st.subheader("📊 Generate Graph from Your Data")
    file = st.session_state.preview_file
    st.write(f"**Using file:** {file.name}")
    
    # Graph description input
    text_area = st.text_area("Describe the graph you want to generate:", height=200)
    
    # Generate button
    if st.button("Generate Graph", key="generate_graph"):
        if text_area.strip():
            # Reset feedback state for new query
            st.session_state.feedback_submitted = False
            st.session_state.current_prompt = text_area
            
            try:
                # Process the data
                file.seek(0)
                df = read_excel_file(file)
                
                # Generate graph
                lida_service = LidaService()
                charts = lida_service.generate_chart(df, text_area)
                
                if charts and len(charts) > 0:
                    st.session_state.current_chart = charts[0].raster
                    st.session_state.current_response = "Graph generated."
                    
                    # Store in history
                    st.session_state.history.append({
                        "prompt": text_area, 
                        "answer": "Graph generated.", 
                        "chart": charts[0].raster,
                        "file": file.name
                    })
                else:
                    st.session_state.current_chart = None
                    st.session_state.current_response = "No graph was generated. Please try modifying your query."
                    st.error(st.session_state.current_response)
            except Exception as e:
                st.session_state.current_chart = None
                st.session_state.current_response = f"An error occurred while generating the graph: {e}"
                st.error(st.session_state.current_response)
    
    # Display current chart
    if st.session_state.current_chart:
        try:
            img = base64_to_image(st.session_state.current_chart)
            st.image(img)
            
            # Show feedback options if not already submitted
            if not st.session_state.feedback_submitted:
                feedback = st.radio("Was this response useful?", ["Useful", "Not Useful"], key="feedback_graph")
                if st.button("Submit Feedback", key="feedback_graph_submit"):
                    update_feedback(feedback)
            else:
                st.success("Thank you for your feedback!")
        except Exception as e:
            st.error(f"An error occurred while displaying the graph: {e}")