#!/usr/bin/env bash

brew cask install anaconda
export PATH="/usr/local/anaconda3/bin:$PATH"
source ~/.zshrc
make pip_mac