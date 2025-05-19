# 📘 [English version available here](README.en.md)

![Project](https://img.shields.io/badge/Project-Media%20Gesture%20Controller-blueviolet?style=for-the-badge)
![Framework](https://img.shields.io/badge/Framework-MediaPipe%20%2B%20OpenCV-orange?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-success?style=for-the-badge)
![Control](https://img.shields.io/badge/Control-Type:Gesture-informational?style=for-the-badge)

# 🎬 Media Gesture Controller using MediaPipe

> ควบคุมการเล่นสื่อด้วยมือเปล่า 🤚  
> ระบบอินเทอร์เฟซไร้สัมผัส (Touchless Interface) สำหรับวิดีโอและเสียง

โปรเจกต์นี้ใช้ ***MediaPipe + OpenCV + PyAutoGUI*** ในการตรวจจับท่าทางมือ (Hand Gestures) เพื่อควบคุมการเล่นวิดีโอหรือสื่อประเภทต่าง ๆ เช่น YouTube, Netflix, VLC หรือระบบ Smart Media

ระบบนี้ออกแบบมาเพื่อรองรับการใช้งานจริงในด้าน Human-Computer Interaction (HCI), Real-time Computer Vision, และ Gesture-Based Media Control  
สามารถนำไปใช้งานใน Smart Home, Kiosk, หรือโปรเจกต์ด้าน AI/Robotics ได้อย่างยืดหยุ่น

---

## Usage Example

<div align="center">
  <img src="images/output.gif" style="max-width: 100%; height: auto;" />
</div>

---

## Key Feature

| ✋ Gesture (L = Left, R = Right) | 🧠 การทำงาน                                  |
|----------------------------------|-----------------------------------------------|
| (L) ✋ แบมือซ้าย                  | เปิด Listening Mode                           |
| (L) ✊ กำมือซ้าย                  | ปิด Listening Mode                            |
| (R) 👌 ท่า OK (นิ้วโป้งแตะนิ้วชี้) | เข้าสู่โหมดควบคุมเสียง (Volume Mode)        |
| (R) ✋ แบมือขวา                   | เข้าสู่โหมดควบคุมการเล่น (Play/Pause Mode)  |
| (R) ✊ กำมือขวา                   | กลับสู่โหมด Idle                             |
| (R) ✌️ ชูนิ้วชี้-กลาง             | สั่งเล่นหรือหยุดวิดีโอ (Play/Pause)         |

---

## 🚀 Installation

### Clone Project

```bash
git clone https://github.com/morsetechlab/media-gesture-controller-using-mediapipe.git
cd media-gesture-controller-using-mediapipe
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Extra for Windows Users

หากคุณใช้ **Windows** โปรดติดตั้งโมดูลเพิ่มเติมสำหรับการควบคุมระดับเสียง:

```bash
pip install pycaw comtypes
```

> `pycaw` และ `comtypes` ใช้สำหรับควบคุมระดับเสียงผ่าน Windows Audio API

---

## How to use

### เปิด Media (YouTube / Netflix / VLC) ในเบราว์เซอร์หรือแอปที่รองรับการกดแป้นพิมพ์ (เช่น Chrome, Safari)

### เรียกใช้ Gesture Controller

```bash
python gesture_controller.py
```

> ✨ ยกมือซ้ายแบออกเพื่อเริ่ม Listening Mode  
> ✌️ ยกสองนิ้วขวาเพื่อ Play/Pause  
> 👌 ทำท่า OK เพื่อปรับระดับเสียง  
> ✊ ปิดระบบด้วยกำปั้นซ้าย

---

## Project Structure

```
media-gesture-controller-using-mediapipe/
├── gesture_controller.py          # สคริปต์หลัก
├── helper/
│   ├── gestures.py                # ตรวจจับ gesture จาก landmark
│   └── volume_control.py          # ปรับเสียงตามระบบปฏิบัติการ
├── requirements.txt               # รายการ dependencies
├── README.md
└── README.en.md
```

---

## Operating System Support

- Windows
- macOS (AppleScript)
- Linux (pactl)

---

## MediaPipe Hand Landmark Reference

[MediaPipe documentation](https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker/python)

<div align="center">
  <img src="images/hand-landmarks.png" style="max-width: 100%; height: auto;" />
</div>

---

## Project Ideas

ระบบ Gesture Controller นี้สามารถนำไปพัฒนาเพิ่มเติมได้หลายรูปแบบ เช่น:

- ควบคุม YouTube, Spotify, VLC หรือ Media Player อื่น ๆ
- สั่งงานระบบสมาร์ทโฮม เช่น เปิด-ปิดไฟ หรือควบคุมเสียงจากลำโพง
- เชื่อมต่อกับ Smart TV ผ่าน API หรือ HDMI-CEC
- ใช้เป็น Gesture Interface สำหรับเกม หรือ AR/VR
- ใช้ในหุ่นยนต์, kiosk, หรือระบบ touchless interaction สำหรับพื้นที่สาธารณะ

> คุณสามารถนำโค้ดไปแก้ไข/เพิ่ม gesture ใหม่ หรือต่อยอดร่วมกับระบบ AI/IoT ได้อย่างยืดหยุ่น

---

## Attribution
Gesture Controller by [MediaPipe](https://mediapipe.dev/)
Developed by [MorseTech Lab](https://www.morsetechlab.com/)

---

## 🛡️ License

โปรเจกต์นี้เผยแพร่ภายใต้เงื่อนไขของ [MIT License](LICENSE)

<!--
tags: Hand Gesture Recognition, MediaPipe, OpenCV, PyAutoGUI, Touchless Control, Human-Computer Interaction, Gesture-based UI, Media Controller, Python Computer Vision, Smart Interface
-->

<!-- Open Graph / Twitter Meta -->
<!--
<meta property="og:title" content="Media Gesture Controller using MediaPipe" />
<meta property="og:description" content="Control media playback with hand gestures using MediaPipe and OpenCV. Ideal for touchless interfaces, HCI, and real-time media applications." />
<meta property="og:image" content="https://raw.githubusercontent.com/morsetechlab/media-gesture-controller/main/images/output.gif" />
<meta property="og:url" content="https://github.com/morsetechlab/media-gesture-controller" />
<meta property="og:type" content="website" />

<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="Media Gesture Controller using MediaPipe" />
<meta name="twitter:description" content="Gesture-based media controller built with MediaPipe and OpenCV. Ideal for smart interfaces and hands-free environments." />
<meta name="twitter:image" content="https://raw.githubusercontent.com/morsetechlab/media-gesture-controller/main/images/output.gif" />
-->
