import base64
import os
import re

from dotenv import load_dotenv
from groq import Groq

from .prompts import DOCTOR_PROMPT

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("Missing GROQ_API_KEY in .env file.")

client = Groq(api_key=api_key)


def encode_image(image_path):
    with open(image_path, "rb") as image:
        return base64.b64encode(image.read()).decode("utf-8")


def remove_think_tags(text: str):
    if not text:
        return ""

    text = re.sub(
        r"<think>.*?</think>",
        "",
        text,
        flags=re.DOTALL
    )

    return text.strip()


def generate_report(image_path=None, patient_question=""):

    if image_path:

        image = encode_image(image_path)

        completion = client.chat.completions.create(
            model="qwen/qwen3.6-27b",
            messages=[
                {
                    "role": "system",
                    "content": DOCTOR_PROMPT
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": patient_question
                            if patient_question
                            else "Please analyze this skin condition."
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{image}"
                            }
                        }
                    ]
                }
            ],
            temperature=0.2,
            max_completion_tokens=1200
        )

    else:

        completion = client.chat.completions.create(
            model="qwen/qwen3.6-27b",
            messages=[
                {
                    "role": "system",
                    "content": DOCTOR_PROMPT
                },
                {
                    "role": "user",
                    "content": f"""
The patient has not uploaded any image.

Please answer ONLY based on the symptoms below.

Make it clear that the diagnosis is NOT confirmed without examining the affected skin.

Symptoms:

{patient_question}
"""
                }
            ],
            temperature=0.2,
            max_completion_tokens=1200
        )

    report = completion.choices[0].message.content
    report = remove_think_tags(report)

    return report


def generate_voice_summary(report):

    summary_prompt = f"""
You are a dermatologist.

Convert the following medical report into a short spoken response.

Rules:

- Maximum 5 sentences.
- Maximum 600 characters.
- Friendly and reassuring.
- Mention the likely condition.
- Mention whether a dermatologist visit is recommended.
- Do NOT repeat the full report.
- Return ONLY the spoken response.

Medical Report:

{report}
"""

    completion = client.chat.completions.create(
        model="qwen/qwen3.6-27b",
        messages=[
            {
                "role": "user",
                "content": summary_prompt
            }
        ],
        temperature=0.2,
        max_completion_tokens=200
    )

    voice = completion.choices[0].message.content
    voice = remove_think_tags(voice)

    if not voice:
        voice = (
            "I've completed your skin analysis. "
            "Please review the report on the screen and consult a dermatologist if needed."
        )

    voice = voice.strip()

    # Deepgram safety
    if len(voice) > 1800:
        voice = voice[:1800]

    return voice


def analyze_skin(image_path=None, patient_question=""):
    """
    Returns:
        report -> Full medical report
        voice  -> Short summary for TTS
    """

    try:

        report = generate_report(
            image_path=image_path,
            patient_question=patient_question
        )

    except Exception as e:

        report = f"""
Unable to analyze the provided information.

Error:
{e}

Please try again.
"""

        voice = (
            "I'm sorry. I couldn't analyze the uploaded information because an internal error occurred. "
            "Please try again."
        )

        return report, voice

    try:

        voice = generate_voice_summary(report)

    except Exception:

        voice = (
            report
            .replace("\n", " ")
            .replace("  ", " ")
            .strip()
        )

        if len(voice) > 500:
            voice = voice[:500] + "..."

    report = report.strip()
    voice = voice.strip()

    if len(voice) > 1800:
        voice = voice[:1800]

    print("=" * 60)
    print("REPORT LENGTH :", len(report))
    print("VOICE LENGTH  :", len(voice))
    print("=" * 60)

    return report, voice


if __name__ == "__main__":

    report, voice = analyze_skin(
        image_path=None,
        patient_question="I have itchy red patches on my face for one week."
    )

    print("\nREPORT\n")
    print(report)

    print("\nVOICE\n")
    print(voice)