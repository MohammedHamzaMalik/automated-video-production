from script_processing import processed_script
from gtts import gTTS

def generate_voiceover(text, language='en', output_file='voiceover.mp3'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(output_file)
    print(f"Voiceover saved as {output_file}")

# for i, sentence in enumerate(processed_script):
#     generate_voiceover(sentence, language='en', output_file=f'voiceover_scene_{i+1}.mp3')

print("Generating voiceover done")
__all__ = ['generate_voiceover']