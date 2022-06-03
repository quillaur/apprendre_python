import streamlit as st
import numpy as np
import cv2

# Object lower and higher hue (for HSV mask purpose)
profils = {
    "Coke": {
        "lower": 0,
        "higher": 5
    } ,
    "Pepsi": {
        "lower": 100,
        "higher": 115
    }
}

# Load image.
uploaded_file = st.sidebar.file_uploader("Upload an image:")

if uploaded_file is not None:

    #convert string data to numpy array
    npimg = np.fromstring(uploaded_file.getvalue(), np.uint8)
    # convert numpy array to image
    frame = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    # Switch to HSV for simplier color handling.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # lower_h, upper_h = st.slider("Select a hue range:", 0, 360, (0,360))
    
    # Loop on all objects we want to detect.
    for object_name in profils.keys():
        # Set lower and high hue for mask filtering.
        lower_h = profils[object_name]["lower"]
        upper_h = profils[object_name]["higher"]
        
        # Create the mask.
        mask = cv2.inRange(hsv, (lower_h,100,100), (upper_h,255,255))

        # Find the object based on the mask.
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        # If we found something.
        if contours:
            # Get the biggest contour
            contour = sorted(contours, key = cv2.contourArea, reverse=True)[0]

            # To see all detected boxes.
            # for contour in contours:

            # Create rectangle from the biggest contour
            rect = cv2.boundingRect(contour)
            x,y,w,h = rect

            # Draw rectangle on original image
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,255), 2)

            # Add name of the object
            cv2.putText(frame, object_name, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    # Show the result.
    # Convert to RGB for matplotlib proper color rendering.
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    st.image(frame)