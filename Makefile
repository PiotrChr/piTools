default: start

start:
    sudo LD_PRELOAD=/usr/lib/arm-linux-gnueabihf/libatomic.so.1 python3 contronCenter.py
