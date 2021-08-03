#IMPORTANT
#Riley,Is a virtual assistant
#   Copyright (C) 2021  Dexter
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 3 of the License, or
#   (at your option) any later version.
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software Foundation,
#   Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA
#   This is free software, and you are welcome to redistribute it












#imports
import imaplib, email
import pickle 
import re
import wolframalpha
import pickle
import imaplib, email 
from multiprocessing import Process
import ctypes
import multiprocessing 
from gingerit.gingerit import GingerIt
from pyNewsApi import PYNEWS
from vosk import Model, KaldiRecognizer
import pyjokes
from word2number import w2n
import geocoder
try:
    import pywhatkit
    import pywhatkit as kit
except :
    print("you need an active internet connection for some features to work")
    
from translate import Translator
import os
import psutil
from PyDictionary import PyDictionary
import json
import pyttsx3
import os
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import smtplib
import pyaudio #pip install pyaudio
import pyautogui
import time
import random
import requests
import subprocess
import platform
import requests
import bs4
import pickle
from datetime import datetime as dt
import time as tl
import pickle
import language_check
import random
from newspaper import Article
import string
try:
	from googlesearch import search
except ImportError:
	print("No module named 'google' found")

#defs


def string(s):  
    
    # initialize an empty string 
    str1 = " " 
    
    # return string   
    return (str1.join(s))



def dump_routine():
    time_ = input("time: ")
    activity_ = input("what do you do?:>> ")


    routine = {time_ : activity_}
    print(routine)
    while True:
        time_ = input("time: ")
        activity_ = input("what do you do?:>> ")
        if "done" in time_ or "done" in activity_:
            break
        else:
            routine.update({time_ : activity_})
            print(routine)
    with open('routine', 'ab') as handle:
        pickle.dump(routine, handle, protocol=pickle.HIGHEST_PROTOCOL)


def splt(word):
    return [char for char in word]
text = "nope"


def clean():
    empty_list = []
#Open the pickle file in 'wb' so that you can write and dump the empty variable
    openfile = open('alarms', 'wb')
    pickle.dump(empty_list, openfile)
    openfile.close()






now = dt.now()


    
# Python code to merge dict using update() method
def string(s):  
    
    # initialize an empty string 
    str1 = " " 
    
    # return string   
    return (str1.join(s))


                
                    
change = 1

    #importing all modules
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
    # print(voices[1].id)
engine.setProperty('voice', voices[change].id)

               
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("GO AHEAD")
        r.pause_threshold = 3
        audio = r.listen(source)
    try:
        print("ummmmmmmm gimme a sec let me check what i got...")    
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")

    except Exception :
        # print(e)    
        print("i am not sure i got that")  
        return "None"
    return query

def speak(text):
    engine.say(text)
    engine.runAndWait() 
def taskexecution(x):
    print(x)
    def ping_ip(current_ip_address):
        
        try:
            
            output = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower(
                
                ) == "windows" else 'c', current_ip_address ), shell=True, universal_newlines=True)
            
            if 'unreachable' in output:
                
                return False
            else:
                return True
        except Exception:
            return False

    def write():
        while True:
            print("'done'to exit")
            name = input("what do you call the person:>> ")
            email = input("their gmail id:>> ")
            password = input("their google account password:>> ")
            a = name
            b = email
            c = password
            if "done" in name:
                break
            elif "done" in email:
                break
            elif "done" in password:
                break
            with open('a', 'ab') as handle:
                pickle.dump(a, handle, protocol=pickle.HIGHEST_PROTOCOL)
            with open('b', 'ab') as handle:
                pickle.dump(b, handle, protocol=pickle.HIGHEST_PROTOCOL)
            with open('c', 'ab') as handle:
                pickle.dump(c, handle, protocol=pickle.HIGHEST_PROTOCOL)


    def mydata():
        
        lis = ["name" , "songs" , "band" , "wakeup" , "sleep" , "email" , "hobby" ,"youtube" , "password"]
        print("note that the time is 24 hour format")
        name = input("what should i call you?>> ")

        songs = input("what kind of songs do you like?>> ")
        band = input("what is your favorite band? >> ")
        your_email = input("your gmail id >>")
        your_password = input("google account password>> ")
        hobbies = input("what are your hobbies>> ")
        yt_channels = input("what is the channel you watch the most(only one)>> ")
        wakeup = input("what time do you generally wake up>> ")
        sleep_time = input("what time do you usually sleep?>> ")
        info = [name , songs , band , wakeup , sleep_time,your_email ,hobbies , yt_channels,your_password]
        
        with open('lis', 'ab') as handle:
            pickle.dump(lis, handle, protocol=pickle.HIGHEST_PROTOCOL)
        with open('info', 'ab') as handle:
            pickle.dump(info, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def my_email():
        email = input("whats your email id?>>")
        pswd  = input("whatsa your password?>>>")
        
        with open('my_email', 'ab') as handle:
            pickle.dump(email, handle, protocol=pickle.HIGHEST_PROTOCOL)
        with open('my_email_password', 'ab') as handle:
            pickle.dump(pswd, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def my_friends():
       
        na_me= input("what do you call the person:>> ")
        email_id = input("their gmail id:>> ")
        
        a = na_me
        b = email_id
        

        with open('na_me', 'ab') as handle:
            pickle.dump(a, handle, protocol=pickle.HIGHEST_PROTOCOL)
        with open('email_id', 'ab') as handle:
            pickle.dump(b, handle, protocol=pickle.HIGHEST_PROTOCOL)
    def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("Good Morning!")

        elif hour>=12 and hour<18:
            speak("Good Afternoon!")   

        else:
            speak("Good Evening!")  

        speak("I am riley sir,how may i help you?")       


    def sendEmail(to, content):
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('<Email id>', '<Email passwd>')
        server.sendmail('<Email id>', to, content)
        server.close()


    def file_read():
        try:
            with open ("data.txt", "r") as myfile:
            
            
                            
                da=myfile.readlines()
                data = da
                print(data)
                lol= (data[0])
                print(lol)       
                mame = lol.split(" ")  
                print(mame[2]) 
                name_1 = mame[2]
                speak(name_1)
        
        except:
            pass
        
            
    # Import the core lib
    def priority():
        while True:
            
            email = input("what is the email id: ").lower()
            emails = [email]
            if "done" in email:
                break
            else:
                
                with open('important_emails', 'ab') as handle:
                    pickle.dump(emails, handle, protocol=pickle.HIGHEST_PROTOCOL)

    # Import NLU classifier
    def get_body(msg): 
        if msg.is_multipart(): 
            return get_body(msg.get_payload(0)) 
        else: 
            return msg.get_payload(None, True) 

                                    # Function to search for a key value pair 
    def search(key, value, con): 
        result, data = con.search(None, key, '"{}"'.format(value)) 
        return data 

                                    # Function to get the list of  under this label 
    def get_emails(result_bytes): 
        msgs = [] # all the email data are pushed inside an array 
        for num in result_bytes[0].split(): 
            typ, data = con.fetch(num, '(RFC822)') 
            msgs.append(data) 

        return msgs 
    change = 1

    #importing all modules
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # print(voices[1].id)
    engine.setProperty('voice', voices[change].id)
    # Speech Synthesis
    def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("GO AHEAD")
            r.pause_threshold = 3
            audio = r.listen(source)
        try:
            print("ummmmmmmm gimme a sec let me check what i got...")    
            query = r.recognize_google(audio)
            print(f"User said: {query}\n")

        except Exception :
            # print(e)    
            print("i am not sure i got that")  
            return "None"
        return query

    def speak(text):
        engine.say(text)
        engine.runAndWait()
    model = Model("modl")
    rec = KaldiRecognizer(model, 16000)

    # Opens microphone for listening.
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
    stream.start_stream()
    wishMe()
    while True:
        data = stream.read(1024)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            # result is a string
            result = rec.Result()
            # convert it to a json/dictionary
            result = json.loads(result)
            text = result['text']
            
            print(text)
            query = text.lower()
            result = GingerIt().parse(query)
            print(len(result['corrections']))

            for i in range(len(result['corrections'])):
                print(result['corrections'][i])
                                


            lala = result['result']
            query = lala.lower()
            
            
            
                        
                        
            #processing the input            
                        
            if 'wikipedia' in query :
                try:
                    
                        
                    speak(f' hold up while i search Wikipedia...')
                    la = query.replace("wikipedia", "")
                    la = la.replace("meaning","")
                    la = la.replace("of","")
                    la = la.replace("off","")
                    la = la.replace("word","")
                    la = la.replace("an" , "")
                    la = la.replace("a","")
                    la = query.replace("synonym" , "")
                    la = la.replace("of","")
                    la = la.replace("off","")
                    la = la.replace("for", "")
                    la = query.replace("other","")
                    la = la.replace("off","")
                    la = la.replace("of","")
                    la= la.replace("word","")
                    la= la.replace("words","")
                    la = la.replace("for","")
                    la = la.replace("to" , "")
                    la= la.replace("2","")
                    la = la.replace("two","")
                    la = la.replace("what","")
                    la = la.replace("is","")
                    la = la.replace("are","")
                    print(la)
                    results = wikipedia.summary(la, sentences=2)
                    file_read()
                    speak(f" According to Wikipedia")
                    print(results)
                    
                    speak(results)
            #searching wikipedia
                except:
                    file_read()
                    speak(f"looks like wikipedia has no information about it whatsoever")
            elif "ceo" in query and "google" in query and "who" in query:
                speak("sundarajan pichai also known as sundar pichai is the director and ceo of google inc and also alphabet inc, if you use google chrome you better thank him") 
            elif "what" in query and "mean" in query or "meaning" in query:
                if "what" in query:
                    la = query.replace("what", "")
                    la = la.replace("does","")
                    la = la.replace("mean","")
                    la = la.replace("an","")
                    la = la.replace("a","")
                    la = query.replace("synonym" , "")
                    la = la.replace("of","")
                    la = la.replace("off","")
                    la = la.replace("for", "")
                    la = query.replace("other","")
                    la = la.replace("off","")
                    la = la.replace("of","")
                    la= la.replace("word","")
                    la= la.replace("words","")
                    la = la.replace("for","")
                    la = la.replace("to" , "")
                    la= la.replace("2","")
                    la = la.replace("two","")
                    la = la.replace("what","")
                    la = la.replace("is","")
                    la = la.replace("are","")
                elif "meaning" in query:
                    la = query.replace("meaning","")
                    la = la.replace("of","")
                    la = la.replace("off","")
                    la = la.replace("word","")
                    la = la.replace("an" , "")
                    la = la.replace("a","")
                    la = query.replace("synonym" , "")
                    la = la.replace("of","")
                    la = la.replace("off","")
                    la = la.replace("for", "")
                    la = query.replace("other","")
                    la = la.replace("off","")
                    la = la.replace("of","")
                    la= la.replace("word","")
                    la= la.replace("words","")
                    la = la.replace("for","")
                    la = la.replace("to" , "")
                    la= la.replace("2","")
                    la = la.replace("two","")
                    la = la.replace("what","")
                    la = la.replace("is","")
                    la = la.replace("are","")
                else:
                    speak("which word's meaning do i have to find?")
                    la = takeCommand()
                    
                    
                try:
                    
                    dictionary=PyDictionary()
                    print (dictionary.meaning(la))
                    speak (dictionary.meaning(la))
                except:
                    speak("i dont know what {la} means")
                                        
            elif "add " in query and "device" in query or "register" in query and "device" in query:
                speak("text input only")
                write()
                
            elif 'open youtube'in query or "youtube kholo" in query:
                try:
                    webbrowser.open("youtube.com")
                except:
                    speak(" i think youtube doesnt like me, i am unable to open it")
                


            elif "synonym" in query or "other word" in query or "synonyms" in query or "other words" in query:
                try:
                        
                    if "synonym" in query:
                        la = query.replace("synonym" , "")
                        la = la.replace("of","")
                        la = la.replace("off","")
                        la = la.replace("for", "")
                        la = query.replace("other","")
                        la = la.replace("off","")
                        la = la.replace("of","")
                        la= la.replace("word","")
                        la= la.replace("words","")
                        la = la.replace("for","")
                        la = la.replace("to" , "")
                        la= la.replace("2","")
                        la = la.replace("two","")
                        la = la.replace("what","")
                        la = la.replace("is","")
                        la = la.replace("are","")
                    elif "other" in query:
                        la = query.replace("other","")
                        la = la.replace("off","")
                        la = la.replace("of","")
                        la= la.replace("word","")
                        la= la.replace("words","")
                        la = la.replace("for","")
                        la = la.replace("to" , "")
                        la= la.replace("2","")
                        la = la.replace("two","")
                        la = la.replace("what","")
                        la = la.replace("is","")
                        la = la.replace("are","")
                    elif "synonyms" in query:
                        
                        la = query.replace("synonym" , "")
                        la = la.replace("of","")
                        la = la.replace("off","")
                        la = la.replace("for", "")
                        la = query.replace("other","")
                        la = la.replace("off","")
                        la = la.replace("of","")
                        la= la.replace("word","")
                        la= la.replace("words","")
                        la = la.replace("for","")
                        la = la.replace("to" , "")
                        la= la.replace("2","")
                        la = la.replace("two","")
                        la = la.replace("what","")
                        la = la.replace("is","")
                        la = la.replace("are","")
                    else:
                        speak("which words synonym do you want?")
                        la = takeCommand()
                    print (dictionary.getSynonyms(la))
                    speak(dictionary.getSynonyms(la))
                except:
                    speak("i couldnt find any synonyms for the word {la}")
                    

            elif 'open google' in query or "google kholo" in query :
                try:
                    webbrowser.open("google.com")
                except:
                    speak(" i guess i am dumb or technologically challenged,i am unable to do it")
            
            
                
                
            elif "search the web" in query or "google" in query and "ceo" not in query or "find results online" in query or "i wana search "  in query or "search" in query :
                
                try:
                    if "search the web" in query:
                        query.replace("search the web", "")
                    elif "google" in query:
                        query.replace("google", "")
                    elif "find results" in query:
                        query.replace("find results", "")
                    elif "i wana search something":
                        query.replace("i wana search ", "")
                    elif "search" in query:
                        query.replace("search","")
                    else:
                        speak("what do you want me to search for?")
                        query = takeCommand().lower()
                        
                        
                    city = query


                    url = "https://google.com/search?q=" + city

                    # Sending HTTP request
                    request_result = requests.get( url )

                    # Pulling HTTP data from internet
                    soup = bs4.BeautifulSoup( request_result.text
                                            , "html.parser" )

                    # Finding temperature in Celsius.
                    # The temperature is stored inside the class "BNeawe".
                    temp = soup.find( "div" , class_='BNeawe' ).text
                        
                    print( temp )
                    
                except:
                    speak("i wasnt able to do it")
                
                
                    
    
            
            
            elif 'open stackoverflow' in query or "i need help with computers" in query or "mujhe computer ke bar mein jaan na hai" in query:
                try:
                    webbrowser.open("stackoverflow.com")
                except:
                    speak("  stack over flow was rude to me,so i am not going to open it!!")   

    #opeing stackoverflow



            elif 'play ' in query or "player" in query or "videos" in query or "song" in query or "sing" in query or "video" in query  or "songs" in query or "music" in query or "youtube" in query:
                
                        
                try:
                    if "play" in query:
                        la = query.replace("play", "")
                    elif "youtube" in query:
                        la = query.replace("youtube","")
                    elif "you tube" in query:
                        la = query.replace("you tube" , "")
                        
                    elif "player" in query:
                        la = query.replace("player", "")
                    elif "video" in query:
                        la = query.replace("videos", "")
                    elif "song" in query:
                        la = query.replace("song", "")    
                    elif "sing" in query:
                        la = query.replace("sing", "")    
                    elif "video" in query:
                        la = query.replace("video", "")
                    elif "songs" in query:
                        la = query.replace("songs", "")
                    else:
                        speak('what do you want me to play')
                        la = takeCommand()
                            
                    
                    
                    pywhatkit.playonyt(la)
                    
                    tl.sleep(4)
                    pyautogui.press("space")
                    speak(f"playing {la}.........")
                
                except Exception as e:
                    print(e)
                    speak(" i am unable to do it Sir")
                #playing videos
                
            
    #playing a song

            elif 'the time' in query or "time is it" in query or "samay kya hai" in query:
                try:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                    speak(f"Sir, the time is {strTime}")
                    print(f"Sir, the time is {strTime}")
                except:
                    speak("time to buy a new watch,i lost my watch i might need some help finding it sir,until then i am sorry and helpless")
            #Time
            
            
            
            elif "play my" in query and "music" or "play my" in query and "videos" or "youtube playlists" in query or "youtube playlists" in query:
                try:
                    pywhatkit.playonyt("https://www.youtube.com/playlist?list=WL")
                    speak("playing your videos from youtube playlist")
                except:
                    speak("i wasnt able to access the youtube playlist")
            elif 'open code' in query or "i need to code" in query or "program" in query or "code kholo" in query :
                try:
                    codePath = "C:\\Users\\lalit.DESKTOP-M4ALJ0O\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(codePath)
                except:
                    speak(" i have many excuses to give, but this is a genuine one")
            
            
            
            
            elif "switch tab" in query or "switch window" in query or "change tab" in query or "change window" in query or "other tab" in query or " window" in query :     
                try:
                    speak("switching")
                    pyautogui.keyDown("alt")
                    pyautogui.press("tab")
                    pyautogui.press("tab")
                    pyautogui.press("tab")
                    pyautogui.keyUp("alt")
                    speak("this one?")
                    query1 = takeCommand()
                    if "not this" in query1 or "nah" in query1 or "other one" in query1 or "again" in query1 or "no " in query:
                        try:
                            speak("switching")
                            pyautogui.keyDown("alt")
                            pyautogui.press("tab")
                            
                            pyautogui.keyUp("alt")
                        except:
                            speak("i am sorry but i am too dumb to do that")
                        
                    else:
                        pass
                except:
                    speak("the keyboard shortcut is alt + tab ")
            
            
            elif "text" in query or " send message " in query:
                try:
                    
                    if "text" in query:
                        la = query.replace("text","")
                    elif "message" in query:
                        la = query.replace("message", "")
                    elif "send message" in query:
                        la = query.replace("send message","")
                    else:
                        speak("who should i send it to?")
                        la = takeCommand()
                    lol = la
                    
                    speak("what do you want to say")
                    message = takeCommand()
                    if "say" in message:
                        message = message.replace("say","")
                    else:
                        pass
                    speak(f"saying {message}")
                            
                    webbrowser.open("web.whatsapp.com")
                    tl.sleep(25)
                    
                    pyautogui.press("Tab")
                    
                    pyautogui.typewrite(lol)
                    pyautogui.press("enter")
                    tl.sleep(5)
                    pyautogui.typewrite(message)
                    pyautogui.press("enter")
                    speak("message sent")
                    speak("one more?")
                    ver = takeCommand()
                    if ver == "yes":
                        while True:
                            speak("text whom?")
                            lol = takeCommand()
                            speak("what do you want to say")
                            message = takeCommand()
                            # toggle these if you find any issues :help
                            #webbrowser.open("web.whatsapp.com")
                            #tl.sleep(25)
                            pyautogui.press("Tab")
                            
                            pyautogui.typewrite(lol)
                            pyautogui.press("enter")
                            tl.sleep(5)
                            pyautogui.typewrite(message)
                            pyautogui.press("enter")
                            speak("message sent")
                            speak("one more?")
                            ver_1 = takeCommand()
                            if ver_1 == "yes" or ver_1 == "yeah" or ver_1 == "yup":
                                pass
                            else:
                                break
                    else:
                        pyautogui.keyDown("ctrl")
                        pyautogui.press("w")
                        pyautogui.keyUp("ctrl")
                        
                        
                except:
                    speak("i wasnt able to do that")
                    

            elif 'send an email' in query or "email bhejo" in query or "send" in query and "mail" in query:
                try:
                    speak("What should I say?")
                    content = takeCommand().lower()
                    speak("who should i send it to?")
                    to_who = takeCommand().lower()
                    
                    
                    


                    pickle_file = open("na_me", "rb")
                    objects = []
                    while True:
                        try:
                            objects.append(pickle.load(pickle_file))
                        except EOFError:
                            break
                    pickle_file.close()


                    la = objects.index(to_who)
                    lol =[]
                    lmao = open("email_id" , "rb")
                    while True:
                        try:
                            lol.append(pickle.load(lmao))
                        except EOFError:
                            break
                    pickle_file.close()
                    to = lol[la]
                    print(to)
                    speak(to)
                    sendEmail(to, content)
                    speak("your Email has been sent!")
                except FileNotFoundError as e:
                    print(e)
                    speak("mmmmm looks like you havent introduced any of your friends to me")
                    speak("do you want to add your friends?")
                    hm= takeCommand().lower()
                    if "yeah" in hm or "yes" in hm or "yup" in hm or "ok" in hm or "okay" in hm:
                        speak("you will have to type it")
                        my_friends()
                    else:
                        speak("okay, but i think i should know you more")
                        
                except Exception as x:
                    print(x)
                    speak("i am so sorry but for some reason i am unable to do it")        
                except ValueError:
                    speak(f"i dont think you have introduced {kisko} to me")
            
            elif "add" in query and "friends" in query or "new" in query and "friend" in query or "new" in query and "friends" in query:
                try:
                    speak("you will have to type it")
                    my_friends()
                except:
                    speak("i wasn't able to do that")
            
            #sending emails
            elif "what can you do" in query:
                speak("first say riley to wake me up.say bye(dont say riley) for me to leave ,,,,i can switch tabs for you,just say riley switch tab or something then......i can play a song and i can open youtube and google then, i can tell you the time......... also,i can play i video on youtube,,,i an search the web or even find stuff from wikipedia,just say wikipedia followed by your search.thank you ")
            
                print("first say riley to wake me up,say bye(dont say riley) for me to leave,i can switch tabs for you,just say riley switch tab or something then......i can play a song and i can open youtube and google then, i can tell you the time......... also,i can play i video on youtube,,,i an search the web or even find stuff from wikipedia,just say wikipedia followed by your search.thank you ")

            elif "where am i" in query or "where are we" in query or "locate me" in query or "what is my location" in query:
                speak("locating you")
                try:
                    
                    g = geocoder.ip('me')
                    lol = (g.latlng)
                    lat = (lol[0])
                    lon = (lol[1])
                    speak(f"these are your approx co ordinates latitude {lat} and longitude {lon}")
                    #error
                except Exception as e:
                    speak("sorry sir , i am unable to find you...you can try turning the wifi or data on!")
            elif "joke" in query or "make me laugh" in query or "i am sad" in query:
                try:
                    
                    joke1=pyjokes.get_joke(language='en', category= 'all')
                    speak(joke1)
                except:
                    speak("my sense of humour sucks so please!")
                    pass
                
            elif "weather" in query and "today" in query:
                try:
                    speak("hold on")
                    speak("looking outside")
                    speak("summarising")
                    

                    
                    
                    question = query
                    # App id obtained by the above steps 
                    app_id = "5725TV-GUGG36TVG6" 

                    # Instance of wolf ram alpha 
                    # client class 
                    client = wolframalpha.Client(app_id) 

                    # Stores the response from 
                    # wolf ram alpha 
                    res = client.query(question) 

                    # Includes only text from the response 
                    answer = next(res.results).text 

                    print(answer)
                    speak(answer) 
                    
                
                
                
                    
                        
                
                except:
                    speak("could not check weather make sure you are connected to the internet")
                            
            elif "weather" in query and "tomorrow" in query:
                if 1 == 1:
                    
                    try:
                        
                        speak("fetching tomorrow's weather data")
                    
                    
                        question = query
                        # App id obtained by the above steps 
                        app_id = "5725TV-GUGG36TVG6" 

                        # Instance of wolf ram alpha 
                        # client class 
                        client = wolframalpha.Client(app_id) 

                        # Stores the response from 
                        # wolf ram alpha 
                        res = client.query(question) 

                        # Includes only text from the response 
                        answer = next(res.results).text 

                        print(answer)
                        speak(answer) 
                    except:
                        speak("i am unable to see the future currently please connect to the internet")
                
                
                    
                    
                
            elif "where is"  in query:
                try :
                    speak("who should i find? ")
                    kisko = takeCommand().lower()
                    


                    pickle_file = open("a", "rb")
                    objects = []
                    while True:
                        try:
                            objects.append(pickle.load(pickle_file))
                        except EOFError:
                            break
                    pickle_file.close()


                    la = objects.index(kisko)
                    lol =[]
                    lmao = open("b" , "rb")
                    while True:
                        try:
                            lol.append(pickle.load(lmao))
                        except EOFError:
                            break
                    pickle_file.close()
                    username = lol[la]
                    lala = []
                    kaka = open("c" , "rb")

                    while True:
                        try:
                            lala.append(pickle.load(kaka))
                        except EOFError:
                            break
                    pickle_file.close()
                    password = lala[la]
                    
                    webbrowser.open("https://www.google.com/android/find")
                    tl.sleep(10)
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    
                    pyautogui.typewrite(username)
                    tl.sleep(1)
                    pyautogui.press("enter")
                    tl.sleep(2)
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.press("backspace")
                    pyautogui.typewrite(password)
                    tl.sleep(1)
                    pyautogui.press("enter")
                    tl.sleep(4)
                    speak("found!!!")
                    

                except FileNotFoundError:
                    speak("i am unable to do that,looks like i havent got any infomation about your friends,say add a device")
                except ValueError:
                    speak(f"i dont think i have any information about {kisko}") 
                except :
                    print("i was unable to do that")
                    speak("i was unable to do that")
                                        
                                                
            elif "close window" in query or "close tab" in query or "close" in query:
                speak("should i close the window?")
                hm = takeCommand().lower()
                if "yes" in hm or "ya" in hm or "yeah" in hm or "hmm" in hm or "yup" in hm or "okay" in hm:
                    
                    try:
                        
                        speak("closing")
                        pyautogui.keyDown("alt")
                        pyautogui.press("f4")
                        pyautogui.keyUp("alt")
                        speak("closed")
                    except:
                        speak("its too easy a job for me thats why i decided not to do it")
            elif "read" in query and "mail" in query or "mail" in query or "mails" in query or "email" in query or "emails" in query:
                try:
                    speak("whose mail should i read")
                    lama = takeCommand().lower()
                    kisko = lama
                        


                    pickle_file = open("na_me", "rb")
                    objects = []
                    while True:
                        try:
                            objects.append(pickle.load(pickle_file))
                        
                        
                        
                        except EOFError:
                        
                            break
                    pickle_file.close()


                    la = objects.index(kisko)
                    lol =[]
                    lmao = open("email_id" , "rb")
                    while True:
                        try:
                            
                            lol.append(pickle.load(lmao))
                        except EOFError:
                            break
                    pickle_file.close()
                    username = lol[la]






                    # Importing libraries 
                    
                    user = '<Email id>'
                    password = '<Email passwd>'
                    imap_url = 'imap.gmail.com'
                    


                    


                    # this is done to make SSL connnection with GMAIL 
                    con = imaplib.IMAP4_SSL(imap_url) 

                    # logging the user in 
                    con.login(user, password) 

                    # calling function to check for email under this label 
                    con.select('Inbox') 

                    # fetching emails from this user "tu**h*****1@gmail.com" 
                    msgs = get_emails(search('FROM', username, con)) 

                    # Uncomment this to see what actually comes as data 
                    # print(msgs) 


                    # Finding the required content from our msgs 
                    # User can make custom changes in this part to 
                    # fetch the required content he / she needs 

                    # printing them by the order they are displayed in your gmail 
                    for msg in msgs[::-1]: 
                        for sent in msg: 
                            if type(sent) is tuple: 

                                # encoding set as utf-8 
                                content = str(sent[1], 'utf-8') 
                                data = str(content) 

                                # Handling errors related to unicodenecode 
                                try: 
                                    indexstart = data.find("ltr") 
                                    data2 = data[indexstart + 5: len(data)] 
                                    indexend = data2.find("</div>") 

                                    # printtng the required content which we need 
                                    
                        # to extract from our email i.e our body
                                    
                                    la = (data2[501:5500]) 
                                
                                except UnicodeEncodeError as e: 
                                    pass
                    speak(f"reading the latest email sent by {kisko}")
                    speak(la)
                except FileNotFoundError as e:
                    print(e)
                    speak("i don't know your friends please tell me about your friends")
                except ValueError:
                    speak(f"i cannot find {kisko} in your contacts")
                    
                    
            elif "increase" in query and "volume" in query or "set" in query and "volume" in query or "sound" in query:
                try:
                    
                    query = w2n.word_to_num(query)
                except:
                    query = "50"
                print(query)
                lala= int(query)
                    
                # Import the SendInput object
                SendInput = ctypes.windll.user32.SendInput

                # C struct redefinitions
                PUL = ctypes.POINTER(ctypes.c_ulong)

                class KeyBoardInput(ctypes.Structure):
                    _fields_ = [
                        ("wVk", ctypes.c_ushort),
                        ("wScan", ctypes.c_ushort),
                        ("dwFlags", ctypes.c_ulong),
                        ("time", ctypes.c_ulong),
                        ("dwExtraInfo", PUL)
                    ]

                class HardwareInput(ctypes.Structure):
                    _fields_ = [
                        ("uMsg", ctypes.c_ulong),
                        ("wParamL", ctypes.c_short),
                        ("wParamH", ctypes.c_ushort)
                    ]

                class MouseInput(ctypes.Structure):
                    _fields_ = [
                        ("dx", ctypes.c_long),
                        ("dy", ctypes.c_long),
                        ("mouseData", ctypes.c_ulong),
                        ("dwFlags", ctypes.c_ulong),
                        ("time",ctypes.c_ulong),
                        ("dwExtraInfo", PUL)
                    ]

                class Input_I(ctypes.Union):
                    _fields_ = [
                        ("ki", KeyBoardInput),
                        ("mi", MouseInput),
                        ("hi", HardwareInput)
                    ]

                class Input(ctypes.Structure):
                    _fields_ = [
                        ("type", ctypes.c_ulong),
                        ("ii", Input_I)
                    ]

                VK_VOLUME_MUTE = 0xAD
                VK_VOLUME_DOWN = 0xAE
                VK_VOLUME_UP = 0xAF

                def key_down(keyCode):
                    extra = ctypes.c_ulong(0)
                    ii_ = Input_I()
                    ii_.ki = KeyBoardInput(keyCode, 0x48, 0, 0, ctypes.pointer(extra))
                    x = Input( ctypes.c_ulong(1), ii_ )
                    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


                def key_up(keyCode):
                    extra = ctypes.c_ulong(0)
                    ii_ = Input_I()
                    ii_.ki = KeyBoardInput(keyCode, 0x48, 0x0002, 0, ctypes.pointer(extra))
                    x = Input(ctypes.c_ulong(1), ii_)
                    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


                def key(key_code, length = 0):    
                    key_down(key_code)
                    tl.sleep(length)
                    key_up(key_code)


                def volume_up():
                    key(VK_VOLUME_UP)


                def volume_down():
                    key(VK_VOLUME_DOWN)

                def set_volume(int):
                    for _ in range(0, 50):
                        volume_down()
                    for _ in range(int // 2):
                        volume_up()
                try:
                    speak(f"setting volume to {lala} percent")        
                    set_volume(lala)
                    speak(f"volume set to {lala} percent")
                except:
                    pass
            elif "news" in query:
                try:
                    if 1==1:
                        try:
                            pickle_file = open("info", "rb")
                            objects = []
                            while True:
                                
                                try:
                                    objects.append(pickle.load(pickle_file))
                                except EOFError:
                                    
                                    break
                            pickle_file.close()
                            la = objects.index(7)
                        except FileNotFoundError:
                            speak(" i dont know your hobbies")
                            speak("any specific topic that you want the news on?")
                            la = takeCommand().lower()
                            if "no" in la or "na" in la or "nope" in la or "nah" in la or "nothing" in la or "upto you" in la or "you decide" in la or "your call" in la or "random" in la and "dont" not in la :
                                speak("okay reading some random news")
                                la = "latest"
                        except:
                            speak(" i dont know your hobbies")
                            speak("any specific topic that you want the news on?")
                            la = takeCommand().lower()
                            if "no" in la or "na" in la or "nope" in la or "nah" in la or "nothing" in la or "upto you" in la or "you decide" in la or "your call" in la or "random" in la and "dont" not in la :
                                speak("okay reading some random news")
                                la = "latest "
                        
                        try:
                                
                            query = f"{la} news"

                            for j in search(query, tld="co.in", num=2, stop=2, pause=2):
                                print(j)
                            
                            article = Article(j,language="en")
                            article.download()
                            article.parse()
                            article.text
                            speak(article.title)
                        except:
                            print("failed to find news")
                except:
                    

                    speak("i am unable to read the news currently")
                    
            
            
            elif "translate" in query or "speak" in query and "language" in query or "trouble understanding" in query or "trouble speaking" in query:
                try:
                    
                    speak("what do you want me to translate")
                    la = takeCommand().lower()
                    speak("to which language")
                    lang = takeCommand().lower()
                    translator= Translator(to_lang= lang)
                    translation = translator.translate(la)
                    speak (translation)
                except:
                    speak("i am not sure i know that language")
            
            
            
                
                
            elif "remember" in query or "list " in query:
                
                speak("what should i remember")
                rem = takeCommand()

                with open('x', 'ab') as handle:
                    pickle.dump(rem, handle, protocol=pickle.HIGHEST_PROTOCOL)
                
                    
            
            
            
            elif "my list" in query or "what did i ask you to remind" in query :
                try:
                    
                    speak("let me think, my memory is being tested ")
                                                    
                                                


                    pickle_file = open("x", "rb")
                    objects = []
                    while True:
                        try:
                            objects.append(pickle.load(pickle_file))
                        except EOFError:
                            break
                    speak (objects)
                    pickle_file.close()
                except FileNotFoundError:
                    speak("i dont think you asked me to remember anything")
                        
                except ValueError:
                    speak("you didnt ask me to remember anything")

                
                    
            
            
            elif "routine" in query or "timetable" in query:
                speak("edit your routine sir")
                print("note that the time has to be in 12 hour format")
                print("format H:M AM/PM CasESeNsitIve")
                print("enter done in both feilds to save")
                
                dump_routine()
                
                
            
            
            
            
            
                    
                    
                    
            elif "shut down" in query and "computer" in query or "off" in query and "computer" in query:
                try:
                    
                    speak("Do you wish to shutdown your computer ?")
                    shutdown = takeCommand()

                    if shutdown == 'no' or shutdown == 'nope' or shutdown == 'dont' or shutdown == "don't":
                        speak("ok i am not doing it")
                        exit() 
                    else: 
                        speak("shutting down")
                        tl.sleep(5)
                        os.system("shutdown /s /t 1") 
                except: 
                    speak("i wasnt able to do it")
            elif "reboot" in query and "computer" in query or "restart" in query and "computer" in query:
                try:
                    
                    speak("Do you wish to restart your computer ?")
                    shutdown = takeCommand()

                    if shutdown == 'no' or shutdown == 'nope' or shutdown == 'dont' or shutdown == "don't":
                        
                        exit() 
                        speak("ok i am not doing it")
                    else: 
                        speak("rebooting")
                        tl.sleep(2)
                        os.system("shutdown /r /t 1")     
                except: 
                    speak("i wasnt able to do it")
            
            
            elif "cursor" in query or "mouse" in query:
                
                
                pyautogui.moveTo(960,540,  duration = 0) 
                speak("it is in the center of the screen sir")
            elif "sleep" in query:
                
                break
            elif "priority" in query:
                speak("edit your priority list")
                priority()   
            elif "type" in query and "for me" in query or "write" and "for me" in query or "take" in query and "keyboard" in query:
                i = True
                while i == True:
                    try:
                        
                        speak("yes tell me what to type")
                        lala = takeCommand()
                        pyautogui.typewrite(lala)
                        if "done" in lala or "over" in lala or "stop" in lala or "finish" in lala:
                            i = False
                            break
                            
                        else:
                            pass
                    except:
                        speak("i am not very good and fast at typing sir,i think i will pass")
                        speak("anything else that i can help you with")
            
            elif "open" in query or "find" in query and "file" or "search" in query and "file" in query or "search" in query and "something" in query:
                
                speak("please include the extension for more accurate results")
                speak("what is the file , app or the object called")
                la= takeCommand()
                pyautogui.press("windows")
                tl.sleep(1)
                pyautogui.typewrite(la)
                speak("these are the most accurate results")
            
            elif "host" in query and "check" in query or "is" in query and "up" in query or "ping" in query and "server" in query:
                
                

                
                if __name__ == '__main__':
                    speak("what is the host's name?")
                    host = takeCommand()
                    current_ip_address = [host]
                    for each in current_ip_address:
                        if ping_ip(each):
                            print(f"{each} is up")
                            speak(f"{each} is up")
                        else:
                            print(f"{each} is down ")
            
                            speak(f"{each} is down")
            elif "hi" in query or "hai" in query or "hello" in query or "heyyo" in query or "wassup" in query or "sup" in query or "hey" in query:
                
                message = ["hello sir i am riley how may i help you" , 'hello' , "hey" , "wassup" , 'sup']
                la = random.choice(message)
                speak(la)
            elif "battery" in query or "charge" in query or "charging" in query or "how much" in query and "power" in query:
                try:
                    
                    battery = psutil.sensors_battery()
                    battery_1 = battery.percent
                    speak(f"we have {battery_1} percent battery")
                except:
                    print("nope")
            
            
        
            
            elif "cancel" in query or "undo" in query or "previous" in query and "move" in query:
                try:
                
                    pyautogui.hotkey("ctrl","z")
                    speak("undone")
                except:
                    speak("the hotkeys are control z")
            elif "stop playing" in query or "stop" in query or "close" in query and "browser tab" in query :
                try:
                    
                    pyautogui.hotkey("ctrl","w")
                    speak("i am shutting up")                            
            
                except:
                    speak("that may be beyond my abilities at the momment")
                    
                    
                    
            
                    
            elif "shut up" in query or "shutup" in query or "don't listen" in query or "shutting up" in query or "privacy" in query or "stop" in query and "listening" in query or "don't" in query and "attention" in query or "shh" in query or "don't" in query and "bother" in query:
                
                try:
                    while True:
                        lala = takeCommand()
                        if "wake up" in lala or "respond" in lala or "buddy" in lala or "respond" in lala or "riley" in lala or "say" in lala or "speak" in lala or "talk" in lala:
                            
                            speak("gimme a minute sir,i need to get all my stuff up and running")
                            break
                        else:
                            pass    
                
                except:
                    
                    pyautogui.hotkey("function","f10")
            else:
                
                #continue
                wolf(query) 
                print("web")
                            
                                
                              






def power(v):
    print(v)
    import psutil
    import time
    while True:
        tl.sleep(120)
        battery = psutil.sensors_battery()
        plugged = battery.power_plugged
        percent = str(battery.percent)
        plugged = "Plugged In" if plugged else "Not Plugged In"
        lala = (percent+'% | '+plugged)
        ol = percent.replace("%","")
        print(ol)
        ol = int(ol)
        if ol < 50 and ol > 45:
            speak(f"we have {ol} percent battery left")
        elif ol < 15 and "Not Plugged In" in lala:
            speak(f"we have {ol} percent battery left")
            speak("i suggest you start charging it")
        elif ol > 90 and "Plugged In" in lala:
            speak("battery is greater than {ol} percent")
            speak("i suggest you stop charging it")




                       


                                                              
                                     
                                       
                            
                           
                
                                
                                   








def wolf(l):
    print(l)
                        
    change = 1

        #importing all modules
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
        # print(voices[1].id)
    engine.setProperty('voice', voices[change].id)
    
    def speak(text):
        engine.say(text)
        engine.runAndWait()
    
    if 1==1:
        if 1==1:
            
            text= l
            
            print(text)
            query = text
            operate = ["add","added","sum","summed","plus","subtract","subtracted","minus","multiply","times","time","multiplied","divide","divided","by","bi","divides"]
            for ope in operate:
                if ope in query:
                    ques = True
                else:
                    ques = False
                
            text = query.lower()
            query = query.lower()

                # Create an object of Gingerit package and pass the text as an paramater to it parse function

            result = GingerIt().parse(text)
            print(len(result['corrections']))

            for i in range(len(result['corrections'])):
                print(result['corrections'][i])
                                


            lala = result['result']
            print(lala)
            query = lala.lower()
            try:
                query_5 = w2n.word_to_num(query)
                query_5 = int(query)
                number = True
            except ValueError as e:
                print(e)
                number = False
            except Exception as e_r:
                print(e_r)
                number = False
            
            operations = ["add","added","sum","summed","plus","subtract","subtracted","minus","multiply","times","time","multiplied","divide","divided","by","bi","divides"]
            
            for operation in operations:
                if operation in query and number == True:
                    google = False
                    
                else:
                    google = True
            
            
            
            
            
            
            if "?" in query and google == True :
                
                try:
                    city = query

            # Generating the url
                    url = "https://google.com/search?q=" + city

                                                # Sending HTTP request
                    request_result = requests.get( url )

                                                # Pulling HTTP data from internet
                    soup = bs4.BeautifulSoup( request_result.text
                            , "html.parser" )

                                                # Finding temperature in Celsius.
                                                # The temperature is stored inside the class "BNeawe".
                    temp_ = soup.find( "div" , class_='BNeawe' ).text
                    #print(f"google: {temp_}") 
                    if "wikipedia" in query:
                        temp_ = ""
                    speak(temp_)
                    
                    wolfram = False  
                    google = True
                except Exception as e :
                    print(e)
                    wolfram = True  
                    google = False              
                    print("i dont know that,asking wolfram")
                    
            else:
                pass
            
            if "?" in query and wolfram == True and google == False or ques == True:
                try:
                    question = query
                    app_id = "5725TV-GUGG36TVG6" 

                                        # Instance of wolf ram alpha 
                                        # client class 
                    client = wolframalpha.Client(app_id) 

                                        # Stores the response from 
                                        # wolf ram alpha 
                    res = client.query(question) 

                                        # Includes only text from the response 
                    answer = next(res.results).text 
                    if "noun" in answer and "meaning" not in question:
                        answer = ""
                                        
                    else:
                        answer = answer
                    if "alarm" in question and "what is" not in question:
                        answer= ""
                    elif "wikipedia" in question:
                        answer = ""
                    else:
                        answer = answer
                                            
                                        
                        speak(answer)
                except Exception as e:
                    print(e)
                    print("i dont know that")
                                
            else:
                pass 



#alarm
#imports for alarms 

import dateutil.parser as dparser
import pickle
from datetime import datetime
from time import sleep




if 1==1:
    
    
    def rmint(s):
        
        Mystr = s
        # Iterates over the chars in the string and joins all characters except digits
        newstr = "".join((item for item in Mystr if not item.isdigit()))
        return newstr


    def string(s):  
            
            # initialize an empty string 
        str1 = " " 
            
            # return string   
        return (str1.join(s))  

    #algorithm to make words into numbers and that stuff 

    #help
    #do it if you can(and remove this comment)






    #algorithm to sort and all that stuff


    def yalaram(x):
        lala = x
        if "morning" in lala:
            lala = lala + "am"
        elif "afternoon" in lala:
            lala = lala + "pm"
        elif "night" in lala:
            lala = lala + "pm"
        else:
            now = datetime.now()

            current_time = now.strftime("%H:%M:%S")
            dt_string = "12:00:00"
            format = "%H:%M:%S"
            current_time = datetime.strptime(current_time, format)
            current_time=current_time.hour
            print(current_time)

            time = datetime.strptime(dt_string, format)
            time =time.hour
            print(time)
            try:
                if current_time > time:
                    lala = lala + "pm"
                elif current_time > time:
                    lala = lala + "am"
                else:
                    lala = lala + "pm"
            except:
                lala = lala + "am"
                    
            
        try:
            date = (dparser.parse(lala,fuzzy=True))
            print(type(date))
            print(date)
            lalala = str(date)
            lol = lalala.split(" ")
            print (lol)
            d = lol[0]
            t = lol[1]
            d = d.split("-")
            print(d)

            date = d[2]
            date = int(date)

            print(date)
            if "tomorrow" in lala and "day after" not in lala:
                date +=1
                print(date)
            elif "day after tomorrow" in lala:
                date +=2
                print(date)   
            print(date)

            new = lol[0]
            print(new)
            new = new.split("-")

            date = str(date)
            new[2] = date

            print(new)
            new = string(new)
            print(new)
            new = new.replace(" ","-")

            print(new)



            print(t)

            final = [new+" "+ t]
            #print(final)
            remind = lala.replace("remind","")
            remind = lala.replace("me","")
            remind = lala.replace("to","")
            remind = lala.replace("morrow","")
            remind = lala.replace("day after","")
            remind = lala.replace(":","") 
            remind = lala.replace("pm","") 
            remind = lala.replace("PM","") 
            remind = lala.replace("am","")
            remind = lala.replace("AM","")  
            remind = rmint(remind)
            print(remind)
        except Exception as e:
            print(e)
            print("error(s) occurred")
            
        final = string(final)
        print(final)
        dump=final
        #putting it in the file
        try:
            with open('aalarms', 'ab') as handle:
                pickle.dump(dump, handle, protocol=pickle.HIGHEST_PROTOCOL)
                
        except Exception as e:
            print(e)





#imports

import dateutil.parser as dparser
import pickle
from datetime import datetime
from time import sleep


def alarm_runing():
   


    ########defs######
    def flattenList(data):
        results = []
        for rec in data:
            if isinstance(rec, list):
                results.extend(rec)
                results = flattenList(results)
            else:
                results.append(rec)
        return results

    ######code#######
    x=0
    while True:
        sleep(2)


            


        #reading the data


        pickle_file = open("aalarms", "rb")
        objects = []
        while True:
            try:
                objects.append(pickle.load(pickle_file))
            except EOFError:
                break  
        objects=flattenList(objects)    
        print(objects) 
        #make True if needed help
        data = sorted(objects, reverse=False)
        
        
        while True:
            try:
                sleep(2)
                tme = data[x]

                print(tme)

                now = datetime.today()
                try:
                    time = datetime.strptime(tme, "%Y-%m-%d %H:%M:%S")
                except:
                    print("nothing to do...")
                    sleep(30)
                    break
                print(time)

                if time <= now:
                    print("done")
                    
                    #removing the entry from the list
                    def string(s):  
                            
                            # initialize an empty string 
                        str1 = " " 
                            
                            # return string   
                        return (str1.join(s))  



                    try:
                        objects.remove(tme)
                    except AttributeError:
                        x=0
                    x+=1

                    print("..................................................")
                    
                    print(objects)

                    try:
                        with open('aalarms', 'wb') as handle:
                            pickle.dump(objects, handle, protocol=pickle.HIGHEST_PROTOCOL)
                            
                    except Exception as e:
                        print(e)
                        
                        
                    
                        
                        
                        

                    
                    
                    
                    
                    
                    
                else:
                    print("started")
                    
                    

                
                
                
                
            except IndexError:
                print("out of index moving back to entry one")
                x=0
                break







        






if __name__ == '__main__':
    
    p = Process(target=taskexecution, args=('main task',))
    p3 = Process(target=power, args=('battery check',))
    
    
    #starting
    p.start()
    p3.start()
    
    
    
    #waiting 
    
    p.join()
    p3.join()
    

