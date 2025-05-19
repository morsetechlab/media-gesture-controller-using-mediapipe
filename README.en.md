
# 📘 [เวอร์ชันภาษาไทย](README.md)

![Project](https://img.shields.io/badge/Project-Media%20Gesture%20Controller-blueviolet?style=for-the-badge)
![Framework](https://img.shields.io/badge/Framework-MediaPipe%20%2B%20OpenCV-orange?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-success?style=for-the-badge)
![Control](https://img.shields.io/badge/Control-Type:Gesture-informational?style=for-the-badge)

# 🎬 Media Gesture Controller using MediaPipe

> Control media playback with your hands 🤚  
> A touchless interface for video and audio applications.

This project uses ***MediaPipe + OpenCV + PyAutoGUI*** to detect hand gestures and control video or media playback in real-time — supporting platforms such as YouTube, Netflix, VLC, or smart media systems.

The system is designed for Human-Computer Interaction (HCI), real-time Computer Vision, and gesture-based control scenarios. It is ideal for use in Smart Homes, public kiosks, robotics, and other AI/IoT applications.

---

## Usage Example

<div align="center">
  <img src="images/output.gif" style="max-width: 100%; height: auto;" />
</div>

▶️ Watch Full Demo on [YouTube](https://youtu.be/qh72NVBzAxE)

---

## Key Features

| ✋ Gesture (L = Left, R = Right) | 🧠 Action                                    |
|----------------------------------|-----------------------------------------------|
| (L) ✋ Open left hand             | Activate Listening Mode                       |
| (L) ✊ Fist (left)                | Deactivate Listening Mode                     |
| (R) 👌 OK gesture                 | Switch to Volume Control Mode                 |
| (R) ✋ Open right hand            | Switch to Play/Pause Control Mode             |
| (R) ✊ Fist (right)               | Return to Idle Mode                           |
| (R) ✌️ Index + middle fingers     | Toggle Play/Pause (spacebar)                  |

---

## 🚀 Installation

### Clone Project

```bash
git clone git@github.com:morsetechlab/media-gesture-controller-using-mediapipe.git
cd media-gesture-controller-using-mediapipe
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Extra for Windows Users

If you're using **Windows**, install additional modules for volume control:

```bash
pip install pycaw comtypes
```

> `pycaw` and `comtypes` are used to manage system audio on Windows.

---

## How to Use

### 1. Open your preferred media (YouTube / Netflix / VLC) in a browser or supported player (Chrome, Safari)

### 2. Start the Gesture Controller

```bash
python gesture_controller.py
```

> ✨ Open your left hand to enable Listening Mode  
> ✌️ Raise two fingers on the right hand to Play/Pause  
> 👌 Make an OK gesture to adjust the volume  
> ✊ Close your left hand to exit Listening Mode

---

## Project Structure

```
media-gesture-controller-using-mediapipe/
├── gesture_controller.py          # Main controller script
├── helper/
│   ├── gestures.py                # Gesture recognition logic
│   └── volume_control.py          # Platform-specific volume control
├── requirements.txt               # Python dependencies
├── README.md
└── README.en.md
```

---

## Operating System Support

- Windows
- macOS (via AppleScript)
- Linux (via pactl)

---

## MediaPipe Hand Landmark Reference

[MediaPipe documentation](https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker/python)

<div align="center">
  <img src="images/hand-landmarks.png" style="max-width: 100%; height: auto;" />
</div>

---

## Extension Ideas

This gesture controller system can be extended in various directions:

- Control YouTube, Spotify, VLC, or any media player
- Integrate with smart home devices (e.g., lights, speakers)
- Connect to Smart TVs via HDMI-CEC or network API
- Build gesture-based game interfaces or AR/VR interactions
- Apply in public kiosks, robotics, or touchless access control

> You are free to modify, extend gestures, or integrate with AI/IoT pipelines.

---

## Attribution

- Gesture recognition powered by [MediaPipe](https://mediapipe.dev/)  
- Developed by [MorseTech Lab](https://www.morsetechlab.com/)

---

## 🛡️ License

This project is licensed under the terms of the [MIT License](LICENSE)

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
