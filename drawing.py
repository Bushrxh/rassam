import cv2
import mediapipe as mp
import numpy as np

class HandDrawingProcessor:
    def __init__(self):
        # init MediaPipe hands module
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        
        # create a Hands object for detecting and tracking hands
        self.hands = self.mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)
        
        # init drawing-related variables
        self.canvas = None  # to store the drawing
        self.prev_point = None  # prev point for line drawing
        self.is_drawing = False  # flag to indicate if we're currently drawing

    def process_frame(self, frame, drawing_color, drawing_thickness, show_landmarks):
        # ff canvas doesn't exist, create it with the same dimensions as the frame
        if self.canvas is None:
            self.canvas = np.zeros(frame.shape, dtype=np.uint8)

        # convert the frame from BGR to RGB (as MediaPipe uses RGB)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # process the frame to detect hands
        results = self.hands.process(rgb_frame)

        # if hands are detected
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # if landmark display is ticked -> draw the landmarks on the frame
                if show_landmarks:
                    self.mp_drawing.draw_landmarks(
                        frame,
                        hand_landmarks,
                        self.mp_hands.HAND_CONNECTIONS,
                        self.mp_drawing_styles.get_default_hand_landmarks_style(),
                        self.mp_drawing_styles.get_default_hand_connections_style())

                # get the landmarks for index and middle fingertips
                index_finger_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP]
                middle_finger_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP]

                # convert the normalized landmark coordinates to pixel coordinates
                h, w, _ = frame.shape
                index_x, index_y = int(index_finger_tip.x * w), int(index_finger_tip.y * h)
                middle_x, middle_y = int(middle_finger_tip.x * w), int(middle_finger_tip.y * h)

                # (drawing mode): check if index finger is raised above middle finger 
                if index_y < middle_y:
                    if not self.is_drawing:
                        # start a new line
                        self.prev_point = (index_x, index_y)
                        self.is_drawing = True
                    else:
                        # continue the line
                        cv2.line(self.canvas, self.prev_point, (index_x, index_y), drawing_color, drawing_thickness)
                        self.prev_point = (index_x, index_y)
                else:
                    # end the line
                    self.is_drawing = False
                    self.prev_point = None

        # combine the original frame with the drawing canvas
        output = cv2.addWeighted(frame, 1, self.canvas, 0.5, 0)
        return output

    def clear_canvas(self):
        # clear the drawing canvas
        if self.canvas is not None:
            self.canvas.fill(0)

    def __del__(self):
        # close the MediaPipe Hands object when the process is deleted
        self.hands.close()