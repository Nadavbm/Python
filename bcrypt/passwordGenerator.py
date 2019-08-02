#!/usr/bin/python
import bcrypt
import argparse
import sys
import os

parser = argparse.ArgumentParser()

parser.add_argument("--password","-p", help="Type the password as a parameter", type=str)

args = parser.parse_args()

password = args.password

def main():
    pass1 = bcrypt.hashpw(password, bcrypt.gensalt(12))
    print(pass1)

main()
