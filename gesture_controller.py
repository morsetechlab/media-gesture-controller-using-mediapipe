import cv2
import mediapipe as mp
import time
import numpy as np
from helper.gestures import *
from helper.volume_control import set_volume
import pyautogui

# MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Set Color
GREEN = (0, 255, 0)
VIOLET = (244, 41, 117)
WHITE = (255, 255, 255)
SKY_BLUE = (255, 204, 0)

# State
listening = False
volume_mode = False
play_pause_mode = False
last_gesture = "Waiting..."
gesture_state = None
gesture_last_time = 0
mode_switch_time = 0  # สำหรับ debounce การเปลี่ยนโหมด
mode_cooldown = 1.0  # วินาที
prev_time = 0

cap = cv2.VideoCapture(0)
print("Starting Netflix Gesture Controller...")

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    h, w, _ = frame.shape
    left_hand, right_hand = None, None

    # Detect Hand
    if results.multi_hand_landmarks and results.multi_handedness:
        for i, hand_landmarks in enumerate(results.multi_hand_landmarks):
            hand_label = results.multi_handedness[i].classification[0].label
            landmarks = [(lm.x, lm.y) for lm in hand_landmarks.landmark]

            if hand_label == "Left":
                left_hand = landmarks
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                    mp_draw.DrawingSpec(color=GREEN, thickness=3, circle_radius=4),
                    mp_draw.DrawingSpec(color=VIOLET, thickness=4))

            elif hand_label == "Right":
                right_hand = landmarks
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                    mp_draw.DrawingSpec(color=GREEN, thickness=3, circle_radius=4),
                    mp_draw.DrawingSpec(color=VIOLET, thickness=4))

    # Left Hand: Listening Mode
    if left_hand:
        if is_open_hand(left_hand) and not listening:
            listening = True
            last_gesture = "Listening ON"
            print(last_gesture)
        elif is_fist(left_hand) and listening:
            listening = False
            volume_mode = False
            play_pause_mode = False
            gesture_state = None
            last_gesture = "Listening OFF"
            print(last_gesture)

    now = time.time()

    if right_hand and listening:
        # Gesture Controller with debounce
        if now - mode_switch_time > mode_cooldown:
            if is_ok_gesture(right_hand):
                volume_mode = True
                play_pause_mode = False
                last_gesture = "Volume Mode"
                mode_switch_time = now

            elif is_open_hand(right_hand):
                play_pause_mode = True
                volume_mode = False
                last_gesture = "Play/Pause Mode"
                mode_switch_time = now

            elif is_fist(right_hand):
                volume_mode = False
                play_pause_mode = False
                gesture_state = None
                last_gesture = "Idle"
                mode_switch_time = now

        # Volume Mode
        if volume_mode:
            tx, ty = right_hand[4]
            ix, iy = right_hand[8]
            cx1, cy1 = int(tx * w), int(ty * h)
            cx2, cy2 = int(ix * w), int(iy * h)
            dist = ((tx - ix) ** 2 + (ty - iy) ** 2) ** 0.5
            vol_percent = min(100, max(0, int((dist - 0.01) * 1000)))

            # Display Volume
            cv2.line(frame, (cx1, cy1), (cx2, cy2), SKY_BLUE, 10)
            mid_x, mid_y = int((cx1 + cx2) / 2), int((cy1 + cy2) / 2)
            cv2.putText(frame, f"{vol_percent}%", (mid_x - 40, mid_y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.2, WHITE, 3)

            if now - gesture_last_time > 0.2:
                set_volume(vol_percent)
                gesture_last_time = now
                print(f"Volume: {vol_percent}%")

        # Play/Pause Mode
        elif play_pause_mode:
            if is_two_fingers(right_hand):
                if gesture_state != "Toggled Playback" and (now - gesture_last_time > 1.0):
                    pyautogui.press("space")
                    last_gesture = "Toggled Playback"
                    gesture_state = "Toggled Playback"
                    gesture_last_time = now
                    print("Toggled Playback")

    # Display FPS
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time + 1e-6)
    prev_time = curr_time

    fps_text = f"FPS: {int(fps)}"
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1.4
    thickness = 3
    (text_w, text_h), _ = cv2.getTextSize(fps_text, font, font_scale, thickness)
    cv2.rectangle(frame, (10, 10), (10 + text_w + 20, 10 + text_h + 20), (0, 0, 0), -1)
    cv2.putText(frame, fps_text, (20, 10 + text_h + 10), font, font_scale, GREEN, thickness)

    # Gesture Feedback Overlay
    if listening:
        overlay = frame.copy()
        alpha = 0.6
        text = f"Gesture: {last_gesture}"
        (text_w, text_h), _ = cv2.getTextSize(text, font, 1.5, 3)
        box_x = int((w - text_w - 40) / 2)
        box_y = h - text_h - 80
        cv2.rectangle(overlay, (box_x, box_y), (box_x + text_w + 40, box_y + text_h + 30), (0, 0, 0), -1)
        cv2.putText(overlay, text, (box_x + 20, box_y + text_h + 10), font, 1.5, WHITE, 3)
        cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)

    cv2.imshow("Netflix Gesture Control", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()