# Day 24: Depth Estimation + Distance Calculation  
**Interview Questions & Answers**

**Date:** 23 June 2026  
**Model Used:** YOLO11s + Depth-Anything V2 (vitb)

---

## Conceptual Questions

### 1. What is Depth Estimation? Explain relative vs absolute depth.

**Answer:**  
Depth Estimation is the task of predicting the distance of each pixel from the camera.  
- **Relative Depth**: Tells which objects are closer or farther (no real units). What we used today.  
- **Absolute Depth**: Gives real-world distance in meters (requires calibration or stereo cameras).

### 2. How does Depth-Anything V2 work? What is its main advantage?

**Answer:**  
Depth-Anything V2 is a foundation model trained on massive amounts of data using self-supervised and synthetic data.  
**Main Advantage**: It generalizes very well to any scene (indoor, outdoor, day, night) without needing task-specific fine-tuning, unlike older models like MiDaS.

### 3. Why do we combine YOLO with Depth models?

**Answer:**  
YOLO gives us **semantic information** (what the object is + bounding box), while Depth gives **geometric information** (how far it is).  
Combining both allows us to answer:  
→ “There is a person **1.8 meters** away from the camera.”

### 4. What are the limitations of monocular depth estimation?

**Answer:**
- Scale ambiguity (cannot get true metric distance without reference)
- Struggles with reflective surfaces, transparent objects, and very dark areas
- Computationally heavy for real-time on low-end devices
- Sensitive to camera intrinsics

### 5. What is the difference between Depth Estimation and 3D Reconstruction?

**Answer:**  
Depth Estimation → Predicts depth map (2.5D).  
3D Reconstruction → Builds actual 3D mesh/point cloud using multiple views or depth + camera pose.

---

## Technical Questions

### 6. How do you estimate object distance using depth map?

**Answer:**  
I take the **center point** of the YOLO bounding box, read the depth value at that pixel from the depth map, then convert the relative depth to approximate distance using:  
`estimated_distance ≈ k / depth_value`  
(where `k` is a scaling factor).

### 7. What are the challenges when combining bounding boxes with depth?

**Answer:**
- Depth map can be noisy at object edges
- Center point may fall on background (especially for thin objects)
- Different parts of the same object can have very different depths
- Solution: Use median depth inside the bounding box instead of center only.

---

## Scenario Questions

### 11. A self-driving car needs to know how far a pedestrian is. How would you approach this?

**Answer:**  
I would combine:
- YOLO11 or YOLO-World for detection
- Depth-Anything V2 or a fine-tuned depth model
- Temporal smoothing (average over few frames)
- Camera calibration for better metric distance

### 13. How would you get real-world meters instead of relative values?

**Answer:**  
Methods:
1. Camera calibration + known object size
2. Fine-tune depth model with LiDAR ground truth data
3. Use stereo cameras or RGB-D cameras (Intel RealSense)

---

**Note for Myself:**
- I understand the high-level concept well.
- I can run the pipeline and combine models.
- I still need to practice explaining **limitations** and **improvements** clearly.

---
