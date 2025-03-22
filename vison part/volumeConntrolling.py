import cv2
import mediapipe as mp
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# Initialize Pycaw for volume control
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# Open the camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Start capturing and processing frames
cx8, cy8 = 0, 0
cx4, cy4 = 0, 0
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

    # Draw hand landmarks
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            lm8 = hand_landmarks.landmark[8]
            lm4 = hand_landmarks.landmark[4]
            cx8, cy8 = int(lm8.x * w), int(lm8.y * h)
            cx4, cy4 = int(lm4.x * w), int(lm4.y * h)
            cv2.line(frame, (cx8, cy8), (cx4, cy4), (255, 255, 255), 3)

            distance = math.sqrt((cx8 - cx4) ** 2 + (cy8 - cy4) ** 2)
            print(int(distance))

            # Map the distance to volume level
            min_distance = 50  # Minimum distance threshold
            max_distance = 200  # Maximum distance threshold
            min_volume = -65.25  # Minimum volume level in dB
            max_volume = 0.0  # Maximum volume level in dB

            if distance < min_distance:
                distance = min_distance
            elif distance > max_distance:
                distance = max_distance

            volume_level = min_volume + (max_volume - min_volume) * (distance - min_distance) / (max_distance - min_distance)
            volume.SetMasterVolumeLevel(volume_level, None)

    # Display the resulting frame
    cv2.imshow('Hand Detection', frame)

    # Press 'q' to exit the camera view
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()