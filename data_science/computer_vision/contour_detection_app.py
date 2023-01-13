import streamlit as st
import numpy as np
import cv2

# Object lower and higher hue (for HSV mask purpose)

# Load image.
uploaded_file = st.sidebar.file_uploader("Upload an image:")

if uploaded_file is not None:

    #convert string data to numpy array
    npimg = np.fromstring(uploaded_file.getvalue(), np.uint8)
    # convert numpy array to image
    frame = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    # Switch to HSV for simplier color handling.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_h, upper_h = st.slider("Select a hue range:", 0, 360, (0,360))
    
    # Create the mask.
    mask = cv2.inRange(hsv, (lower_h,100,100), (upper_h,255,255))

    c1, c2 = st.columns(2)
    with c1:
        st.image(frame)
    with c2:
        st.image(mask)

    # Find the object based on the mask.
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    contour_nb = st.number_input('Insert a number of contour to keep:', min_value=1)

    # If we found something.
    if contours:
        # Get the nb biggest contour
        contour = sorted(contours, key = cv2.contourArea, reverse=True)[:contour_nb]

        drawing = np.zeros(shape=(frame.shape[0], frame.shape[1]), dtype=np.int32)

        # To see all detected boxes.
        for contour in contours:
            cv2.fillPoly(drawing, contour, color=(255,255,255))

        st.image(drawing)
        st.write(len(contours))