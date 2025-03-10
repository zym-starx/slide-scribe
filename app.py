import streamlit as st

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

if __name__ == "__main__":
    main()
