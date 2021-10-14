import streamlit as st
from PIL import Image

def main():
    '''streamlit app that compress uploaded image.
    '''

    st.title('Compress JPG image')
    uploaded_file = st.file_uploader("Choose your .jpg file", type="jpg")

    if not uploaded_file:
        st.write("Upload a .jpg file to get started")
        return

    uploaded_image = Image.open(uploaded_file)
    st.image(uploaded_image)

if __name__ == '__main__':
    main()