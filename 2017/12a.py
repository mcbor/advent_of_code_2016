#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    12a.py
    ~~~~~~
    Advent of Code 2017 - Day 12: Digital Plumber
    Part One

    Walking along the memory banks of the stream, you find a small village that
    is experiencing a little confusion: some programs can't communicate with
    each other.

    Programs in this village communicate using a fixed system of pipes.
    Messages are passed between programs using these pipes, but most programs
    aren't connected to each other directly. Instead, programs pass messages
    between each other until the message reaches the intended recipient.

    For some reason, though, some of these messages aren't ever reaching their
    intended recipient, and the programs suspect that some pipes are missing.
    They would like you to investigate.

    You walk through the village and record the ID of each program and the IDs
    with which it can communicate directly (your puzzle input). Each program
    has one or more programs with which it can communicate, and these pipes are
    bidirectional; if 8 says it can communicate with 11, then 11 will say it
    can communicate with 8.

    You need to figure out how many programs are in the group that contains
    program ID 0.

    For example, suppose you go door-to-door like a travelling salesman and
    record the following list:

        0 <-> 2
        1 <-> 1
        2 <-> 0, 3, 4
        3 <-> 2, 4
        4 <-> 2, 3, 6
        5 <-> 6
        6 <-> 4, 5

    In this example, the following programs are in the group that contains
    program ID 0:

     - Program 0 by definition.
     - Program 2, directly connected to program 0.
     - Program 3 via program 2.
     - Program 4 via program 2.
     - Program 5 via programs 6, then 4, then 2.
     - Program 6 via programs 4, then 2.

    Therefore, a total of 6 programs are in this group; all but program 1,
    which has a pipe that connects it to itself.

    How many programs are in the group that contains program ID 0?

    :copyright: (c) 2017 by Martin Bor.
    :license: MIT, see LICENSE for more details.
"""

import sys
from collections import defaultdict


def solve(pipes):
    """Return number of programs that contain program ID 0 (i.e. are reachable
    from program ID 0).

    :pipes: string of pipes separated by newlines.
    :return: number of proframs that contain program ID 0

    >>> solve('''0 <-> 2
    ... 1 <-> 1
    ... 2 <-> 0, 3, 4
    ... 3 <-> 2, 4
    ... 4 <-> 2, 3, 6
    ... 5 <-> 6
    ... 6 <-> 4, 5''')
    6
    """

    graph = defaultdict(set)

    for line in pipes.split('\n'):
        pid, _, *tail = line.split()
        graph[pid].update(n.strip(', ') for n in tail)

    visited = set()
    stack = ['0']

    while stack:
        v = stack.pop()
        visited.add(v)

        for n in graph[v]:
            if n not in visited:
                stack.append(n)

    return len(visited)


def main(argv):
    if len(argv) == 2:
        f = open(argv[1], 'r')
    else:
        sys.stderr.write('reading from stdin...\n')
        f = sys.stdin
    print(solve((f.read().strip())))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
