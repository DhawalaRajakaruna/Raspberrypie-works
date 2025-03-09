import cv2
import mediapipe as mp
import math

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# Open the camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()
# Start capturing and processing frames
cx8,cy8=0,0
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    # Flip the frame horizontally for a later selfie-view display
    frame = cv2.flip(frame, 1)

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame and detect hands
    results = hands.process(rgb_frame)
    h, w, c = frame.shape

    center_x = w // 2  # Middle of width
    center_y = h // 2  # Middle of height

    # Draw hand landmarks
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            #mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            lm8 = hand_landmarks.landmark[8]
            cx8, cy8 = int(lm8.x * w), int(lm8.y * h)
            cv2.line(frame, (cx8, cy8), (center_x, center_y), (255, 255, 255), 3)


    delt_x = cx8 - center_x
    delt_y = cy8 - center_y

    angle = math.atan2(delt_y, delt_x)
    angle = math.degrees(angle)

    angle=-angle
    if angle < 0:
        angle=(angle)+360
    print(int(angle))
    
    
    #map the angles witha stepper motor
    #angle=angle*1.8
    #angle=int(angle)

    # Draw the angle text on the frame
    cv2.putText(frame, f'Angle: {int(angle)}°', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

    # Display the resulting frame
    cv2.imshow('Hand Detection', frame)

    # Press 'q' to exit the camera view
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()