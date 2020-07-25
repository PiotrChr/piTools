default: start_linux

start_linux:
	LD_PRELOAD=/usr/lib/arm-linux-gnueabihf/libatomic.so.1 python3 controlCenter.py -m f

start_mac:
	python3 controlCenter.py

start_fullscreen_mac:
	python3 controlCenter.py -m f
