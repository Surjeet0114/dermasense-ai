import gradio as gr

from voice_of_the_patient import listen
from brain_of_the_doctor import analyze_skin
from voice_of_the_doctor import speak


def diagnose(image, audio, symptoms, history):

    if history is None:
        history = []

    # User must provide at least one input
    if image is None and audio is None and not symptoms.strip():

        history.append({
            "role": "assistant",
            "content": "❌ Please upload an image, record your voice, or type your symptoms."
        })

        return history, history

    patient_question = ""

    # -------------------------
    # Voice -> Text
    # -------------------------

    if audio is not None:

        try:

            voice_text = listen(audio)

            if voice_text:
                patient_question += voice_text

        except Exception as e:

            history.append({
                "role": "assistant",
                "content": f"❌ Voice processing failed.\n\n{e}"
            })

            return history, history

    # -------------------------
    # Typed symptoms
    # -------------------------

    if symptoms.strip():

        if patient_question:
            patient_question += "\n\nAdditional Symptoms:\n"

        patient_question += symptoms.strip()

    # -------------------------
    # Show patient message
    # -------------------------

    if patient_question:

        history.append({
            "role": "user",
            "content": patient_question
        })

    elif image is not None:

        history.append({
            "role": "user",
            "content": "📷 Uploaded a skin image for analysis."
        })

    # -------------------------
    # AI Diagnosis
    # -------------------------

    try:

        report, voice = analyze_skin(
            image_path=image,
            patient_question=patient_question
        )

    except Exception as e:

        report = f"❌ Error while analyzing:\n\n{e}"
        voice = "I'm sorry, I couldn't analyze the uploaded information due to an internal error."

    # -------------------------
    # Show detailed report
    # -------------------------

    history.append({

        "role": "assistant",
        "content": report

    })

    # -------------------------
    # Speak only voice summary
    # -------------------------

    try:

        speak(voice)

    except Exception as e:

        print("=" * 60)
        print("TTS ERROR")
        print(e)
        print("=" * 60)

    return history, history


with gr.Blocks(title="🩺 AI Skin Specialist") as demo:

    gr.Markdown(
        """
# 🩺 AI Skin Specialist

Upload any combination of:

- 📷 Skin Image
- 🎤 Voice
- ✍️ Symptoms

Then click **Analyze**.
"""
    )

    with gr.Row():

        image = gr.Image(
            type="filepath",
            label="📷 Upload Skin Image"
        )

        audio = gr.Audio(
            type="filepath",
            label="🎤 Upload Voice"
        )

    symptoms = gr.Textbox(
        label="✍️ Describe Symptoms",
        placeholder="Example: I have dark spots on my face for 2 months...",
        lines=4
    )

    chatbot = gr.Chatbot(
        label="🩺 Doctor Consultation",
        height=450,
        layout="bubble"
    )

    history = gr.State([])

    with gr.Row():

        analyze_btn = gr.Button(
            "🔍 Analyze",
            variant="primary"
        )

        clear_btn = gr.Button(
            "🗑️ Clear Chat"
        )

    analyze_btn.click(

        fn=diagnose,

        inputs=[
            image,
            audio,
            symptoms,
            history
        ],

        outputs=[
            chatbot,
            history
        ]

    )

    clear_btn.click(

        lambda: ([], []),

        outputs=[
            chatbot,
            history
        ]

    )

demo.launch()