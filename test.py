from ping3 import ping, verbose_ping
import os
import time


def m1():
    while True:
        if ping("google.com"):
            print(ping("google.com"))
        else:
            print("i will stop network")
            os.system("service network-manager stop")
            time.sleep(30)
            print(" i will start network")
            os.system("service network-manager start")
            break

    #        time.sleep(30)
    m1()

m1()
