import gradio as gr
from ultralytics import YOLO
import os

model = YOLO("yolo11s.pt")   

def detect_objects(image, confidence=0.25):
    results = model.predict(image, conf=confidence, verbose=False)
    annotated_image = results[0].plot()
    return annotated_image

# Beautiful Interface
with gr.Blocks(title="Waste & Vehicle Detector") as demo:
    gr.Markdown("# 🚀 Smart Object Detection System")
    gr.Markdown("### YOLO11 | Computer Vision Journey")
    
    with gr.Row():
        with gr.Column():
            input_image = gr.Image(type="pil", label="Upload an Image")
            conf_slider = gr.Slider(0.1, 0.95, value=0.25, label="Confidence Threshold", step=0.05)
            btn = gr.Button("🔍 Run Detection", variant="primary")
        
        with gr.Column():
            output_image = gr.Image(label="Detection Result")
    
    btn.click(
        fn=detect_objects,
        inputs=[input_image, conf_slider],
        outputs=output_image
    )

    gr.Markdown("### Made with ❤️ in Ethiopia | Day 11 Deployment")

demo.launch()