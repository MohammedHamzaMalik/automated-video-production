from script_processing import process_script
from generate_voiceovers import generate_voiceover
from generate_images import generate_image
from create_video import create_video

def generate_ai_video(script, output_file, is_vertical=True):
    processed_script = process_script(script)

    image_files = []
    audio_files = []

    for i, sentence in enumerate(processed_script):
        generate_voiceover(sentence, output_file=f'voiceover_scene_{i + 1}.mp3')
        generate_image(sentence, f"image_scene_{i + 1}.png")
        image_files.append(f"image_scene_{i + 1}.png")
        audio_files.append(f'voiceover_scene_{i + 1}.mp3')

    create_video(processed_script, image_files, audio_files, output_file, is_vertical)


# Example usage
script = "Artificial intelligence is revolutionizing industries. It has applications in healthcare, finance, and education."
generate_ai_video(script, "ai_video.mp4", is_vertical=True)