import gradio as gr
from ultralytics import YOLO
import pandas as pd
from collections import defaultdict
import os

model = YOLO("yolo11s.pt")  


print("✅ Model loaded successfully!")

def analyze_traffic(video):
    if video is None:
        return None, pd.DataFrame({"Vehicle Type": ["Please upload a video"], "Count": [0]})
    
    print(f"🚦 Processing video: {video}")
    
    # Run tracking
    results = model.track(
        source=video,
        conf=0.25,
        iou=0.5,
        tracker="bytetrack.yaml",
        save=True,
        name="traffic_analysis",
        verbose=False,
        persist=True
    )
    
    # Count unique vehicles using tracking IDs
    unique_vehicles = defaultdict(set)
    for r in results:
        if r.boxes is not None and r.boxes.id is not None:
            for box, track_id in zip(r.boxes, r.boxes.id):
                cls_name = r.names[int(box.cls)]
                unique_vehicles[cls_name].add(int(track_id))
    
    counts = {cls: len(ids) for cls, ids in unique_vehicles.items()}
    
    df = pd.DataFrame(list(counts.items()), columns=["Vehicle Type", "Count"])
    df = df.sort_values(by="Count", ascending=False).reset_index(drop=True)
    
    # Get output video path
    output_dir = "runs/detect/traffic_analysis"
    output_video = None
    if os.path.exists(output_dir):
        video_files = [f for f in os.listdir(output_dir) if f.endswith(('.mp4', '.avi'))]
        if video_files:
            output_video = os.path.join(output_dir, video_files[-1])
    
    if output_video and os.path.exists(output_video):
        return output_video, df
    else:
        # Fallback: return original video
        return video, df


# ====================== GRADIO INTERFACE ======================
with gr.Blocks(title="🚦 Smart Traffic AI", theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🚦 Smart Traffic AI System")
    gr.Markdown("**YOLO11s + ByteTrack** • Vehicle Detection, Tracking & Analytics")
    gr.Markdown("**Note:** Currently using pre-trained YOLO11s. Custom model coming soon!")

    with gr.Row():
        with gr.Column(scale=1):
            video_input = gr.Video(
                label="📹 Upload Traffic Video",
                height=500,
                sources=["upload"]
            )
            analyze_btn = gr.Button("🚀 Analyze Video", variant="primary", size="large")
        
        with gr.Column(scale=1):
            output_video = gr.Video(
                label="🎥 Processed Video with Tracking",
                height=500
            )
    
    gr.Markdown("### 📊 Vehicle Count Report")
    output_table = gr.DataFrame(label="Detection Summary", headers=["Vehicle Type", "Count"])
    
    analyze_btn.click(
        fn=analyze_traffic,
        inputs=video_input,
        outputs=[output_video, output_table]
    )

    gr.Markdown("---\nMade as part of Computer Vision Journey")

demo.launch(share=True)