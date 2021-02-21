#!/usr/bin/env bash

sudo apt install matchbox-keyboard -y

pip install netifaces

## user is allowed to execute halt and reboot
#pi ALL=NOPASSWD: /sbin/halt, /sbin/reboot, /sbin/poweroff