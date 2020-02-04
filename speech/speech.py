import speech_recognition as sr
import sys
from gTTs import gTTs

y = 1
while y == 1:
	r = sr.Recognizer()

	with sr.Microphone() as source:
		print('Listen..')
		audio = r.listen(source)

	try:
		print(r.recognize_google(audio))
	except:
		pass
else:
	y = 1
