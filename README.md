# led-gui

INSTALL / PATH's:


IMAGE: https://www.raspberrypi.org/downloads/raspbian/


COMMANDS:

(https://github.com/scottlawsonbc/audio-reactive-led-strip)

sudo apt-get install build-essential python-dev git scons swig

sudo git clone https://github.com/jgarff/rpi_ws281x.git

cd rpi_ws281x

scons

cd python

sudo python setup.py install

cd examples

Then run: sudo python strandtest.py (LED_PIN: 18!)
(https://www.elektronik-kompendium.de/sites/raspberry-pi/1907101.htm)

AUDIO DEVICE CONFIGURATION: (USES JACK-AUDIO)

sudo nano /etc/asound.conf

SET FILE TO FOLLOWING TEXT:

pcm.!default {

    type hw
    
    card 1
    
}

ctl.!default {

    type hw
    
    card 1
    
}

NEXT STEP:

sudo nano /usr/share/alsa/alsa.conf

Change

defaults.ctl.card 0

defaults.pcm.card 0

To

defaults.ctl.card 1

defaults.pcm.card 1

___Finish___


