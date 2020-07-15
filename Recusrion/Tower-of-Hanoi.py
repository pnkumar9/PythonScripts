#!/usr/bin/env python3


def towerOfHanoi(disks, src, dst, temp):
    if disks == 1:
        print(f"move disk from {src} to {dst}")
    else:
        towerOfHanoi(disks-1, src, temp, dst)
        print(f"move disk from {src} to {dst}")
        towerOfHanoi(disks-1, temp, dst, src)

towerOfHanoi(5, "A", "B", "C")