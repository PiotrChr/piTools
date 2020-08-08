default: start_linux

pip:
	pip install $(i) && pip freeze | grep $(i) >> requirements.txt

install_pi:
	sh resources/setup/pi.sh

install_mac:
	sh resources/setup/mac.sh

start_pi:
	LD_PRELOAD=/usr/lib/arm-linux-gnueabihf/libatomic.so.1 python3 controlCenter.py -m f

start_mac:
	python3 controlCenter.py

start_fullscreen_mac:
	python3 controlCenter.py -m f
