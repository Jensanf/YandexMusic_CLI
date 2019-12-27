import os
from time import sleep
import sys
os.system("git pull")
sleep(3)
os.system("python3 main.py {}&".format(sys.argv[1]))
