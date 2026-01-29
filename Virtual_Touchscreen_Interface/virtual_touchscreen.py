import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import math

# ---------------- SAFETY ----------------
pyautogui.FAILSAFE = True

# ---------------- SCREEN ----------------
screen_width, screen_height = pyautogui.size()

# ---------------- CAMERA ----------------
cap = cv2.VideoCapture(0)

# ---------------- MEDIAPIPE ----------------
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

# ---------------- CALIBRATION ----------------
FRAME_MARGIN = 120
alpha = 0.2
prev_x, prev_y = 0, 0

# ---------------- PINCH / DRAG ----------------
PINCH_THRESHOLD = 50
PINCH_FRAMES_CLICK = 6
PINCH_FRAMES_DRAG = 18

pinch_counter = 0
clicked = False
dragging = False

# ---------------- SCROLL ----------------
SCROLL_THRESHOLD = 40
prev_scroll_y = None

# ---------------- ZOOM ----------------
prev_zoom_dist = None
ZOOM_SENSITIVITY = 30

# ---------------- MAIN LOOP ----------------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    x_min, y_min = FRAME_MARGIN, FRAME_MARGIN
    x_max, y_max = w - FRAME_MARGIN, h - FRAME_MARGIN

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:

            # Landmarks
            index = hand_landmarks.landmark[8]
            middle = hand_landmarks.landmark[12]
            thumb = hand_landmarks.landmark[4]

            ix, iy = int(index.x * w), int(index.y * h)
            mx, my = int(middle.x * w), int(middle.y * h)
            tx, ty = int(thumb.x * w), int(thumb.y * h)

            # Clamp to active area
            ix = np.clip(ix, x_min, x_max)
            iy = np.clip(iy, y_min, y_max)

            # ---------------- CURSOR MOVE ----------------
            raw_x = np.interp(ix, (x_min, x_max), (0, screen_width))
            raw_y = np.interp(iy, (y_min, y_max), (0, screen_height))

            smooth_x = alpha * raw_x + (1 - alpha) * prev_x
            smooth_y = alpha * raw_y + (1 - alpha) * prev_y
            prev_x, prev_y = smooth_x, smooth_y

            pyautogui.moveTo(smooth_x, smooth_y)

            # ---------------- DISTANCES ----------------
            pinch_dist = math.hypot(tx - ix, ty - iy)
            scroll_dist = math.hypot(ix - mx, iy - my)

            # ---------------- SCROLL ----------------
            if scroll_dist < SCROLL_THRESHOLD:
                if prev_scroll_y is not None:
                    delta = iy - prev_scroll_y
                    scroll_amount = int(-delta / 3)
                    pyautogui.scroll(scroll_amount)
                prev_scroll_y = iy
                cv2.putText(frame, "SCROLL", (10, 40),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
            else:
                prev_scroll_y = None

            # ---------------- ZOOM ----------------
            if pinch_dist < PINCH_THRESHOLD * 1.5:
                if prev_zoom_dist is not None:
                    zoom_change = pinch_dist - prev_zoom_dist
                    if abs(zoom_change) > ZOOM_SENSITIVITY:
                        pyautogui.keyDown('ctrl')
                        pyautogui.scroll(int(-zoom_change))
                        pyautogui.keyUp('ctrl')
                prev_zoom_dist = pinch_dist
                cv2.putText(frame, "ZOOM", (10, 80),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
            else:
                prev_zoom_dist = None

            # ---------------- CLICK / DRAG ----------------
            if pinch_dist < PINCH_THRESHOLD:
                pinch_counter += 1
                if pinch_counter >= PINCH_FRAMES_DRAG and not dragging:
                    pyautogui.mouseDown()
                    dragging = True
                elif pinch_counter >= PINCH_FRAMES_CLICK and not clicked and not dragging:
                    pyautogui.click()
                    clicked = True
            else:
                if dragging:
                    pyautogui.mouseUp()
                    dragging = False
                pinch_counter = 0
                clicked = False

            # ---------------- VISUALS ----------------
            cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (255, 255, 0), 2)
            cv2.circle(frame, (ix, iy), 8, (0, 255, 0), -1)
            cv2.circle(frame, (mx, my), 8, (255, 0, 255), -1)
            cv2.circle(frame, (tx, ty), 8, (255, 0, 0), -1)

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Virtual Touchscreen – Final+", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
