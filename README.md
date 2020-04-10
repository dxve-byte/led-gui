!!!THIS is an Tutorial for LED controlling!!!

Full TUTORIAL: https://www.youtube.com/watch?v=FA9rMkuVmvQ&t=558s

BE PATIENT with installing

# led-gui

__INSTALL / PATH's:__

IMAGE: https://www.raspberrypi.org/downloads/raspbian/


__COMMANDS:__

__change__ sudo nano /boot/config.txt 

__to__ led-gui/config.txt (replace the text from my GIT | you can remove config.txt: sudo rm /boot/config.txt and create a new with sudo nano /boot/config.txt THEN paste the Text from my GIT[config.txt])

(https://github.com/scottlawsonbc/audio-reactive-led-strip)

sudo apt-get install build-essential python-dev git scons swig

sudo git clone https://github.com/jgarff/rpi_ws281x.git

cd rpi_ws281x

sudo scons

cd python

sudo python setup.py install

cd examples

__Then run:__ sudo python strandtest.py __(LED_PIN: 18!)__
(https://www.elektronik-kompendium.de/sites/raspberry-pi/1907101.htm)

__ERROR?__

Try to change the LED_PIN with "sudo nano strandtest.py".

__AUDIO DEVICE CONFIGURATION: (USES JACK-AUDIO)__

cd

sudo nano /etc/asound.conf

__SET FILE TO FOLLOWING TEXT:__

pcm.!default {

    type hw
    
    card 1
}

ctl.!default {

    type hw
    
    card 1
}

__NEXT STEP:__

sudo nano /usr/share/alsa/alsa.conf

__Change__

defaults.ctl.card 0

defaults.pcm.card 0

__To__

defaults.ctl.card 1

defaults.pcm.card 1

___Finish___



__Audio Reactive LED's__

sudo apt-get update

sudo apt-get install python-numpy python-scipy python-pyaudio

sudo apt install python-pyqtgraph

sudo git clone https://github.com/naztronaut/dancyPi-audio-reactive-led.git

__Run script:__

cd dancyPi-audio-reactive-led/python/

sudo python visualization.py



__ERRORS:__


change PIN with "sudo nano config.py" 
!!! Pick your Device, Pi is normal !!! 
USE_GUI = True 
DISPLAY_FPS = False 

sudo python visualization.py /tmp


__NOW MY PROJECT!__

cd

mkdir led-gui/

mkdir led-gui/LED/

sudo rsync -r /home/pi/dancyPi-audio-reactive-led/python/* /home/pi/led-gui/LED/

sudo rsync -r /home/pi/rpi_ws281x/python/examples/strandtest.py /home/pi/led-gui/LED/

sudo git clone https://github.com/dxve-byte/led-gui/ temp

sudo mv temp/* led-gui/

sudo mv temp/LED/* led-gui/LED/

sudo rm -r temp

__ERROR?__

cd led-gui/LED/

sudo chmod 777 config.py

sudo nano config.py

__CHANGE__

USE_GUI = False

__TO__

USE_GUI = True


With command "ls" you see what files in the directory are!

__FINSIH__

__THE GUI__

sudo apt-get update

sudo apt-get install apache2

sudo apt-get install php

cd /var/www/html/

sudo rm *

__After that, include the GUI files from my GitHub to this Folder:__

cd

sudo rsync -r led-gui/GUI/* /var/www/html/

__The Webserver has no rights to execute the Comments, so:__

sudo visudo

This Text at the end: www-data ALL=NOPASSWD: ALL

