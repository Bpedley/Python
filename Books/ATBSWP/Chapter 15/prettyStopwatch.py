#! python3
# prettyStopwatch.py - A simple stopwatch program.

import time, pyperclip

print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. \
Press Ctrl-C to quit.')
input()
print('Started.')
startTime = time.time()
lastTime = startTime
lapNum = 1
laps = []

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        lap = 'Lap #%s: %s (%s)' % (str(lapNum).rjust(2), str(totalTime).rjust(5), str(lapTime).rjust(5))
        print(lap)
        laps.append(lap)
        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:
    text = ''
    for line in laps:
        text += line + "\n"
    pyperclip.copy(text)
    print('\nDone.')