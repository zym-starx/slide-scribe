import streamlit as st
from pdf_utils import create_notes_pdf

def main():
    st.title("Slide Scribe")
    st.write("Welcome to Slide Scribe!")
    
    # PDF Uploader
    uploaded_pdf = st.file_uploader("Upload a PDF of your slides", type=["pdf"])
    
    # Layout options
    layout_option = st.selectbox("Choose a layout", ["1-slide-per-page", "2-slides-per-page"])
    orientation_option = st.radio("Orientation", ["Portrait", "Landscape"])
    
    
    if uploaded_pdf is not None:
        st.write("Uploaded file name:", uploaded_pdf.name)
        st.write(f"Layout: {layout_option}")
        st.write(f"Orientation: {orientation_option}")

        # Generate new structured PDF
        output_pdf = create_notes_pdf(uploaded_pdf, layout_option, orientation_option)

        # Allow downloading
        st.download_button(
            label="Download Notes PDF",
            data=output_pdf,
            file_name="structured_notes.pdf",
            mime="application/pdf"
        )

if __name__ == "__main__":
    main()
