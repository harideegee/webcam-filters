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
    match filter:
        case "Original":
            image = img
        case "Grayscale":
            image = img.convert("L")
        case "Blur":
            image = img.filter(ImageFilter.BLUR)
        case "Contour":
            image = img.filter(ImageFilter.CONTOUR)
        case "Detail":
            image = img.filter(ImageFilter.DETAIL)
        case "Edge Enhance":
            image = img.filter(ImageFilter.EDGE_ENHANCE)
        case "More Edge Enhance":
            image = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
        case "Emboss":
            image = img.filter(ImageFilter.EMBOSS)
        case "Outline":
            image = img.filter(ImageFilter.FIND_EDGES)
        case "Sharpen":
            image = img.filter(ImageFilter.SHARPEN)
        case "Smooth":
            image = img.filter(ImageFilter.SMOOTH)
        case "More Smooth":
            image = img.filter(ImageFilter.SMOOTH_MORE)
    st.image(image)
    
    image.save(buf, format="PNG")
    file = buf.getvalue()
    st.download_button("Download file", data=file, file_name="altered_image.png")