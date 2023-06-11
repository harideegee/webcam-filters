import streamlit as st
from PIL import Image, ImageFilter
from io import BytesIO

buf = BytesIO()

st.title("Webcam Filters App")
st.write("Explore new filters for your next amazing picture!")

with st.expander("Open Webcam"):

    capture = st.camera_input("Camera")

if capture is not None:
    filter = st.selectbox("Select filter.", ("Original", "Grayscale", "Blur", "Contour", "Detail", "Edge Enhance", "More Edge Enhance", "Emboss", "Outline", "Sharpen", "Smooth", "More Smooth"))
    img = Image.open(capture)

    if filter == "Original":
        image = img
    elif filter == "Grayscale":
        image = img.convert("L")
    elif filter == "Blur":
        image = img.filter(ImageFilter.BLUR)
    elif filter == "Contour":
        image = img.filter(ImageFilter.CONTOUR)
    elif filter == "Detail":
        image = img.filter(ImageFilter.DETAIL)
    elif filter == "Edge Enhance":
        image = img.filter(ImageFilter.EDGE_ENHANCE)
    elif filter == "More Edge Enhance":
        image = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    elif filter == "Emboss":
        image = img.filter(ImageFilter.EMBOSS)
    elif filter == "Outline":
        image = img.filter(ImageFilter.FIND_EDGES)
    elif filter == "Sharpen":
        image = img.filter(ImageFilter.SHARPEN)
    elif filter == "Smooth":
        image = img.filter(ImageFilter.SMOOTH)
    elif filter == "More Smooth":
        image = img.filter(ImageFilter.SMOOTH_MORE)
    else:
        pass


    st.image(image)
    
    image.save(buf, format="PNG")
    file = buf.getvalue()
    st.download_button("Download file", data=file, file_name="altered_image.png")