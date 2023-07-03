import win32com.client as wincom
if __name__ == '__main__':
    print("hi mate welcome to robo speaker,please enter what u want to speak!! and please enter q to stop interacting with me")
    z= "hi mate welcome to Robospeaker,please enter what u want to speak!!and please enter q to stop interacting with me"
    speak = wincom.Dispatch("SAPI.SpVoice")
    speak.Speak(z)
    while True:
        x=input("enter what u want to speak:")
        if x=='q':
            y="bye bye mate"
            speak = wincom.Dispatch("SAPI.SpVoice")
            speak.Speak(y)
            break
        speak=wincom.Dispatch("SAPI.SpVoice")
        speak.Speak(x)
        