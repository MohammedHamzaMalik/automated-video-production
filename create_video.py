from moviepy.editor import *
from script_processing import processed_script

def create_video(script, image_files, audio_files, output_file, is_vertical=True):
    clips = []
    for text, image_file, audio_file in zip(script, image_files, audio_files):
        img_clip = ImageClip(image_file).set_duration(5)
        txt_clip = TextClip(text, fontsize=40, color='white', bg_color='black',
                            size=(1080, 1920) if is_vertical else (1920, 1080))
        txt_clip = txt_clip.set_pos('center').set_duration(5)
        audio_clip = AudioFileClip(audio_file)
        video = CompositeVideoClip([img_clip, txt_clip]).set_audio(audio_clip)
        clips.append(video)

    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile(output_file, fps=24)


image_files = [f"image_scene_{i + 1}.png" for i in range(len(processed_script))]
audio_files = [f"voiceover_scene_{i + 1}.mp3" for i in range(len(processed_script))]

create_video(processed_script, image_files, audio_files, "output_video.mp4", is_vertical=True)