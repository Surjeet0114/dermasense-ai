# AI Skin Specialist

AI Skin Specialist is a Python-based AI prototype for skin image analysis and voice interaction.

The project combines vision-based AI analysis with speech-to-text and text-to-speech capabilities, providing a simple Gradio interface for experimentation and demonstration.

## Features

- Skin image upload and analysis
- AI-generated skin analysis report
- Voice input from the user
- Voice-to-text transcription using Groq Whisper
- AI-generated voice summary
- Text-to-speech using Deepgram
- Gradio-based web interface
- Environment-based API key configuration

## Architecture

```text
                    AI Skin Specialist
                           │
                           ▼
                    Gradio Web UI
                     frontend.py
                           │
              ┌────────────┴────────────┐
              │                         │
         Image Input               Voice Input
              │                         │
              ▼                         ▼
     Skin Analysis Logic          Groq Whisper
              │                         │
              │                    Transcribed Text
              │                         │
              └────────────┬────────────┘
                           ▼
                  AI Analysis Pipeline
                           │
                           ▼
                    Groq Vision Model
                           │
                           ▼
                  Generated AI Report
                           │
                           ▼
                  Voice Summary Generation
                           │
                           ▼
                       Deepgram
                           │
                           ▼
                    Audio Response
```

## Project Structure

```text
ai-skin-specialist/
│
├── app.py
├── frontend.py
├── README.md
├── requirements.txt
├── pyproject.toml
├── .env.example
├── .gitignore
│
└── src/
    ├── __init__.py
    ├── brain_of_the_doctor.py
    ├── prompts.py
    ├── voice_of_the_patient.py
    └── voice_of_the_doctor.py
```

## Main Components

### `app.py`

Provides the terminal-based application flow for testing the AI pipeline without the Gradio interface.

### `frontend.py`

The main Gradio web interface.

It provides the user-facing interface for:

- Image input
- Voice input
- AI analysis
- Generated report
- Audio response

### `src/brain_of_the_doctor.py`

Contains the main AI analysis orchestration.

It handles:

- Image processing
- AI model interaction
- Skin analysis
- Report generation
- Voice-summary generation

### `src/voice_of_the_patient.py`

Handles patient voice input and converts speech into text using Groq Whisper.

### `src/voice_of_the_doctor.py`

Handles text-to-speech generation using Deepgram.

### `src/prompts.py`

Contains the prompts used to guide the AI during skin analysis and response generation.

## Technology Stack

- Python
- Gradio
- Groq
- Groq Vision Models
- Groq Whisper
- Deepgram
- Python Dotenv
- OpenCV
- Pillow

## Requirements

- Python 3.13+
- Groq API key
- Deepgram API key

## Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
DEEPGRAM_API_KEY=your_deepgram_api_key
```

Never commit the `.env` file or expose API keys in source control.

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd ai-skin-specialist
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

Using `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

Or using the project configuration:

```bash
pip install .
```

### 4. Configure environment variables

Copy `.env.example` to `.env` and add your API keys:

```env
GROQ_API_KEY=your_groq_api_key
DEEPGRAM_API_KEY=your_deepgram_api_key
```

## Running the Application

### Gradio Web Interface

Start the Gradio application:

```bash
python frontend.py
```

Gradio will provide a local URL in the terminal, usually:

```text
http://127.0.0.1:7860
```

Open the URL in your browser.

### Terminal Application

The AI pipeline can also be executed through:

```bash
python app.py
```

The terminal application will request the required image and voice input.

## AI Processing Flow

The application follows this general workflow:

```text
User
 │
 ├── Skin Image
 │
 └── Voice Input
        │
        ▼
   Speech-to-Text
        │
        ▼
   AI Analysis
        │
        ├── Image Understanding
        ├── User Symptoms
        └── Prompt Instructions
        │
        ▼
   Generated Report
        │
        ▼
   Voice Summary
        │
        ▼
   Text-to-Speech
        │
        ▼
   Audio Response
```

## Disclaimer

This project is an AI prototype for experimentation, demonstration, and research purposes.

It is **not a medical diagnosis system** and should not be used as a substitute for professional medical advice, diagnosis, or treatment.

AI-generated results may be inaccurate or incomplete. Always consult a qualified healthcare professional for actual medical concerns.

## Project Status

The project is maintained as a standalone AI prototype demonstrating:

- Computer vision
- Large language models
- Speech-to-text
- Text-to-speech
- Multimodal AI
- AI-assisted skin analysis
- Gradio-based AI applications

The AI functionality from this project can also serve as a foundation for integration into a larger application platform.