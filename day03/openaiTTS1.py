from llm.MyApi import openAiModel
import warnings
warnings.filterwarnings(action='ignore')

speech_file_path = "tts_audio.mp3"
client = openAiModel()
response = client.audio.speech.create(
    model="tts-1",
    input="아~ 오늘 파이썬 배우기 정말 좋은 날이네~",
    voice="alloy",
    response_format="mp3",
    speed=1.1,
)

response.stream_to_file(speech_file_path)
