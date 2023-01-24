def getFileInput(file, nice=False):
    with open(file, 'r') as f:
        text = f.readlines()
    if nice:
        for i in range(len(text)):
            text[i] = str(text[i]).replace('\n', '')
    return text


def getPf(file):
    numbers = getFileInput(file, True)
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])

    return numbers


def getLog():
    text = getFileInput('log.txt')
    for i in range(len(text)):
        try:
            text[i] = text[i].split(':')[1].lower().replace('\n', '')
        except:
            continue
    run = True
    x = 1
    na = ['', ' ', '\n', None]
    while run:
        if str(text[len(text) - x]) in na:
            x += 1
            continue
        else:
            return str(text[len(text) - x])


def writeLog(idt, num):
    with open('log.txt', 'a') as f:
        f.write(f'{idt}:{num}\n')


def getRange():
    start = int(getLog()) + 1
    if start % 2 == 0:
        start += 1
    end = start + 5000
    return start, end


def checkControl():
    text = getFileInput('control.txt', True)
    if str(text[0]).lower() == 'stop':
        return False
    else:
        return True


def checkPrime(num:int, pf:list):
    for z in pf:
        if int(num) % int(z) == 0:
            return False
    return True


def appendNumber(num:int):
    with open('primfaktoren.txt', 'a')  as f:
        f.write(f'{str(num)}\n')


def logout(idt):
    try:
        mes = getLog()
        writeLog(idt, f'ready {int(getLog().split(" ")[1]) + 1}')
    except:
        writeLog(idt, f'ready 1')


def writeNice():
    li = getPf('primfaktoren.txt')
    li.sort()
    for i in range(len(li)):
        li[i] = f'{str(li[i])}\n'
    li = ''.join(li)
    with open('primfaktoren.txt', 'w') as f:
        f.write(li)
