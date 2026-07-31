from groq import Groq
from dotenv import load_dotenv

import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def listen(audio_path):

    with open(audio_path, "rb") as audio:

        transcription = client.audio.transcriptions.create(

            file=audio,

            model="whisper-large-v3"

        )

    return transcription.text