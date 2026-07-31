from deepgram import DeepgramClient
from dotenv import load_dotenv
from pathlib import Path

import os
import platform
import subprocess

load_dotenv()

deepgram = DeepgramClient(
    api_key=os.getenv("DEEPGRAM_API_KEY")
)


def speak(text: str):

    output = Path("doctor_voice.mp3")

    audio = deepgram.speak.v1.audio.generate(
        text=text,
        model="aura-2-thalia-en",
        encoding="mp3"
    )

    with output.open("wb") as f:
        total = 0

        for chunk in audio:
            f.write(chunk)
            total += len(chunk)

    print(f"Written {total} bytes")
    print(f"File size : {output.stat().st_size}")

    if platform.system() == "Windows":
        os.startfile(str(output))
    elif platform.system() == "Darwin":
        subprocess.run(["afplay", str(output)])
    else:
        subprocess.run(["xdg-open", str(output)])