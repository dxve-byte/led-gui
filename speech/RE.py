from sreco import *
import time
from datetime import datetime
import random
from internetcrab import *

# RE = Rückantworten

def welcome():
	i = random.randint(1,3)
	
	if i == 1:
		tts = gTTS(text="Hey " + owner_name + " wie geht es dir", lang='de')
	elif i == 2:
		tts = gTTS(text="Ein wunderschönen guten Tag " + owner_name, lang='de')
	elif i == 3:
		tts = gTTS(text="Hey na was läuft", lang='de')
		
	tts.save("output.mp3")
	playsound("output.mp3")

def time():
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")

	tts = gTTS(text="Es ist " + current_time, lang='de')
	tts.save("output.mp3")
	playsound("output.mp3")
	
	#reco()

def weather():
	#print(iweather)

	tts = gTTS(text=iweather, lang='de')
	tts.save("output.mp3")
	playsound("output.mp3")

def hay():

	i = random.randint(1,3)
	
	if i == 1:
		tts = gTTS(text="Mir gehts gut ein schöner Tag heut", lang='de')
	elif i == 2:
		tts = gTTS(text="Es könnte mir nicht besser gehen", lang='de')
	elif i == 3:
		tts = gTTS(text="Mir gehts Super", lang='de')

	tts.save("output.mp3")
	playsound("output.mp3")
	
def way():

	if sex == "female":
		txt = "Mein Name ist " + robotname + " und ich bin deine persönliche Assistentin für Sprachsteuerung"
		tts = gTTS(text=txt, lang='de')
	elif sex == "male":
		tts = gTTS(text="Mein Name ist " + robotname + " und ich bin dein persönlicher Assistent für die Sprachsteuerung", lang='de')
	tts.save("output.mp3")
	playsound("output.mp3")

def insult():
	i = random.randint(1,3)

	if i == 1:
		tts = gTTS(text="Das ist aber nicht nett", lang='de')
	elif i == 2:
		tts = gTTS(text="Okay ich versuche mich zu verbessern", lang='de')
	elif i == 3:
		tts = gTTS(text="Danke für das Feedback", lang='de')
		
	tts.save("output.mp3")
	playsound("output.mp3")
	
def sleeptrue():
	tts = gTTS(text="Ruhemodus eingeschaltet", lang='de')
	tts.save("output.mp3")
	playsound("output.mp3")
	
def sleepfalse():
	tts = gTTS(text="Ruhemodus ausgeschaltet", lang='de')
	tts.save("output.mp3")
	playsound("output.mp3")
	
