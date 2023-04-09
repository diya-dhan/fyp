import speech_recognition as sr



# Create a recognizer object

r = sr.Recognizer()



# The name of the audio file to transcribe

file_name = "bbaf1s.wav"



# Load the audio file into the recognizer

with sr.AudioFile(file_name) as source:

        audio = r.record(source)



        # Convert speech to text

        text = r.recognize_google(audio)



        # Print the transcribed text

        print(f"Transcription: {text}")
