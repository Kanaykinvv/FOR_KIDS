#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os.path
import sys
import argparse


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', default="./", type=str)
    parser.add_argument('-c', '--count', default=1, type=int)

    return parser

def create_file(count: int, output: str):
    for i in range(count):
        with open(output + "test_file_%s" % i, "w") as file:
            file.write("0"*100)

if __name__ == '__main__':
    parser = createParser()
    args = parser.parse_args(sys.argv[1:])
    if args.output:
        print("output = " + args.output)
    if args.count:
        print("count = " + str(args.count))
    create_file(args.count, args.output)

