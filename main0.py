from requests.sessions import session
import speech_recognition as sr 
import datetime
import wikipedia
import pyttsx3
import webbrowser
import random
import time 
import urllib.parse
import os 
import pyjokes
import PyPDF2
import sys
import operator
import smtplib
import requests 
from requests import get
from email.message import EmailMessage
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisUi2 import Ui_JarvisUi2



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
     engine.say(audio)
     engine.runAndWait()

speak('Initializing the system')
speak('Jarvis is about to load in')
speak('3')
speak('2')
speak('1')
speak('loading GUI')
speak('please press the start button to activate jarvis')
speak('or click stop to terminate')


def Intro():
     hour = int(datetime.datetime.now().hour)
     if hour>=0 and hour<12:
          speak('Good Morning Sir!')
     elif hour>=12 and hour<18:
          speak('Good Afternoon Sir!')
     elif hour>=18 and hour<24:
          speak('Good Evening Sir!')
     else:
          speak('Good Night Sir!')
     time()
     #speak("I am Jarvis, your own personal digital voice assistant")
     #speak("what do you want me do")
     speak("Jarvis is Present at your Service, Ask me something good")
     speak("i will try my best to serve you")
     speak('Ears out, hearing now')


def time():
     Time = datetime.datetime.now().strftime("%I:%M:%S")
     speak('the current time is: ')
     speak(Time)

def date():
     year = int(datetime.datetime.now().year)
     month = int(datetime.datetime.now().month)
     day = int(datetime.datetime.now().day)
     speak('Todays date is')
     speak(day)
     speak(month)
     speak(year)

def readpdf():
     book = open('pdf.pdf','rb')
     pdfReader = PyPDF2.PdfFileReader(book)
     pages = pdfReader.numPages
     speak(f"number of pages in this book are{pages}")
     speak('Please Enter the page number you want me to read')
     pagess = int(input('Please Enter the page number:'))
     page = pdfReader.getPage(pagess)
     text = page.extractText()
     speak(text)



def news():
     main_url = "https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=1de0a7393a6c438692c607e135548a58"
     open_bbc_page = requests.get(main_url).json()
     article = open_bbc_page["articles"]
     results = []
     headline = ["first","second","third","fourth","fifth"]
     for i in article:
          print (results.append(i["title"]))
     for i in range(len(headline)):
          print(f"Todays {headline[i]} headline is : {results[i]}")
          speak(f"{headline[i]} headline is : {results[i]}")
     speak("Thats it for now")
     speak("I will inform you the updates later")
     speak("Just say News")


def send_email(receiver, subject, messagee):
     server = smtplib.SMTP('smtp.gmail.com',587)
     server.starttls()
     server.login('mail', 'password')
     email = EmailMessage() 
     email['From'] = 'mail'
     email['To'] = receiver
     email['Subject'] = subject
     email.set_content(messagee)
     server.send_message(email)

email_list = {

     'abhi' : 'abhishekkatte05@gmail.com',
     'rahul' : 'rahulnimbargikar@gmail.com'
}




class MainThread(QThread):
     def __init__(self):
          super(MainThread, self).__init__()

     def run(self):
          self.TaskExecution()
     
     def coms(self):
          r = sr.Recognizer()
          with sr.Microphone(device_index=0) as source:
               print('Ears Out')
               r.pause_threshold = 2 
               r.adjust_for_ambient_noise(source)
               audio = r.listen(source,timeout=4,phrase_time_limit=7)
          try:
               print('Recognizing audio')
               text = r.recognize_google(audio,language='en-in')
               print(text)
          except Exception:
               #speak('Sorry, could not understand audio')
               #speak('i do not speak alien language')
               #speak('maybe consider checking your Internet connection and try again')
               #print('Error')
               return "none"
          #query = query.lower()
          #return query
          return text

     def TaskExecution(self):
          Intro()
          while True:
          #if 1:
               self.query = self.coms().lower()
               
          
               if 'wikipedia' in self.query:
                    speak('Searching wikipedia')
                    self.query = self.query.replace('wikipedia','')
                    results = wikipedia.summary(self.query, sentences = 2)
                    speak('According to wikipedia')
                    speak(results)

               elif 'hello' in self.query or 'hey' in self.query:
                    speak('Hello sir hope you had an awesome day')

               elif 'what is your name' in self.query:
                    speak('My name is jarvis')
                    speak('I am famous you might have heard about me')

               elif 'what are you' in self.query or 'what do you do' in self.query:
                    speak('I am an virtual assistant')

               elif 'how are you' in self.query:
                    speak('perfectly fit to assist you')

               elif 'my name is' in self.query:
                    speak('glad to know')

               elif 'whom do you work for' in self.query:
                    speak('i work for anyone and everyone')
                    speak('especially if you are good to me')

               elif 'what is full form of jarvis' in self.query:
                    speak('Just a rather very intelligent system')

               elif 'what do you eat' in self.query or 'what is your fuel' in self.query:
                    speak('every bit of information you have for me')

               elif 'whats up' in self.query:
                    sts = ('Just fueling my energy','trying to learn some secret information','just doing my daily chores what about you')
                    speak(random.choice(sts))

               elif 'do you have superpowers' in self.query:
                    speak('Patience is my superpower')

               elif 'laugh' in self.query:
                    speak('hahahah hahahha hahahahaha')

               elif 'dumb' in self.query or 'useless' in  self.query:
                    speak('Sorry to disappoint you')
                    speak('I hope you will teach me better')

               elif 'thank you' in self.query:
                    comp = ('Cheers! Always happy to help','make it a habit','I dont like compliments','you are lucky to have me')
                    speak(random.choice(comp))

               elif 'corona' in self.query:
                    webbrowser.open("https://covid19.who.int/?gclid=Cj0KCQjw16KFBhCgARIsALB0g8JapBp65cINTqidLjDZ3RKsB87vMeXrQj06e5CSwobtHwWzHfNb1fYaAmTAEALw_wcB")
                    speak('this is the current update of active cases')
                    speak('situation seems bad for humans right now')
                    speak('sometimes i feel lucky for not having a flesh')

               elif 'what can you do' in self.query:
                    speak('1 I can tell you jokes')
                    speak('2 I can search various things on internet for you')
                    speak('3 I can read you a pdf')
                    speak('4 I can remember things for you')
                    speak(' and Most importantly I can help you pass time as you all are mostly single he he he')

               elif 'open youtube' in self.query or 'Search for videos online' in self.query:
                    webbrowser.open("https://www.youtube.com") 
                    speak('Opening Youtube')  

               elif 'open google' in self.query:
                    webbrowser.open("https://google.com")
                    speak('opening google')

               elif 'news' in self.query or 'what is happening around the world' in self.query:
                    speak("Searching for news around the globe")
                    news()

               elif 'open github' in self.query:
                    speak("opening github")
                    webbrowser.open("https://github.com")

               elif 'yahoo' in self.query:
                    speak("opening yahoo")
                    webbrowser.open("https://in.yahoo.com")

               elif 'time'in self.query:
                    time()

               elif 'date' in self.query:
                    date()

               elif 'open calculator' in self.query:
                    speak('opening calculator')
                    os.system('calc.exe')

               elif 'open command prompt' in self.query:
                    speak('opening command prompt')
                    os.system('start cmd')

               elif 'open spotify' in self.query:
                    speak('opening spotify')
                    os.system('spotify.exe') 

               elif 'open stack overflow' in self.query:
                    webbrowser.open('http://www.stackoverflow.com')

               elif 'location' in self.query:
                    speak('what is the location')
                    loct = self.coms().lower()
                    url = f'https://google.nl/maps/place/{loct}/&amp'
                    webbrowser.get().open(url)
                    speak(f"here is what i found{loct}")

               elif 'search' in self.query:
                    speak("what do you want to search for?")
                    ask = self.coms().lower()
                    webbrowser.open(f'{ask}')
                    speak('i found this on internet')

               elif 'open college portal'  in self.query or 'college website' in self.query:
                    speak('opening your college website')
                    webbrowser.open('https://www.kjei.edu.in/kjcoemr/')


               elif 'open gmail' in self.query:
                    speak('opening gmail')
                    webbrowser.open("https://www.gmail.com")

               elif 'open amazon' in self.query:
                    speak('opening amazon')
                    webbrowser.open("https://www.amazon.in")

               elif 'open flipkart' in self.query:
                    speak('opening flipkart')
                    webbrowser.open("https://www.flipkart.com")

               
               elif 'joke' in self.query:
                    speak(pyjokes.get_joke())   

               elif 'notepad' in self.query:
                    speak('opening notepad')
                    os.system("Notepad")

               elif 'close notepad' in self.query:
                    os.system('taskkill/f/im notepad.exe')
               
               elif 'read pdf'  in self.query or 'read' in self.query:
                    speak('opening pdf file')
                    readpdf() 

               elif 'hide files' in self.query:
                    speak('Are you sure, your files will be hidden until you make them visible')
                    condition = self.coms().lower()
                    if 'hide' in condition or 'yes' in condition:
                         os.system('attrib +h /s /d')
                         speak('All the files are hidden now')
                    elif 'no' in condition:
                         speak('okay')

               elif 'visible' in self.query or 'show hidden files' in self.query:
                    speak('okay, making files visible now')
                    os.system('attrib -h /s /d')

               elif 'alarm' in self.query:
                    speak('sorry, i cannot set an alarm for you right now')
                    speak('but i can remember things for you if you would like')
                    speak('would you like to make a reminder')
                    hear = self.coms().lower()
                    if 'yes' in hear or 'sure' in hear:
                         speak('what do you want me to remember?')
                         data = self.coms()
                         speak('you asked me to remember' + data)
                         remember = open('data.txt','w')
                         remember.write(data)
                         remember.close()
                    elif 'no' in hear or 'not really' in hear:
                         speak('okay I understand')


               elif 'calculate' in self.query or 'calculation' in self.query:
                    r = sr.Recognizer()
                    
                    with sr.Microphone() as source:
                         print("what do you want to calculate")
                         speak("what do you want me to calculate")
                         r.adjust_for_ambient_noise(source)
                         audio = r.listen(source)
                    my_string=r.recognize_google(audio)
                    print(my_string)
                    def get_operator_fn(op):
                         return {
                              '+' : operator.add,
                              '-' : operator.sub,
                              'x' : operator.mul,
                              'divided' :operator.__truediv__,
                              'Mod' : operator.mod,
                              'mod' : operator.mod,
                              '^' : operator.xor,
                              }[op]
                    def eval_binary_expr(op1, oper, op2):
                         op1,op2 = int(op1), int(op2)
                         return get_operator_fn(oper)(op1, op2)
                    print(eval_binary_expr(*(my_string.split())))
                    speak('result is')
                    speak(eval_binary_expr(*(my_string.split())))
                              
               elif 'set a reminder' in self.query:
                    speak('what do you want me to remember?')
                    data = self.coms()
                    speak('you asked me to remember' + data)
                    remember = open('data.txt','w')
                    remember.write(data)
                    remember.close()
                    
               elif 'what did i ask you to remember' in self.query or 'do you remember something' in self.query:
                    remember = open('data.txt','r')
                    speak('you asked me to remember '+ remember.read())

               elif 'play music' in self.query:
                    os.system('spotify.exe')
                    speak('playing a random playlist on spotify')

               elif 'weather' in self.query or 'temperature' in self.query or 'what are conditions like' in self.query or 'climate' in self.query:
                    #speak("what is the city name you want to search the weather for")
                    

                    link = f"https://api.openweathermap.org/data/2.5/weather?q=mumbai&appid=53fcf7e4f8fa5a2631aa41f349aef87c"
                    api_link = requests.get(link).json()
                    #print(api_link)
                    
                    if api_link['cod'] == '404':
                         print("Please check your city name")
                         speak("Invalid city, Please check your city name")
                    else:
                         temp_city = ((api_link['main']['temp']) - 273.15)
                         weather_desc = api_link['weather'][0]['description']
                         hmdt = api_link['main']['humidity']
                         wind_spd = api_link['wind']['speed']
                         print("current temperature is: {:2f} degree Celcius".format(temp_city))
                         print("it is like : ",weather_desc)
                         print("current humidity is:",hmdt, 'percentage')
                         print("current wind speed is:",wind_spd,'kilo meters per hour')
                         speak("current temperature is: {:2f} degree Celcius")
                         speak(f"it is like : {weather_desc}")
                         speak(f"current humidity is:{hmdt}'percentage'")
                         speak(f"current wind speed is:{wind_spd}'kilo meters per hour'")
                                                 


               elif self.query == 'none':
                    continue


               elif  'sleep' in self.query or 'bye' in self.query or 'see you' in self.query or 'quit' in self.query or 'abort' in self.query or 'no' in self.query or 'shut up' in self.query or 'go away' in self.query or 'nothing' in self.query or 'go offline' in self.query or 'take a break' in self.query:
                    speak('sleep mode activated')
                    speak('use the wakeup command to call me again anytime')
          
                    break

               elif 'exit' in self.query or 'close the program' in self.query:
                    speak('may we meet again')
                    exit()

               
               elif 'email' in self.query or 'send an email' in self.query or 'send mail' in self.query or 'mail' in self.query:
                    
                    def get_email_info():
                         speak('to whom you want to send an email')
                         namee = self.coms().lower()
                         receiver = email_list[namee]
                         print(receiver)
                         speak('what is the subject of your email')
                         subject = self.coms().lower()
                         speak('tell me the text in your email')
                         messagee = self.coms().lower()
                         send_email(receiver,subject,messagee)
                         speak('email successfully sent')

                    get_email_info()





               
               #else:
                #    temp = self.query.replace('','+')
                #    g_url="https://www.google.com/search?q="
                #    print("Searching on Internet") 
                #    speak('seems like you havent taught me that yet')
                #    #speak("you want me to search that on internet?")
                #    askin = self.coms().lower()
                #    #if 'yes' in askin:
                #    speak("Searching for results on Internet")   
                #    webbrowser.open(g_url+temp)   
                #    #elif 'no' in askin or 'dont' in askin:
                #         #speak("okay")

               speak('what else can I help you with')

     
          if __name__=='__main__':
               while True:
                    permission = self.coms().lower()
                    if 'wakeup' in permission or 'wake up' in permission or 'hello jarvis' in self.query or 'time to work' in permission or 'hey jarvis' in permission:
                         speak('welcome back')
                         self.TaskExecution()
                    elif "goodbye" in permission or "exit" in permission or "close the program" in permission:
                         speak('may we meet again')
                         sys.exit()


startExecution = MainThread()

class Main(QMainWindow):
     def __init__(self):
          super().__init__()
          self.ui =Ui_JarvisUi2()
          self.ui.setupUi(self)
          self.ui.Start.clicked.connect(self.startTask)
          self.ui.Start_2.clicked.connect(self.close)
        


     def startTask(self):
          self.ui.movie = QtGui.QMovie("mid2.gif")
          self.ui.label_2.setMovie(self.ui.movie)
          self.ui.movie.start()
          self.ui.movie = QtGui.QMovie("robo4.gif")
          self.ui.label_4.setMovie(self.ui.movie)
          self.ui.movie.start()
          timer=QTimer(self)
          timer.timeout.connect(self.showTime)
          timer.start()
          startExecution.start()

     def showTime(self):
          current_time = QTime.currentTime()
          current_date = QDate.currentDate()
          label_time = current_time.toString('hh:mm:ss')
          label_date = current_date.toString(Qt.ISODate)
          self.ui.textBrowser.setText(label_time)
          self.ui.textBrowser_2.setText(label_date)
         
          






app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
sys.exit(app.exec_())


