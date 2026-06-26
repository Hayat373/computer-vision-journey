# Day 25: Action Recognition using Pose Keypoints

**Date:** June 26
**Main Tool:** YOLO11 Pose + Keypoint Sequence Analysis

---

## 🎯 Objective

Convert human **body movements** (sequence of keypoints) into **action prediction** (Standing, Walking, Running, etc.).

---

## 📌 Core Concept

- **Pose Estimation** gives us the position of 17 keypoints (nose, shoulders, elbows, knees, ankles, etc.) in every frame.
- **Action Recognition** looks at **how these keypoints change over time** (sequence of frames).
- We treat the movement as a **time series** of body positions.

---

## 🔑 Key Learnings

1. **Keypoints Format**
   - YOLO11 Pose returns **17 keypoints** per person.
   - Each keypoint has **(x, y, confidence)**.
   - Shape: `(number_of_frames, 17, 3)`

2. **Why Pose Keypoints are Powerful**
   - More efficient than analyzing raw video frames.
   - Works well even with low-resolution video.
   - Privacy-friendly (no full face/body image needed).

3. **Challenges**
   - Need multiple frames (temporal information).
   - Different people have different body sizes and speeds.
   - Occlusion (when body parts are hidden).
   - Need good pose detection first.

---

## 🛠 Methods I Used

- **Feature Extraction**: Flatten keypoints → 51 features per frame (17×3)
- **Simple Rule-based Classifier**: Based on ankle/knee movement variance
- **Future Improvement**: Use LSTM, GRU, or Transformer to learn complex actions

---

## 📊 Common Actions & How to Detect Them

| Action          | Detection Method                        | Difficulty |
|-----------------|-----------------------------------------|----------|
| Standing        | Very low ankle movement                 | Easy     |
| Walking         | Medium ankle vertical movement          | Medium   |
| Running         | High ankle/knee movement                | Medium   |
| Sitting         | Low hip height + low movement           | Hard     |
| Falling         | Sudden big change in head/hip position  | Hard     |
| Waving          | High wrist movement                     | Medium   |

---

## 🚀 Real-World Applications

- Fall detection for elderly care
- Sports form analysis
- Security (suspicious behavior detection)
- Human-robot interaction
- Exercise tracking apps


---

## 💡 Personal Observations

- YOLO11 Pose is reliable for keypoint extraction.
- Simple movement-based rules work surprisingly well for basic actions.
- Need temporal modeling (LSTM) for complex actions.
- Lighting and camera angle still affect accuracy.

---

**Status:** Completed Day 25  
**Next Goal:** Build a more accurate classifier + real-time demo