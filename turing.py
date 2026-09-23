#!/usr/bin/env python3

UNREACHABLE = False

import csv
import sys

assert len(sys.argv) == 2

initial = "<"
blank = "_"
tape = initial
tape_pos = 1
tape = list(tape)

transition_table_csv = open(sys.argv[1], "r")
transition_table = [row for row in csv.DictReader(transition_table_csv)]

input_word = input('enter input symbols: ')
tape.extend(list(input_word))

def transition(cur_state, cur_symbol):
    for row in transition_table:
        if int(row['state']) == int(cur_state) and row['symbol'] == cur_symbol:
            return row
    return None

cur_state = 0

while True:
    assert tape_pos >= 0

    if tape_pos >= len(tape):
        tape.extend(list(blank*len(tape)))
        #print(tape)

    try:
        row = transition(cur_state, tape[tape_pos])
    except:
        breakpoint()

    if row == None:
        break

    new_state = row['new_state']
    new_symbol = row['new_symbol']
    direction = row['direction']

    cur_state = int(new_state)
    tape[tape_pos] = new_symbol
    
    if direction == 'D':
        tape_pos += 1
    elif direction == 'E':
        tape_pos -= 1
    else:
        assert UNREACHABLE

    

print('tape: ' + ''.join(tape).strip('_'))
