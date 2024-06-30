import streamlit as st
import cv2
from drawing import HandDrawingProcessor

st.set_page_config(layout="wide")
st.title("Rassam - Live Drawing App")

# create 2 columns: drawing controls and the feed
col1, col2 = st.columns([3, 1])

with col1:
    stframe = st.empty()

with col2:
    st.sidebar.header("Drawing Controls")
    drawing_color = st.sidebar.color_picker("Choose drawing color", "#00FF00")
    drawing_thickness = st.sidebar.slider("Drawing thickness", 1, 20, 5)
    show_landmarks = st.sidebar.checkbox("Show hand landmarks", value=True)
    clear_button = st.sidebar.button('Clear Canvas', key='clear')
    stop_button = st.sidebar.button('Stop', key='stop')

# from Hex to BGR
drawing_color = tuple(int(drawing_color.lstrip('#')[i:i+2], 16) for i in (4, 2, 0))

processor = HandDrawingProcessor()
cap = cv2.VideoCapture(0)

# main loop flag
run = True

while run and cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    output = processor.process_frame(frame, drawing_color, drawing_thickness, show_landmarks)
    stframe.image(output, channels="BGR", use_column_width=True)

    if clear_button:
        processor.clear_canvas()
    if stop_button:
        run = False

cap.release()
st.sidebar.success("Drawing session ended. You can close this tab and get a life.")