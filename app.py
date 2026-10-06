from faster_whisper import WhisperModel

# Load Whisper model
model = WhisperModel("base", device="cpu", compute_type="int8")

# Transcribe audio
segments, info = model.transcribe("audio.wav")

# Combine all segments
text = ""

for segment in segments:
    text += segment.text

# Display result
print("Transcription:")
print(text)