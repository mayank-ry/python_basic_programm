import speech_recognition as sr
AUDIO_FILE = ("../assets/recog.wav")
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)

try:
    print("audio file contents : " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Not Working")
except sr.RequestError:
    print("Request Not Get From Google")

