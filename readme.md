Pi Chatter
----------

This is an electronics project that allows you to listen in remotely
with your Raspberry Pi and talk back like a virtual assistant.
It is part of a project to make autonomous robots more interactive.

It is built on top of Google's AIY Voice Kit v2 here
https://aiyprojects.withgoogle.com/voice/


Steps
-----

Below is a minimal, non-exaustive, set of instructions to get you up
and started quickly. I have provided further links in case you get
stuck and/or would like to understand some aspects in more detail.


1. Flash your SD Card with the AIY system image

Install https://etcher.io/

Get the latest image at https://github.com/google/aiyprojects-raspbian/releases

Full details are in Google's AIY Voice Kit homepage.


2. Enable SSH through USB, and enter your WiFI credentials

On the SD Card, add at the end of `config.txt`:

```
dtoverlay=dwc2
```

In `cmdline.txt`, add the following after `rootwait` (leaving only a 1 space gap):

```
modules-load=dwc2,g_ether
```

On the SD Card, create a new file `wpa_supplicant.conf` and enter the below,
making the appropriate edits:

```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=<Insert 2 letter ISO 3166-1 country code here>

network={
 ssid="<Name of your wireless LAN>"
 psk="<Password for your wireless LAN>"
}
```

Full instructions here:
https://desertbot.io/blog/ssh-into-pi-zero-over-usb

And here:
https://www.raspberrypi.org/documentation/configuration/wireless/headless.md

3. If you have not connected the Voice Bonnet or Speaker to the Raspberry Pi
yet, please do so now.


4. First Boot

Connect your Raspberry Pi to power using USB.
For first boot-up, give it a minute and a half to load fully.


5. Set up UV4L and WebRTC

These are the minimal set of commands to install UV4L and set it up.
You may wish to run these _one line at a time_.

```bash
curl -s -L http://www.linux-projects.org/listing/uv4l_repo/lpkey.asc | sudo apt-key add -
sudo bash -c 'echo "deb http://www.linux-projects.org/listing/uv4l_repo/raspbian/stretch stretch main" >> /etc/apt/sources.list'
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install uv4l-webrtc-armv6 -y
sudo apt-get install uv4l-raspicam-extras -y

sudo raspi-config  # Enable the camera (if attached)
sudo nano /etc/uv4l/uv4l-raspicam.conf  # Edits are shown below
```

Uncomment and modify the following lines in the `/etc/uv4l/uv4l-raspicam.conf` file:

```apacheconf
### WebRTC options:
server-option = --enable-webrtc=yes
server-option = --enable-webrtc-datachannels=yes
server-option = --webrtc-datachannel-label=uv4l
server-option = --webrtc-datachannel-socket=/tmp/uv4l.socket
# server-option = --webrtc-old-sctp-syntax=true
server-option = --enable-webrtc-video=no
server-option = --enable-webrtc-audio=yes
```

Restart UV4L with this:

```bash
sudo service uv4l_raspicam restart
```

Test that it is working at this link
http://raspberrypi.local:8080/stream/webrtc
Click on the green "Call!" button at the bottom. You should be able
to hear everything that the Raspberry Pi picks up.

Further detailed instructions for UV4L can be found here:
https://www.linux-projects.org/uv4l/installation/
and here:
https://www.highvoltagecode.com/post/webrtc-on-raspberry-pi-live-hd-video-and-audio-streaming


6. Git clone this repo into your Raspberry Pi's home folder

```bash
git clone https://github.com/borobaya/pi-chatter.git
```

7. Run and check that it works

Start the flask server:

```bash
cd pi-chatter
python3 index.py
```

On your laptop, go to the link:
http://raspberrypi.local:8000/

Edit the sound volume using this:

```bash
alsamixer
```


