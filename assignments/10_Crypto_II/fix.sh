#!/bin/sh
dd conv=notrunc if=original.bmp of=ecb.bmp bs=54 count=1
dd conv=notrunc if=original.bmp of=cbc.bmp bs=54 count=1
