import os
from faster_whisper import WhisperModel

# Check whether the audio file exists
audio_file = "audio.wav"

if not os.path.exists(audio_file):
    print(f"Error: {audio_file} not found.")
    print("Make sure audio.wav is in the same folder as this Python file.")
    exit()

# Load Whisper model
print("Loading Whisper model...")
model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

# Transcribe audio
print("Transcribing audio...")
segments, info = model.transcribe(audio_file)

# Collect recognized text
text = ""

for segment in segments:
    text += segment.text

# Display result
print("\nRecognized Text:")
print(text.strip())