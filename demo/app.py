import gradio as gr
import torch
import os
from glob import glob
from pathlib import Path
from typing import Optional


with gr.Blocks() as demo:
  gr.Markdown("Nerfstudio")
  with gr.Row():
    with gr.Column():
        image = gr.Image(label="Upload your image", type="pil")
        generate_btn = gr.Button("Generate")

if __name__ == "__main__":
    demo.queue(max_size=20)
    demo.launch(share=True)