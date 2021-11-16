#!/usr/env/python3 
# Author : 7h3h4ckv157
# https://github.com/7h3h4ckv157
# https://twitter.com/7h3h4ckv157

import pytube; source = input("enter the link:")
src = pytube.YouTube(source)

hack=src.streams.first()
hack.download()
