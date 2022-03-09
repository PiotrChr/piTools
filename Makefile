rotate180:
	DISPLAY=:0 xrandr --output HDMI-1 --rotate inverted

rotateNormal:
	DISPLAY=:0 xrandr --output HDMI-1 --rotate normal

setupUSBcamera:
	sudo apt-get install fswebcam -y \
	&& sudo apt-get install libatlas-base-dev libjasper-dev -y \
	&& python3 -m pip install --upgrade pip \
	&& pip3 install --upgrade pip setuptools wheel \
	&& pip3 install -r requirements.txt

testWebcam:
	python3 scripts/testWebcam.py


