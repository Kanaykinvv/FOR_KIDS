#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import argparse


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output')
    parser.add_argument('-c', '--count', default=1, type=int)

    return parser


if __name__ == '__main__':
    parser = createParser()
    args = parser.parse_args(sys.argv[1:])
    if args.output:
        print("output = " + args.output)
    if args.count:
        print("Count = " + str(args.count))

    print(args)
