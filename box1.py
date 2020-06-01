#!/usr/bin/env python3
# coding=utf-8

class hola(object):
    """docstring for hola."""

    def __init__(self):
        super(hola, self).__init__()

    def saludar(self, arg):
        print("Hola ", arg)


def main():
    hola.saludar(hola, "alcachofa")


if __name__ == "__main__":
    main()
