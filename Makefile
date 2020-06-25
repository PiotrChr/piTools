default: start

start:
	LD_PRELOAD=/usr/lib/arm-linux-gnueabihf/libatomic.so.1 python3 controlCenter.py
