import torch
from diffusers import StableDiffusionPipeline
from script_processing import processed_script
from config import MODEL_ID, DEVICE

def load_stable_diffusion_model():
    # Check if CUDA is available
    if torch.cuda.is_available():
        # Use float16 precision for GPU
        pipe = StableDiffusionPipeline.from_pretrained(MODEL_ID, torch_dtype=torch.float16)
    else:
        # Use float32 precision for CPU
        pipe = StableDiffusionPipeline.from_pretrained(MODEL_ID, torch_dtype=torch.float32)
    return pipe

def generate_image(prompt, output_path, width=512, height=512):
    pipe = load_stable_diffusion_model()
    pipe = pipe.to(DEVICE)
    image = pipe(prompt, width=width, height=height).images[0]
    image.save(output_path)
    print(f"Image saved to {output_path}")

for i, sentence in enumerate(processed_script):
    generate_image(sentence, f"image_scene_{i+1}.png")