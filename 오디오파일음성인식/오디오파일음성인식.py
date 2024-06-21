import speech_recognition as sr

r = sr.Recognizer()

harvard = sr.AudioFile('harvard.wav')
with harvard as source:
    audio = r.listen(source)

    text = r.recognize_google(audio)
    print('Converting audio transcripts into text...')
    print(text)
