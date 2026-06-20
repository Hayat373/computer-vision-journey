# 🚦 Smart Traffic AI System

**Vehicle Detection, Tracking & Analytics** using **YOLO11 + ByteTrack**

![Demo](https://img.shields.io/badge/Status-Ready-green)
![YOLO11](https://img.shields.io/badge/YOLO11-8.4.0-blue)
![Gradio](https://img.shields.io/badge/Gradio-5.0-orange)

## ✨ Features

- Real-time vehicle detection (car, truck, bus, motorcycle, etc.)
- Multi-object tracking with unique IDs
- Accurate vehicle counting (no double counting)
- Processed video output with bounding boxes + tracking lines
- Interactive analytics dashboard

## 🛠 Tech Stack

- **YOLO11s** (Ultralytics)
- **ByteTrack** (Multi-object tracking)
- **Gradio** (Web Interface)
- **Pandas** (Analytics)

## 📁 Project Structure
smart-traffic-ai/
├── app.py                 # Main Gradio application
├── requirements.txt       # Dependencies
├── models/                # (Optional) best.pt goes here
├── README.md
└── runs/                  # Generated during inference (ignored)

## 🚀 Quick Start

### Local Run
```bash
pip install -r requirements.txt
python app.py
```
### Hugging Face Space
This app is deployed and ready to use on Hugging Face Spaces.
📊 Example Output

- Detects and tracks multiple vehicles
- Shows accurate count per class
- Generates downloadable processed video

## 🎯 Future Improvements

- Custom trained model on traffic dataset
- Speed estimation
- Violation detection (red light, wrong lane)
- Multi-camera support


Part of Computer Vision Journey
Made with ❤️ in Ethiopia