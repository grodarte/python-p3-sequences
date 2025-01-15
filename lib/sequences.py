#!/usr/bin/env python3

def print_fibonacci(length):
    s = []
    i = 0
    while i < length:
        if i < 2:
            s.append(i)
        else:
            s.append(s[-1] + s[-2])
        i += 1
    print(s)