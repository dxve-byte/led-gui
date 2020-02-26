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
from compare import *

####################################################### Requirements ################################################
# pip3 install SpeechRecognition ; [for Speech to Text]
# Herunterladen: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio (PyAudio‑0.2.11‑cp37‑cp37m‑win_amd64.whl)
# zu Downloads wechseln und manuell installieren: (cd Downloads, pip install PyAudio-0.2.11-cp37-#cp37m-win_amd64.whl)
# pip3 install gTTS ; for text to Speech
# pip3 install mpyg321 ; for output
# pip3 install bs4 ; for Internet crab
# python -m pip install requests
# pip3 install playsound
#
# 	FOR ERRORS WITH PYAUDIO:
# git clone https://github.com/jleb/pyaudio.git
# cd pyaudio
# sudo python3 setup.py install
#
# 	FOR ERRORS WITH FLAC:
# sudo ln -s /usr/local/bin/flac /usr/sbin
#
# 	FOR ERRORS WITH AUDIO OUTPUT:
# sudo apt-get install libgstreamer1.0-dev libgstreamer1.0-0-dbg libgstreamer1.0-0 gstreamer1.0-tools gstreamer-tools gstreamer1.0-doc gstreamer1.0-x
#
#	For Mails:
# pip install secure-smtplib
# pip install python-imap
# pip install email
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

global silentmode

def reco():
	try:										# Versucht ein Mikro zu finden
		r = sr.Recognizer()
		with sr.Microphone() as source:
												# hört zu und nimmt auf
			print("Höre zu..")
			audio = r.listen(source)
				
												# Versucht das Gesprochene mittels Google zu reconieren und in Text umzuwandeln
			result = r.recognize_google(audio, language="de_DE")
			compares(result)				# Wenn ALLES geklappt hat, wird es ausgewertet(compare block)
							
					
	except:
		error()



def compares(result):
	result = result.lower() 						# setzt alles auf Kleinbuchstaben, um die Vergleichung zu vereinfachen
	ressplit = result.split()
	print(result)
	
	
	
	exac = []
	bin = []
	resultlist = []
	
	
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
	
	if highestval == second_highestval:					# Macht jetzt den Vergleichung
		print("Type Error: To many results, need an exact result..")				# Fehler
	else:
		exac.insert(pos, highestval)				# fügt höchste Zahl wieder hinzu
							
	


	# ############################################################
	# ############### WELCHE LIST PASST AM BESTEN ZUM SATZ #################
	# ############################################################

		
		groupspos = exac[pos]
		print(groupsdic.keys())
		forfunc = list(groupsdic.keys())[pos]
		func(forfunc)
			
def func(forfunc):
	print("Worked :", forfunc)
	

def error():

	try:
		tts = gTTS(text="Fehler. Bitte Internetverbindung, Code oder Mikro überprüfen.", lang='de')
		tts.save("output.mp3")
		playsound('output.mp3')
	except:
		print("Error with permission in Function Error(). Still not too bad..")




if __name__ == '__main__':
	reco() #Führt den 'reco' Block zuerst auf
	
