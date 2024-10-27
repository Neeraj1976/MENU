from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
import google.generativeai as genai  # Replace with actual Gemini API
import pyttsx3
from googletrans import Translator

app = Flask(__name__)

# Configure the Gemini API key
genai.configure(api_key="Gemini API KEY")

# Initialize translator and TTS engine globally
translator = Translator()
tts_engine = pyttsx3.init()

@app.route('/')
def home():
    # This will render the HTML page
    return render_template('speech_to_speech.html')

@app.route('/start-voice', methods=['POST'])
def voice_to_gemini():
    target_language = request.json.get('target_language', 'en')  # Default language is English
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for voice input...")
        audio = recognizer.listen(source)

    try:
        # Convert voice to text using Google's speech recognition
        text = recognizer.recognize_google(audio)
        print("You said: " + text)

        # Generate a response from the hypothetical Gemini API
        gemini_response = genai.generate_text(prompt=f"{text}")
        response_text = gemini_response.result
        print("Gemini's response:", response_text)

        # Translate the Gemini response
        translated_response = translate_text(response_text, target_language)
        print(f"Translated response: {translated_response}")

        # Optionally speak the translated response
        speak(translated_response, target_language)

        # Return response as JSON
        return jsonify({
            "gemini_response": response_text,
            "translated_response": translated_response
        })

    except sr.UnknownValueError:
        return jsonify({"error": "Could not understand audio"}), 400
    except sr.RequestError as e:
        return jsonify({"error": f"Error with speech recognition: {e}"}), 500

def translate_text(text, target_language):
    """Translate text to the target language."""
    translation = translator.translate(text, dest=target_language)
    return translation.text

def speak(text, language):
    """Convert text to speech."""
    voices = tts_engine.getProperty('voices')
    for voice in voices:
        if language in voice.languages:
            tts_engine.setProperty('voice', voice.id)
            break
    tts_engine.say(text)
    tts_engine.runAndWait()

if __name__ == '__main__':
    app.run(debug=True)
