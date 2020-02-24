# coding=utf-8
# PYTHON SPEECHRECOGNITION by dxve

# *ACHTUNG GOOGLE HAT ANTEILE (Er ist hier für die "Speech to Text" Sache zuständig)*

# Eine Sprachsteuerung für eigene Sprachbefehle und einen "Überblick" über seine Daten


import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os


#Dateien
from internetcrab import *
from RE import *

####################################################### Requirements ################################################
#pip3 install SpeechRecognition ; [for Speech to Text]
#Herunterladen: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio (PyAudio‑0.2.11‑cp37‑cp37m‑win_amd64.whl)
#zu Downloads wechseln und manuell installieren: (cd Downloads, pip install PyAudio-0.2.11-cp37-#cp37m-win_amd64.whl)
#pip3 install gTTS ; for text to Speech
#pip3 install mpyg321 ; for output
#pip3 install bs4 ; for Internet crab
#python -m pip install requests
#pip3 install playsound
#Linux: 
#####################################################################################################################

############################################## EIGENSCHAFTEN ########################################################

owner_name = "dave"		#alles klein schreiben ALLES
robotname = "" 	#Der Robotername(wann das Script auf den Namen reagiert) // Standart: "Alexa"
sex = "female" 			#male/female

#####################################################################################################################

if owner_name == "":
	owner_name = "dave"

if robotname == "":
	robotname = "alexa"
	
if sex == "":
	sex = "female"

############################################ START #################################	


def reco():
											# Versucht ein Mikro zu finden
		r = sr.Recognizer()
		with sr.Microphone() as source:
											# hört zu und nimmt auf
				print("Höre zu..")
				audio = r.listen(source)
					
												# Versucht das Gesprochene mittels Google zu reconieren und in Text umzuwandeln
				result = r.recognize_google(audio, language="de_DE")
				compares(result)				# Wenn ALLES geklappt hat, wird es ausgewertet(compare block)
							
					#tts = gTTS(text=outputs, lang='de')
					#tts.save("output.mp3")
					#playsound('output.mp3')
									# Fehler 1 -> wird weitergegeben und ausgewertet
	
global silentmode
silentmode = "false"


def compares(result):
	result = result.lower() 						# setzt alles auf Kleinbuchstaben, um die Vergleichung zu vereinfachen
	ressplit = result.split()
	print(result)
	
	
	
	exac = []
	bin = []
	resultlist = []
	
	groupscount = len(groups)							# Zählt wie viel Gruppen es gibt
	
	print('The count of p is:', groupscount)
	for all in groups:


		for element in all:								# element = [hey, hallo, hallöchen] usw.
			if element in ressplit:						# Passt Element zu result-string
				#print(result)
				#lastword = resultlist[1]
				bin.insert(0, element)					# Fügt neues Element bei "Bin" hinzu
		exac.insert(999999, len(bin))					# Zählt List(bin) und fügt die Anzahl in eine neue List zu
		bin.clear()										# Löscht die "Bin"-list
	
	
	
	highestval = max(exac)								# Wählt die höchste Zahl aus
	print("exac:", exac)

	
	# Nimmt die 2. höchste Zahl und vergleicht ob sie mit der 1. höchsten gleich ist,
	# um danach zu sagen dass es mehrere Resultate gab und nichts ausgeben kann
	pos = exac.index(highestval)						# Postition von der höchsten Zahl
	exac.remove(highestval)								# Löscht die höchste Zahl
	second_highestval = max(exac)						# Nimmt die 2. höchste Zahl
	
	if highestval == second_highestval:					# Macht jetzt den Vergleichung#
		print("Type Error: To many results, need an exact result..")				# Fehler
	else:
			exac.insert(pos, highestval)
							
	


	# ############################################################
	# ############### WELCHE LIST PASST AM BESTEN ZUM SATZ #################
	# ############################################################


		#if robotname in result:
			#Hier geht er zur Datei RE.py um darauf zu Antworten
			
			
			if pos == 0:
				#search internet
				groupname = "Agroup"
			
			if pos == 1:
				#welcome
				groupname = "Bgroup"
				welcome()
			if pos == 2:
				#time
				groupname = "Cgroup"
				time()
			if pos == 3:
				#weather
				groupname = "Dgroup"
				
				try:
				
					resultlist = result.split()						# schneidet alle Wörter im resultstring aus
					ort = resultlist[resultlist.index("in") + 1]	# sucht "in" und nimmt den ORT [nächstes Wort]
					
					
					r = requests.get("https://www.wetteronline.de/wetter/" + ort)			# hohlt sich URL
					soup = BeautifulSoup(r.text, 'html.parser')								# parst die Seite
					str1 = soup.find(id="forecasttext")										# findet id
					str1.prettify()
					iweather = re.sub('<[^>]*>', '', str(str1))								# löscht Zeichen (<p></p> ; usw.)
					
					weather(iweather)														# startet weather()
				except:
					tts = gTTS(text="Tut mir leid ich weiß nicht welchen Ort du meinst", lang='de')
					tts.save("output.mp3")
					playsound("output.mp3")
				
			if pos == 4:
				#how are you
				groupname = "Egroup"
				hay()
			if pos == 5:
				#where are you
				groupname = "Fgroup"
				way()
			if pos == 6:
				#insult me
				groupname = "Ggroup"
				insult()
			if pos == 7:
				#sleepmode true
				groupname = "Hgroup"
				sleeptrue()
				silentmode = "true"
			if pos == 8:
				#sleepmode false
				groupname = "Igroup"
				sleepfalse()
				silentmode = "false"
			if pos == 9:
				#what can you do
				groupname = "Jgroup"
				wcyd()
			if pos == 10:
				#random number
				groupname = "Kgroup"
				console()
			if pos == 11:
				#random number
				groupname = "Lgroup"
				rn()
		
			
			#print("I think I can classify this in group ", groupname)
	
	

def error(x):

	#silentmode = ""
	print("silentmode: ", silentmode)
	if silentmode == "false":
		if x == 1:
			tts = gTTS(text="Es konnte kein Mikro gefunden werden. Schließen Sie eins an oder wechseln Sie zu den Einstellungen.", lang='de')
			tts.save("output.mp3")
			playsound('output.mp3')
			
		if x == 2:
			tts = gTTS(text="Tut mir leid, dass konnte ich nicht verstehen.", lang='de')
			tts.save("output.mp3")
			playsound('output.mp3')
			
		if x == 3:
			tts = gTTS(text="Ups, dass konnte nicht ausgewertet werden.", lang='de')
			tts.save("output.mp3")
			playsound('output.mp3')
		




if __name__ == '__main__':
	reco() #Führt den 'reco' Block zuerst auf
	
