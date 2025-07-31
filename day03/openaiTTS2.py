from llm.MyApi import openAiModel
import warnings
warnings.filterwarnings(action='ignore')

audio_file = open("tts_audio.mp3", "rb")
client = openAiModel()
transcript = client.audio.transcriptions.create(
    file=audio_file,
    model="whisper-1",
    language="ko",
    response_format="text",
    temperature=0.0,
)

print(transcript)
