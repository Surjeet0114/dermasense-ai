# AI Skin Specialist

A Gradio-based Python prototype for skin-condition consultation using:
- image upload support
- voice-to-text transcription
- AI report generation
- AI voice summary playback

## Project layout
- `app.py` – CLI-style terminal flow for image + voice input
- `frontend.py` – Gradio web UI entrypoint
- `brain_of_the_doctor.py` – LLM report generation and voice-summary orchestration
- `voice_of_the_patient.py` – audio transcription with Groq Whisper
- `voice_of_the_doctor.py` – text-to-speech output with Deepgram
- `prompts.py` – system prompt for the dermatologist-style report
- `test_*.py` – small smoke tests for internal modules

## Required environment
1. Create a Python virtual environment.
2. Install dependencies from `requirements.txt` or `pyproject.toml`.
3. Copy `.env.example` to `.env` and add your keys:
   - `GROQ_API_KEY`
   - `DEEPGRAM_API_KEY`

## How to run

### Option 1: Web UI
```bash
python -m pip install -r requirements.txt
python frontend.py
```
Then open the local URL printed in the terminal, usually:
`http://127.0.0.1:7860`

### Option 2: Terminal CLI
```bash
python app.py
```
You will be prompted to enter:
- an image path
- a voice file path

## Recommended cleanup before GitHub push
Remove or archive these if you do not need them in the public repo:
- `doctor_voice.mp3` and `patient_voice.mp3` – generated media; keep out of source control
- `sample-image.png` – demo asset; replace with a more neutral or remove it
- `list_models.py` – utility script, not part of the product flow
- `test_*.py` – keep only if you want QA coverage; otherwise they can stay for local validation
- `uv.lock` – useful only if you want reproducibility with `uv`; not required for general GitHub delivery

## GitHub push checklist
1. Commit the source code and docs.
2. Do not commit `.env` or API keys.
3. Add a repository description and a `.gitignore`-protected `.env` file locally.
4. Create a remote on GitHub and push:

```bash
git init
git add .
git commit -m "Initial AI Skin Specialist prototype"
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```

## Important note
This project is a prototype and should not be treated as a medical diagnosis system. It is best used as a demo or research assistant, not as a real clinical decision tool.
