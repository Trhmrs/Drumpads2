import os
import sys
import pyttsx3
import colored
import random
import time
from termcolor import colored
color=['red','magenta','yellow']
while True:
    engine=pyttsx3.init()
    engine.say(color[random.randint(0,2)])
    engine.runAndWait()
    print(colored('h', color[random.randint(0,2)]),colored('i',color[random.randint(0,2)]))
    time.sleep(1)