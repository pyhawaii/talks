# Excerpted from Violent Python, by TJ O'Connor
# Revised to account for python 3 and changes to several libraries.

import time
start = time.time()

import optparse
import socket
from socket import *                  # note... this is not ideal/pythonic

def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('GET / HTTP/1.1\r\n\r\n'.encode())
        results = connSkt.recv(512).decode()
        print('{}/tcp open'.format(tgtPort), '\n')
        print('Banner:\n' + results + '\n')
        connSkt.close()
    except Exception as err:
        print('{}/tcp closed'.format(tgtPort), err, '\n')

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print("Cannot resolve '{}': Unknown host".format(tgtHost))
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print('\nScan Results for: {}'.format(tgtName[0]), '\n')
    except:
        print('\nScan Results for: {}'.format(tgtIP))
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print('Scannning port {}'.format(tgtPort))
        connScan(tgtHost, int(tgtPort))

def main():

    parser = optparse.OptionParser('usage %prog -H <target host> -p <target port>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string', 
                      help='specify target port[s] separated by commas')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(', ')

    if (tgtHost == None) | (tgtPorts[0] == None):
        print(parser.usage)
        exit()
    portScan(tgtHost, tgtPorts)

    end = time.time()
    print("Time: ", end - start)

if __name__ == '__main__':
    main()
