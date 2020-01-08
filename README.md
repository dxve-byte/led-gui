!!!THIS CODE BELOW IS NOT MY PROJECT!!!
Full TUTORIAL: https://www.youtube.com/watch?v=FA9rMkuVmvQ&t=558s
BE PATIENT with installing

# led-gui

__INSTALL / PATH's:__


IMAGE: https://www.raspberrypi.org/downloads/raspbian/


__COMMANDS:__

(https://github.com/scottlawsonbc/audio-reactive-led-strip)

sudo apt-get install build-essential python-dev git scons swig

sudo git clone https://github.com/jgarff/rpi_ws281x.git

cd rpi_ws281x

scons

cd python

sudo python setup.py install

cd examples

__Then run:__ sudo python strandtest.py __(LED_PIN: 18!)__
(https://www.elektronik-kompendium.de/sites/raspberry-pi/1907101.htm)

__AUDIO DEVICE CONFIGURATION: (USES JACK-AUDIO)__

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

cd /dancyPi-audio-reactive-led/python/

sudo python visualization.py



If there is an Error then use this command:

sudo python visualization.py /tmp
