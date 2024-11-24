import whisper
from pydub import AudioSegment

# Convert MP3 to WAV
def convert_mp3_to_wav(mp3_path, wav_path):
    audio = AudioSegment.from_mp3(mp3_path)
    audio.export(wav_path, format="wav")

# Transcribe the audio using Whisper
def transcribe_audio(wav_path):
    model = whisper.load_model("base")
    result = model.transcribe(wav_path)
    return result["text"]
