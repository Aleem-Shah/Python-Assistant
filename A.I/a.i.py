
# all import commands
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import weather_forecast as wf
import time
import random


#  importing weather 
wf.forecast(place = "srinagar" , time=datetime.datetime.now().strftime("%H:%M:%S"), date="2020-12-07", forecast="daily")


print("this A.I was created by Aleem Shah on (26 november 2020)")
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

engine.setProperty('rate',180)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
#another speak for wishing    
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak('Good morning Aleem!')
       
          
        speak('sir i think you should check your mail first and then start your day')
        webbrowser.open('gmail.com')
    elif hour>=12 and hour<18:
        speak('Good afternoon Aleem!')
     
    else:
        speak('Goood Evening aleem!')    

    speak(' aleem i am doc your personal made assistant ')    

wf=str() 
if wf>='10' :
    speak('sir today it will be warmer')
elif wf<='5':
    speak('sir it would be  a little bit colder today')    

def take_command():
    # '''takes input from the user and returns  the string value
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print('Recognizing...')    
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
  
    except Exception as e:
        print("say that again please...")
        return"None"
    return (query)



    
if  __name__ == '__main__':
   wishme()
   while 10>9:
       query= take_command().lower()

        
       
       if "open youtube"in query :
           webbrowser.open('youtube.com')
   
       elif 'wikipedia' in query:
               speak("searching wikipedia sir...")
               query=query.replace('wikipedia',"")
               result=wikipedia.summary(query,sentences=2)
               speak("according to wikipedia")
               print(result)
               speak(result)
       elif "open google" in query:
           webbrowser.open('google.com')

       elif 'open stack overflow'in query:
           webbrowser.open('stackoverflow.com')   

       elif 'open amazon' in query:
           webbrowser.open('amazon.in')    
       elif 'open flipkart'in query:
           webbrowser.open('flipkart.com')    
       elif 'open myntra'in query:
           webbrowser.open('myntra.com')
       elif 'open github'in query:
           webbrowser.open('github.com')        
       elif ' what is time ' in query:
           Time=datetime.datetime.now().strftime("%H:%M:%S")
           speak(Time)
           print(Time)
       elif'open editor'in query:
           codePath="C:\\Users\\shaha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
           os.startfile(codePath)
       elif 'open whatsapp' in query:
           webbrowser.open('web.whatsapp.com') 
       elif'open school' in query:
           webbrowser.open('burnhallschool.ac.in')
       elif'open tuition'in query:
           webbrowser.open('http://srinagar.motion.ac.in/')     
       elif 'open zoom'in query:
           zoompath="C:\\Users\\shaha\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"       
           os.startfile(zoompath)       
       elif 'open gmail'in query:
           webbrowser.open('gmail.com')
       elif 'open word'in query:
           wordpath="C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
           os.startfile(wordpath)
       elif 'what can you do'in query:
           print("I can do whatever you have programmed me to do")
           speak("I can do whatever you have programmed me to do")
       elif 'hello'in query:
           l1=['hola','bonjour','assalamuilikum','nameste','merheba']
           choice=random.choice(l1)
     
           speak(f"{choice} how are you aleem . how is your day going ")
       elif'good'in query:
           print("wow ok do you need my help")    
           speak("wow ok do you need my help")
       elif 'bad'in query:
           print("oh.Well can i do some favour")  
           speak("oh Well can i do some favour")  
       elif 'my friend'in query:
           speak("Numair is your bestie")
           print("Numair you are my bestie")    
       elif 'quotes'in query:
           print('quotes will only waste your time') 
       elif 'open wix'in query:
           webbrowser.open('wix.com')
       elif 'my projects'in query:
           projectpath="E:\\python projects"
           os.startfile(projectpath) 
       elif 'test my speed'in query:
           webbrowser.open('fast.com')
       elif 'open udemy'in query:
           webbrowser.open('udemy.com')
       elif 'open fiver'in query:
           webbrowser.open('fiver.com')      
       elif 'name' in query:
           speak('my name is Doc ')
       elif 'my name'in query:
           speak("you are my master and your name is aleem") 
       elif 'play a game' in query:
           gamepath="E:\\learning\\FIRSTPROJ.PY"
           os.startfile(gamepath)
       elif "git" in query:
           gitpath="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Git\\Git Bash.lnk"  
           os.startfile(gitpath)  
       elif 'stop' in query:
           speak('as you wish sir')
           break
       elif 'bye' in query:
           speak('as you wish sir')
           break
