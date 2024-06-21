import speech_recognition as sr #음성인식
import pyttsx3 #TTS 엔진
import pywhatkit #유튜브 등 검색 flask도 설치해야함
import datetime #시간
import wikipedia

#음성인식 초기화
listener = sr.Recognizer()

#TTS엔진 초기화
engine = pyttsx3.init()

#TTS 목소리
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id) # 0=man, 1=woman ?? 둘다 여자목소리

#engine.say('I am NishiKata') << 이런식으로 말하게 할 수 있다.

#말하기 
def talk(text):    
    engine.say(text)
    engine.runAndWait() #말 다 할때까지 대기


def take_command():
    try:        
        with sr.Microphone() as source: #오타 MicroPhone->Microphone
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice) #영어만 인식함
            command = command.lower() # <<소문자 변환

            if 'nishikata' in command: #naming
                command = command.replace('nishkata','') #명령에서 NishiKata를 제외
                #print(command) #talk(command) 함수를 통해 내가 한 말을 따라하게 함
                
    except:
        pass
    return command

def run_NishKata():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','') #명령에서 play를 제외
        talk('playing'+song)
        pywhatkit.playonyt(song) # 유튜브 실행

    #이런 식으로 명령 키워드를 추가함
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M') #strftime?
        print(time)
        talk('Current time is' + time) #단 영어로 알려줌

    elif 'search' in command:
        search = command.replace('search' ,'')
        info = wikipedia.summary(search, 1) #위키피디아 정보를 가져옴 summary? 왜 1이 있지?
        print(info)
        talk(info)

    elif 'date' in command:
        talk('sorry, i have a headache')
        
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
        
    elif 'are you there' in command:
        talk('i am here, always with you')

    elif 'i love you' in command:
        talk('i love you, too!')

    # 명령을 이해하지 못했을때/ 명령 키워드가 없을때
    else:
        talk('Please say the command again.')
        print('Please say the command again.')
        
while True:
    run_NishKata()
