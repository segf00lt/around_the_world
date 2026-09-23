#!/usr/bin/env python3

UNREACHABLE = False

import csv
import sys

assert len(sys.argv) == 2

initial = "<"
blank = "_"

tapes = [list(initial), list(initial)]
tape_pos = [1, 1]

transition_table_csv = open(sys.argv[1], "r")
transition_table = [row for row in csv.DictReader(transition_table_csv)]

input_word = input('enter input symbols: ')
tapes[0].extend(list(input_word))
tapes[1].extend(list(blank * len(input_word)))

def transition(cur_state, symbols):
    for row in transition_table:
        if int(row['state']) == int(cur_state) and \
           row['symbol1'] == symbols[0] and \
           row['symbol2'] == symbols[1]:
            return row
    return None

cur_state = 0

while True:
    for tape in tapes:
        if tape_pos[tapes.index(tape)] >= len(tape):
            tape.extend(list(blank * len(tape)))

    symbols = [tapes[i][tape_pos[i]] for i in range(2)]

    row = transition(cur_state, symbols)

    if row == None:
        break

    cur_state = int(row['new_state'])

    tapes[0][tape_pos[0]] = row['new_symbol1']
    tapes[1][tape_pos[1]] = row['new_symbol2']

    for i in range(2):
        if row[f'direction{i + 1}'] == 'D':
            tape_pos[i] += 1
        elif row[f'direction{i + 1}'] == 'E':
            tape_pos[i] -= 1
        else:
            assert UNREACHABLE

print('tape 1: ' + ''.join(tapes[0]).strip('_'))
print('tape 2: ' + ''.join(tapes[1]).strip('_'))
