import os
import threading
import time
from file import *

def setup():
    with open('control.txt', 'w') as f:
        f.write('start')
    if not os.path.exists('primfaktoren.txt'):
        with open('primfaktoren.txt', 'w') as f:
            f.write('2\n')
    if not os.path.exists('log.txt'):
        with open('log.txt', 'w') as f:
            f.write('0:2\n')
    elif os.path.exists('log.txt'):
        last = getPf('primfaktoren.txt')
        writeLog(0, last[len(last)-1])


def startThread(ta, a):
    t = threading.Thread(target=ta, args=str(a))
    t.start()


def getInput(anzahlThreads):
    run = True
    while run:
        x = input('Anweisung: ')
        if str(x).lower() == 'stop':
            with open('control.txt', 'w') as f:
                f.write('stop')
            run = False
    x = 0
    end = False
    while not end:
        try:
            if int(getLog().split(' ')[1]) == int(anzahlThreads):
                end = True
                time.sleep(1)
                try:
                    writeNice()
                    print('Done with sorting')
                except:
                    print('Done without sorting')
        except:
            x += 1
            time.sleep(1)
        if x == 10:
            end = True
            print('Timeout Error')



def arbeit(idt):
    pf = getPf('primfaktoren.txt')

    run = True
    found = 0
    while run:
        start, end = getRange()
        writeLog(idt, end)

        for i in range(int(start), int(end) + 1, 2):
            if checkPrime(i, pf):
                pf.append(i)
                appendNumber(i)
                found += 1

        if not checkControl():
            run = False

    print(f'Gefundene Primzahlen Thread {idt}: {found}')
    logout(idt)


setup()
startThread(arbeit, 1)
startThread(getInput, 3)
time.sleep(1)
startThread(arbeit, 2)
time.sleep(0.1)
startThread(arbeit, 3)
