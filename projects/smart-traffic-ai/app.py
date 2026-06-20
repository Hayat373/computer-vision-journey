import gradio as gr
from ultralytics import YOLO
import pandas as pd
from collections import defaultdict

model = YOLO("models/best.pt")

def analyze_traffic(video):
    results = model.track(
        source=video,
        conf=0.3,
        iou=0.5,
        tracker="bytetrack.yaml",
        save=True,
        name="traffic_analysis",
        verbose=False
    )
    
    counts = defaultdict(int)
    for r in results:
        for box in r.boxes:
            cls_name = r.names[int(box.cls)]
            counts[cls_name] += 1
    
    df = pd.DataFrame(list(counts.items()), columns=["Vehicle", "Count"])
    df = df.sort_values(by="Count", ascending=False)
    
    output_video = f"runs/detect/traffic_analysis/{video.name.split('/')[-1]}"
    
    return output_video, df

with gr.Blocks(title="Smart Traffic AI") as demo:
    gr.Markdown("# 🚦 Smart Traffic AI System")
    gr.Markdown("### Vehicle Detection • Tracking • Analytics")
    
    video_input = gr.Video(label="Upload Traffic Video")
    btn = gr.Button("Analyze", variant="primary")
    
    with gr.Row():
        output_video = gr.Video(label="Processed Video")
        output_table = gr.DataFrame(label="Vehicle Count")
    
    btn.click(analyze_traffic, inputs=video_input, outputs=[output_video, output_table])

demo.launch()