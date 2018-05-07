#!/usr/bin/python3

# Kimberly Decker
# Adapted from Violent Python
# Exercise to convert python 2 program to python 3
# March 2, 2018
#
# *********************************************************************
# TCP port scanner with threading
# *********************************************************************


from socket import *
from threading import *


def connScan(tgtHost, tgtPort):
    """Function to evaluate open/closed ports"""
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('Violent Python\r\n'.encode())
        results = connSkt.recv(100)
        print('[+] tcp open port ' + str(tgtPort))
        print('[+] ' + str(results))
    except Exception as e:
        print(e)
        print('[-] tcp closed port ' + str(tgtPort))
    finally:
        connSkt.close()

def portScan(tgtHost, tgtPorts):
    """Function to scan for ports"""
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print("[-] Cannot resolve IP: Unknown host" + str(tgtHost))
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print('\n[+] Scan results for: ' + tgtName[0])
    except:
        print('\n[+] Scan results for: ' + tgtIP)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()

def main():
    tgtHost = '10.0.3.198'
    tgtPorts = ['22', '80','443', '80']
    print(tgtHost)
    print(tgtPorts)
    portScan(tgtHost, tgtPorts)

if __name__ == '__main__':
    main()
