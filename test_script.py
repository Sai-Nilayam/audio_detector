import pydub

audio_info = pydub.utils.mediainfo('data/train/all_voice_mp3/sai.mp3')
print(audio_info)
