
# PYTHON SPEECHRECOGNITION by dxve

# *ACHTUNG GOOGLE HAT ANTEILE (Er ist hier für die "Speech to Text" Sache zuständig)*

#Eine Sprachsteuerung für eigene Sprachbefehle und einen Überblick über seine Daten


import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os


#Dateien
from internetcrab import *
from RE import *

####################################################### Requirements ################################################
#pip install SpeechRecognition ; [for Speech to Text]
#Herunterladen: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio (PyAudio‑0.2.11‑cp37‑cp37m‑win_amd64.whl)
#zu Downloads wechseln und manuell installieren: (cd Downloads, pip install PyAudio-0.2.11-cp37-#cp37m-win_amd64.whl)
#pip install gTTS ; for text to Speech
#pip install mpyg321 ; for output
#pip install bs4 ; for Internet crab
#python -m pip install requests
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

	try:											# Versucht ein Mikro zu finden
		r = sr.Recognizer()
		with sr.Microphone() as source:
		
			try:									# hört zu und nimmt auf
				print("Höre zu..")
				audio = r.listen(source)
					
				try:								# Versucht das Gesprochene mittels Google zu reconieren und in Text umzuwandeln
					result = r.recognize_google(audio, language="de_DE")
					compares(result)				# Wenn ALLES geklappt hat, wird es ausgewertet(compare block)
							
					#tts = gTTS(text=outputs, lang='de')
					#tts.save("output.mp3")
					#playsound('output.mp3')
				except:
					error(3) 						# Fehler 3 -> wird weitergegeben und ausgewertet
			except:
				error(2) 							# Fehler 2 -> wird weitergegeben und ausgewertet
	except:
		error(1) 									# Fehler 1 -> wird weitergegeben und ausgewertet
	
global sleepmode
sleepmode = "false"


def compares(result):
	result = result.lower() 						# setzt alles auf Kleinbuchstaben, um die Vergleichung zu vereinfachen
	print(result)
	
	
	
	exac = []
	bin = []
	resultlist = []


	groups = [welcomegroup, timegroup, weathergroup, howareyougroup, whereareyougroup, insultgroup, sleeptruegroup, sleepfalsegroup]
	
	for all in groups:


		for element in all:								# element = [hey, hallo, hallöchen] usw.
			if element in result:						# Passt Element zu result-string
				#lastword = resultlist[1]
				bin.insert(0, element)					# Fügt neues Element bei "Bin" hinzu
		exac.insert(999999, len(bin))					# Zählt List(bin) und fügt die Anzahl in eine neue List zu
		bin.clear()										# Löscht die "Bin"-list
	
	
	
	highestval = max(exac)								# Wählt die höchste Zahl aus
	print("exac:", exac)
	pos = exac.index(highestval)						# Postition von der höchsten Zahl

	#print(pos)

	# ############################################################
	# ############### WELCHE LIST PASST AM BESTEN ZUM SATZ #################
	# ############################################################


	if robotname in result:
		#Hier geht er zur Datei RE.py um darauf zu Antworten
		if pos == 0:
			groupname = "welcomegroup"
			welcome()
		if pos == 1:
			groupname = "timegroup"
			time()
		if pos == 2:
			groupname = "weathergroup"

			resultlist = result.split()						# schneidet alle Wörter im resultstring aus
			ort = resultlist[resultlist.index("in") + 1]	# sucht "in" und nimmt den ORT [nächstes Wort]
			
			
			r = requests.get("https://www.wetteronline.de/wetter/" + ort)			# hohlt sich URL
			soup = BeautifulSoup(r.text, 'html.parser')								# parst die Seite
			str1 = soup.find(id="forecasttext")										# findet id
			str1.prettify()
			iweather = re.sub('<[^>]*>', '', str(str1))								# löscht Zeichen (<p></p> ; usw.)
			
			weather(iweather)														# startet weather()
			
		if pos == 3:
			groupname = "howareyougroup"
			hay()
		if pos == 4:
			groupname = "whereareyougroup"
			way()
		if pos == 5:
			groupname = "insultgroup"
			insult()
		if pos == 6:
			groupname = "sleeptruegroup"
			sleeptrue()
			sleepmode = "true"
		if pos == 7:
			groupname = "sleepfalsegroup"
			sleepfalse()
			sleepmode = "false"
			
		print("I think I can classify this in group ", groupname)
	
	

def error(x):

	#sleepmode = ""
	print("sleepmode: ", sleepmode)
	if sleepmode == "false":
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
	
