#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    09b.py
    ~~~~~~
    Advent of Code 2017 - Day 9: Stream Processing
    Part Two

    Now, you're ready to remove the garbage.

    To prove you've removed it, you need to count all of the characters within
    the garbage. The leading and trailing < and > don't count, nor do any
    canceled characters or the ! doing the canceling.

     - <>, 0 characters.
     - <random characters>, 17 characters.
     - <<<<>, 3 characters.
     - <{!>}>, 2 characters.
     - <!!>, 0 characters.
     - <!!!>>, 0 characters.
     - <{o"i!a,<{i<a>, 10 characters.

    How many non-canceled characters are within the garbage in your puzzle
    input?

    :copyright: (c) 2017 by Martin Bor.
    :license: MIT, see LICENSE for more details.
"""

import sys


def garbage(stream):
    """Skip over any garbage in the stream, properly handling escaped (!)
    characters, and counting all characters.

    :stream: stream of characters
    :returns: number of garbage characters
    """
    count = 0

    for c in stream:
        if c == '!':
            # escape, skip the next char
            next(stream)
        elif c == '>':
            return count
        else:
            count += 1


def group(stream):
    """Return total number of garbage characters in this subgroup

    :stream: stream of character
    :returns: total number of garbage characters
    """
    count = 0

    for c in stream:
        if c == '}':
            return count
        elif c == '<':
            count += garbage(stream)
        elif c == '{':
            count += group(stream)

    return count


def solve(stream):
    """Count total number of garbage characters in the stream.

    :stream: stream of characters
    :return: total number of garbage characters

    >>> solve('{<>}')
    0
    >>> solve('{<random characters>}')
    17
    >>> solve('{<<<<>}')
    3
    >>> solve('{<{!>}>}')
    2
    >>> solve('{<!!>}')
    0
    >>> solve('{<!!!>>}')
    0
    >>> solve('{<{o"i!a,<{i<a>}')
    10
    """

    return group(iter(stream))


def main(argv):
    if len(argv) == 2:
        f = open(argv[1], 'r')
    else:
        sys.stderr.write('reading from stdin...\n')
        f = sys.stdin
    print(solve(f.read().strip()))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
