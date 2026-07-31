from voice_of_the_patient import listen
from brain_of_the_doctor import analyze_skin
from voice_of_the_doctor import speak


def main():

    print("=" * 60)
    print("        AI SKIN SPECIALIST")
    print("=" * 60)

    image_path = input("Enter image path : ").strip()
    audio_path = input("Enter voice file path : ").strip()

    print("\nConverting speech to text...\n")
    patient_question = listen(audio_path)

    print("Patient Said:")
    print(patient_question)

    print("\nAnalyzing skin...\n")

    doctor_response = analyze_skin(
        image_path=image_path,
        patient_question=patient_question
    )

    print("=" * 60)
    print("Doctor Response\n")
    print(doctor_response)
    print("=" * 60)

    print("\nGenerating doctor's voice...\n")
    speak(doctor_response)

    print("\nDone!")


if __name__ == "__main__":
    main()