from os import system
from sys import exit, stdout
import signal
from random import choice
from time import time

# All available notes
NOTES = [
    'C',
    'D flat',
    'D',
    'E flat',
    'E',
    'F',
    'F sharp',
    'G',
    'Ay flat',
    'Ay',
    'B flat',
    'B'
]

STRINGS = [
    'E string',
    'Ay string',
    'D string',
    # 'G',
    # 'C',
    # 'B',
]

# Determine bpm
try:
    bpm = int(input('BPM (will only approximate BPM): '))
except Exception as e:
    exit(f'{e} -> Please enter a valid bpm')

# Determine string
fixed_string = input('Choose a string: ')


def wait(delay):
    delay = 60 / delay
    end_time = time() + delay
    while end_time > time():
        continue

# Ensure interruption signal stops program
run = True
def signal_handler(signal, frame):
    global run
    print("exiting")
    run = False

signal.signal(signal.SIGINT, signal_handler)

curr_string = STRINGS[0]

while run:
    randomly_selected_string = choice(STRINGS)
    if not fixed_string and randomly_selected_string != curr_string:
        command = 'say ' + f'\"{randomly_selected_string}\"'
        curr_string = randomly_selected_string
        system(command)
        next

    randomly_selected_note = choice(NOTES)
    stdout.write('\033[2K\033[1G')
    print(randomly_selected_note.replace('Ay', 'A') if 'Ay' in randomly_selected_note else randomly_selected_note, end="\r")

    command = 'say ' + f'\"{randomly_selected_note}\"'
    system(command)

    wait(bpm)

