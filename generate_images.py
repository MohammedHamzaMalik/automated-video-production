import torch
from diffusers import StableDiffusionPipeline
from script_processing import processed_script

def generate_image(prompt, output_path, width=512, height=512):
    model_id = "dreamlike-art/dreamlike-photoreal-2.0"
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")
    image = pipe(prompt, width=width, height=height).images[0]
    image.save(output_path)
    print(f"Image saved to {output_path}")

for i, sentence in enumerate(processed_script):
    generate_image(sentence, f"image_scene_{i+1}.png")