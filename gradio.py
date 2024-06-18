import gradio as gr
import speech_recognition as sr
import tensorflow
from tensorflow.keras.models import load_model

model = load_model('model.pb')

css_code = """
.gradio-container {background: url(https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMudvUx27TvoNNHRxaswur9Z33zRqzLrmIHA&usqp=CAU) no-repeat center center fixed; background-size: cover;}
"""
recognizer = sr.Recognizer()

def translate_audio_to_text(audio, language):
    # Map user-friendly language names to the codes used by the speech recognizer
    language_code = {
        "Hindi": "hi-IN",
        "Marathi": "mr-IN"
    }.get(language, "hi-IN")  # Default to Hindi if something goes wrong

    # Use SpeechRecognition to convert audio to text
    with sr.AudioFile(audio) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data, language=language_code)
            print(f"Recognized Text: {text}")
        except sr.UnknownValueError:
            return "Sorry, I could not understand the audio."
        except sr.RequestError:
            return "Could not request results; check your network connection."

    translated_text = model.translate(text)
    return translated_text


# Define the Gradio interface
iface = gr.Interface(
    fn=translate_audio_to_text,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath"),
        gr.Dropdown(choices=["Hindi", "Marathi"], label="Select Language")
    ],
    outputs="text",
    title="Voice Translation",
    description="Record your voice in Hindi or Marathi to get the English translation.",
    css=css_code
)

# Launch the Gradio app
iface.launch()
