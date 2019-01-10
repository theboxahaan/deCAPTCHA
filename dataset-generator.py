#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 10:50:38 2018

@author: ahaandabholkar
"""

from captcha.audio import AudioCaptcha
from random import randint

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

audio = AudioCaptcha()
for i in range(100):
       t =str(random_with_N_digits(4))
       audio.write(t,'init_dataset/'+t+'.wav')
