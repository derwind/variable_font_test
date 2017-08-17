#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, re
from robofab.world import OpenFont

UPM = 1000
XSCALE = 1. * 2400/UPM
YSCALE = 1. * 2400/UPM

def main():
    path = re.sub(r"{}+$".format(os.sep), "", sys.argv[1])
    font = OpenFont(path)

    g = font["uni6211"]
    for con in g:
        for pt in con.points:
            pt.x = round(pt.x * XSCALE, 2)
            pt.y = round(pt.y * YSCALE, 2)
    g.width = int(g.width * XSCALE)
    font.save("scaled.ufo")

if __name__ == "__main__":
    main()
