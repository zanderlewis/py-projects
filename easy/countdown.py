# Difficulty: IV

import time
import sys

def countdown(t):
    print('{:02d}:{:02d}'.format(*divmod(t, 60)), '\n')
    while t:
        time.sleep(1)
        t -= 1
        mins, secs = divmod(t, 60)
        print('\033[2F\033[K{:02d}:{:02d}'.format(mins, secs), '\n')
    print('\033[2F\033[KCountdown Over!')

try:
    t = int(input("Enter the time in seconds: "))
    countdown(int(t))
except KeyboardInterrupt:
    print('\033[2F\033[KCountdown Stopped!')
    sys.exit(0)
