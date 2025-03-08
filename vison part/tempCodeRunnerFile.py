            lm8 = hand_landmarks.landmark[8]
            cx8, cy8 = int(lm8.x * w), int(lm8.y * h)

            # Get coordinates of landmark 4
            lm4 = hand_landmarks.landmark[4]
            cx4, cy4 = int(lm4.x * w), int(lm4.y * h)

            print(f'Landmark 8: ({cx8}, {cy8})')
            print(f'Landmark 4: ({cx4}, {cy4})')