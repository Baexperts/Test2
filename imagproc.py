import streamlit as st
import numpy as np
import cv2

# Title of the web app
st.title("Image Processing with Streamlit")

# Upload an image
uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    # Read the uploaded image
        image = cv2.imdecode(np.fromstring(uploaded_image.read(), np.uint8), 1)

            # Display the original image
                st.image(image, caption="Original Image", use_column_width=True)

                    # Image processing options
                        st.sidebar.header("Image Processing Options")
                            grayscale = st.sidebar.checkbox("Grayscale")
                                blur = st.sidebar.checkbox("Blur")

                                    # Apply selected image processing
                                        if grayscale:
                                                image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                                                    if blur:
                                                            image = cv2.GaussianBlur(image, (7, 7), 0)

                                                                # Display the processed image
                                                                    st.image(image, caption="Processed Image", use_column_width=True)