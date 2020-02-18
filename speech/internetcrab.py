from bs4 import BeautifulSoup
import requests
import re

# WETTER:

r = requests.get("https://www.wetter.com/deutschland/*ort*/*kennnummer*.html")
soup = BeautifulSoup(r.text, 'html.parser')
str1 = soup.find("p", class_="json-ld-answer")
for s in str1:
	iweather = re.sub('<[^>]*>', '', s)
	#print(iweather)
