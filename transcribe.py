import speech_recognition as sr

def transcribe_wav(filename):
    # Initialize the recognizer
    r = sr.Recognizer()
    
    # Read the .wav file
    with sr.AudioFile(filename) as source:
        # Load the audio to memory
        audio_data = r.record(source)
        
        # Perform speech recognition
        text = r.recognize_google(audio_data)
        
    return text

filename = "TestVoice/test1.wav"
transcription = transcribe_wav(filename)
print(transcription)
