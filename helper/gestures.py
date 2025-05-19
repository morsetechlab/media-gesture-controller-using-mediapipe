def finger_states(landmarks):
    """
    รับ landmark 21 จุด
    คืนค่า list: [Thumb, Index, Middle, Ring, Pinky] (True = ยกนิ้ว)
    """
    thumb_tip = landmarks[4]
    thumb_ip = landmarks[3]
    index_tip = landmarks[8]
    index_pip = landmarks[6]
    middle_tip = landmarks[12]
    middle_pip = landmarks[10]
    ring_tip = landmarks[16]
    ring_pip = landmarks[14]
    pinky_tip = landmarks[20]
    pinky_pip = landmarks[18]

    fingers = [
        thumb_tip[0] > thumb_ip[0],             # นิ้วโป้ง (แนว x)
        index_tip[1] < index_pip[1],            # นิ้วชี้
        middle_tip[1] < middle_pip[1],          # นิ้วกลาง
        ring_tip[1] < ring_pip[1],              # นิ้วนาง
        pinky_tip[1] < pinky_pip[1],            # นิ้วก้อย
    ]
    return fingers


def is_fist(landmarks):
    return finger_states(landmarks) == [False, False, False, False, False]


def is_open_hand(landmarks):
    return finger_states(landmarks) == [True, True, True, True, True]


def is_ok_gesture(landmarks, max_distance=0.03):
    """
    ตรวจสอบท่า OK โดยการแตะปลายนิ้วชี้และนิ้วโป้งเข้าด้วยกัน
    """
    ix, iy = landmarks[8]
    tx, ty = landmarks[4]
    distance = ((ix - tx) ** 2 + (iy - ty) ** 2) ** 0.5
    return distance < max_distance


def is_two_fingers(landmarks):
    """
    นิ้วชี้ + กลาง ยก (Play)
    """
    fingers = finger_states(landmarks)
    return fingers[1] and fingers[2] and not fingers[3] and not fingers[4]
